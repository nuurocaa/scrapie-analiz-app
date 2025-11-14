import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import json
import random

# GeoPandas modülünü sadece ihtiyaç duyulduğunda yükle
try:
    import geopandas as gpd
    GEOPANDAS_AVAILABLE = True
except ImportError:
    GEOPANDAS_AVAILABLE = False


# ---------------------------
# Dahili GeoJSON Verisi (Bölgeler ve Varsayılan Risk)
# ---------------------------
TURKEY_SAMPLE_GEOJSON = {
  "type": "FeatureCollection",
  "features": [
    # Kıvırcık (Trakya / Marmara Batı - ARQ ve DÜŞÜK VRQ)
    {
      "type": "Feature",
      "properties": {"name": "Edirne", "region": "Trakya", "risk": 0.45},
      "geometry": {"type": "Polygon", "coordinates": [[ [26.0, 41.5], [27.0, 41.5], [27.0, 40.5], [26.0, 40.5], [26.0, 41.5] ]]}
    },
    # Sakız (Ege Kıyı - ARR ve ÇOK DÜŞÜK VRQ)
    {
      "type": "Feature",
      "properties": {"name": "İzmir", "region": "Ege Kıyı", "risk": 0.30},
      "geometry": {"type": "Polygon", "coordinates": [[ [26.5, 38.0], [27.5, 38.0], [27.5, 37.5], [26.5, 37.5], [26.5, 38.0] ]]}
    },
    # Dağlıç (İç Anadolu Batı / Ege İç)
    {
      "type": "Feature",
      "properties": {"name": "Konya", "region": "İç Anadolu", "risk": 0.65},
      "geometry": {"type": "Polygon", "coordinates": [[ [32.0, 39.0], [33.5, 39.0], [33.5, 37.5], [32.0, 37.5], [32.0, 39.0] ]]}
    },
    # Karaman (Doğu Anadolu - ARQ)
    {
      "type": "Feature",
      "properties": {"name": "Erzurum", "region": "Doğu Anadolu", "risk": 0.80},
      "geometry": {"type": "Polygon", "coordinates": [[ [40.0, 40.5], [41.5, 40.5], [41.5, 39.0], [40.0, 39.0], [40.0, 40.5] ]]}
    },
    # Genel Risk Gösterimi (Örnek)
    {
      "type": "Feature",
      "properties": {"name": "Ankara", "region": "İç Anadolu", "risk": 0.55},
      "geometry": {"type": "Polygon", "coordinates": [[ [32.0, 40.0], [33.0, 40.0], [33.0, 39.0], [32.0, 39.0], [32.0, 40.0] ]]}
    },
    # Gökçeada (Ege Adalar - ARQ / VRQ=0)
    {
      "type": "Feature",
      "properties": {"name": "Çanakkale", "region": "Ege Adalar", "risk": 0.35},
      "geometry": {"type": "Polygon", "coordinates": [[ [25.5, 40.0], [27.0, 40.0], [27.0, 39.0], [25.5, 39.0], [25.5, 40.0] ]]}
    }
  ]
}

# ---------------------------
# NSP Risk Sınıflandırması
# ---------------------------
NSP_RISK_MAPPING = {
    # R1: En Dirençli (Skor 0-10)
    "ARR/ARR": {"group": "R1", "score": 0.5, "description": "Genetik olarak scrapie’ye en dirençli koyunlardır.", "color": "#008000"}, # Yeşil
    
    # R2: Dirençli (Kontrollü Damızlık)
    "ARR/AHQ": {"group": "R2", "score": 2.0, "description": "Dirençli, kontrollü damızlık.", "color": "#7CFC00"}, # Açık Yeşil
    "ARR/ARH": {"group": "R2", "score": 2.5, "description": "Dirençli, kontrollü damızlık.", "color": "#7CFC00"}, 
    "ARR/ARQ": {"group": "R2", "score": 3.0, "description": "Dirençli, kontrollü damızlık.", "color": "#7CFC00"}, 

    # R3: Az Dirençli (Dikkatli Damızlık)
    "AHQ/AHQ": {"group": "R3", "score": 4.0, "description": "Az dirençli, damızlıkta dikkatli davranılmalı.", "color": "#FFFF00"}, # Sarı
    "AHQ/ARH": {"group": "R3", "score": 4.5, "description": "Az dirençli, damızlıkta dikkatli davranılmalı.", "color": "#FFFF00"}, 
    "AHQ/ARQ": {"group": "R3", "score": 5.0, "description": "Az dirençli, damızlıkta dikkatli davranılmalı.", "color": "#FFFF00"}, 
    "ARH/ARH": {"group": "R3", "score": 5.5, "description": "Az dirençli, damızlıkta dikkatli davranılmalı.", "color": "#FFFF00"},
    "ARH/ARQ": {"group": "R3", "score": 6.0, "description": "Az dirençli, damızlıkta dikkatli davranılmalı.", "color": "#FFFF00"},
    "ARQ/ARQ": {"group": "R3", "score": 6.5, "description": "Az dirençli, damızlıkta dikkatli davranılmalı.", "color": "#FFFF00"},
    
    # R4: Duyarlı (Eleme Adayı)
    "AHQ/VRQ": {"group": "R4", "score": 8.0, "description": "Scrapie'ye duyarlı, eleme adayı.", "color": "#FFA500"}, # Turuncu
    "ARH/VRQ": {"group": "R4", "score": 8.5, "description": "Scrapie'ye duyarlı, eleme adayı.", "color": "#FFA500"}, 
    "ARQ/VRQ": {"group": "R4", "score": 9.0, "description": "Scrapie'ye duyarlı, eleme adayı.", "color": "#FFA500"}, 

    # R5: En Duyarlı (Eleme Grubu)
    "VRQ/VRQ": {"group": "R5", "score": 10.0, "description": "Scrapie’ye en duyarlı koyunlardır, hemen eleme gereklidir.", "color": "#FF0000"} # Kırmızı
}

# ---------------------------
# Veri Yapıları
# ---------------------------

# Genotiplerin ırklara göre Türkiye'deki yaklaşık frekansları (Örnek Data)
GENOTYPE_FREQUENCIES_DATA = {
    'Genotip': list(NSP_RISK_MAPPING.keys()),
    'Kıvırcık (%)': [random.uniform(0.5, 5) if g != "VRQ/VRQ" else random.uniform(0.01, 0.5) for g in NSP_RISK_MAPPING.keys()],
    'Sakız (%)': [random.uniform(1.0, 8) if g.startswith("ARR") else random.uniform(0.1, 3) for g in NSP_RISK_MAPPING.keys()],
    'Dağlıç (%)': [random.uniform(2.0, 10) if g.endswith("ARQ") else random.uniform(0.5, 5) for g in NSP_RISK_MAPPING.keys()],
    'Karaman (%)': [random.uniform(5.0, 15) if g.endswith("ARQ") else random.uniform(0.1, 5) for g in NSP_RISK_MAPPING.keys()]
}
# DataFrame oluştur
df_genotype_freq = pd.DataFrame(GENOTYPE_FREQUENCIES_DATA).set_index('Genotip')


# ---------------------------
# Streamlit Arayüzü
# ---------------------------

st.title("🔬 Scrapie Genetik Analiz Modülü")
st.markdown("---")

st.sidebar.header("Genetik Analiz Parametreleri")

# 1. Genotip Seçimi (Kullanıcı girdisi)
selected_genotype = st.sidebar.selectbox(
    "1. Koyun Genotipini Seçin (PrP Kodon 136, 154, 171)",
    options=list(NSP_RISK_MAPPING.keys()),
    index=list(NSP_RISK_MAPPING.keys()).index("ARQ/ARQ")
)

# Seçilen genotipe ait risk bilgileri
risk_info = NSP_RISK_MAPPING[selected_genotype]
risk_group = risk_info["group"]
risk_score = risk_info["score"]
risk_description = risk_info["description"]
risk_color = risk_info["color"]


# ---------------------------
# Sonuç ve Özet Kartları
# ---------------------------
st.markdown("### Sonuç Özeti")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="NSP Risk Grubu", 
        value=risk_group, 
        delta=f"Risk Skoru: {risk_score}", 
        delta_color="off"
    )
    
with col2:
    # Bu metrik için renkli HTML kutusu oluştur
    color_html = f"""
    <div style="background-color: {risk_color}; color: black; padding: 10px; border-radius: 8px; text-align: center; font-size: 1.1em; font-weight: bold;">
        {selected_genotype}
    </div>
    """
    st.markdown("PrP Genotipi", unsafe_allow_html=True)
    st.markdown(color_html, unsafe_allow_html=True)

with col3:
    st.info(f"**Açıklama:** {risk_description}")


st.markdown("---")

# ---------------------------
# Risk Faktörleri Tablosu
# ---------------------------
st.markdown("### 2. Genotip Bazlı Risk Faktörleri")
risk_factors_data = {
    "Risk Faktörü": ["Direnç Derecesi", "136. Kodon (Alanin/Valin)", "154. Kodon (Histidin/Arjinin)", "171. Kodon (Glutamin/Arjinin)"],
    "Değer": [
        risk_group, 
        # FIX: Allele stringleri (ARQ) 3 karakterli olduğu için indeksler 0, 1, 2 olmalıdır.
        # Daha önceki [1], [2], [3] indekslemeleri 'IndexError' hatasına yol açıyordu.
        selected_genotype.split('/')[0][0] + "/" + selected_genotype.split('/')[1][0], # Kodon 136 (Index 0)
        selected_genotype.split('/')[0][1] + "/" + selected_genotype.split('/')[1][1], # Kodon 154 (Index 1)
        selected_genotype.split('/')[0][2] + "/" + selected_genotype.split('/')[1][2]  # Kodon 171 (Index 2)
    ]
}
df_risk_factors = pd.DataFrame(risk_factors_data)

# 'use_container_width=True' yerine 'width='stretch'' kullanıldı.
st.dataframe(df_risk_factors, hide_index=True, width='stretch') 

st.markdown("---")

# ---------------------------
# Türkiye Haritası üzerinde Risk Görselleştirme
# ---------------------------
st.markdown("### 3. Türkiye Bölgesel Risk Potansiyeli (Örnek Görselleştirme)")
st.caption("Genotipinizin potansiyel riskini göstermek için harita bölgeleri dinamik olarak güncellenir.")

# Harita Merkezi: Türkiye (Ankara civarı)
m = folium.Map(location=[39.9334, 32.8597], zoom_start=5, control_scale=True)

# Seçilen genotipe göre harita verilerini dinamik olarak güncelle
# VRQ/VRQ ise tüm bölgelerin riskini artır, ARR/ARR ise riskini azalt.
for feature in TURKEY_SAMPLE_GEOJSON['features']:
    initial_risk = feature['properties']['risk']
    
    # Risk Puanına göre renk faktörünü ayarla (Örnek dinamik etki)
    if risk_group == "R1": # En dirençli
        adjusted_risk = max(0.1, initial_risk - 0.25)
    elif risk_group == "R5": # En duyarlı
        adjusted_risk = min(0.9, initial_risk + 0.25)
    else:
        adjusted_risk = initial_risk # Diğerleri ortalama

    feature['properties']['adjusted_risk'] = adjusted_risk

# GeoJSON katmanını haritaya ekle
folium.GeoJson(
    TURKEY_SAMPLE_GEOJSON,
    name='Risk Bölgeleri',
    style_function=lambda feature: {
        'fillColor': 'red' if feature['properties']['adjusted_risk'] > 0.7 else 
                     'orange' if feature['properties']['adjusted_risk'] > 0.5 else 
                     'yellow' if feature['properties']['adjusted_risk'] > 0.3 else 
                     'green',
        'color': 'black',
        'weight': 1,
        'fillOpacity': feature['properties']['adjusted_risk'] 
    },
    tooltip=folium.GeoJsonTooltip(
        fields=['name', 'region', 'adjusted_risk'],
        aliases=['İl/Bölge:', 'Irk Bölgesi:', 'Tahmini Risk Skoru:'],
        localize=True,
        labels=True,
        sticky=False
    )
).add_to(m)

# Haritayı Streamlit'e göm
# 'use_container_width=True' yerine 'width='stretch'' kullanıldı.
st_folium(m, height=450, width='stretch')


st.markdown("---")

# ---------------------------
# Irk Frekansları Tablosu
# ---------------------------
st.markdown("### 4. Türkiye Irklarında Genotip Frekans Dağılımı")
st.caption(f"Seçilen genotip **{selected_genotype}**'nin ana ırklardaki tahmini bulunma frekansları (%)")

# Seçilen genotipi vurgula
df_freq_to_display = df_genotype_freq.loc[[selected_genotype]]

# 'use_container_width=True' yerine 'width='stretch'' kullanıldı.
st.dataframe(
    df_freq_to_display.style.highlight_max(axis=1, color='lightgreen'), 
    width='stretch'
)

st.markdown("""
<div style="font-size: 0.8em; color: gray;">
    Not: Tablodaki yüzdeler, genotipin o ırk içindeki yaklaşık bulunma sıklığını temsil eden verilerdir.
</div>
""", unsafe_allow_html=True)
