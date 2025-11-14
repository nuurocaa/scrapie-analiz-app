import streamlit as st
# PIL kütüphanesi st.image tarafından otomatik olarak kullanıldığı için gereksiz import kaldırıldı.

st.set_page_config(page_title="Ana Sayfa", layout="wide")

# --- CSS STİLİ ---
st.markdown("""
<style>
/* Ana içeriğin kenar boşluğunu düzenleme */
.css-1d391kg {
    padding-top: 2rem;
}
/* Menüdeki "Ana Sayfa" başlığını gizler */
li[data-testid="stSidebarNavListItem"]:nth-child(1) {
    display: none;
}
/* Streamlit'in varsayılan durum widget'ını (logoda hata gösteren) gizler */
section[data-testid="stSidebar"] div[data-testid="stStatusWidget"] button[kind="secondary"] {
    visibility: hidden;
}

/* Ana başlık stili */
.main-title {
    font-size: 2.8em;
    font-weight: 700;
    color: #1a5276; /* Koyu Mavi */
    margin-bottom: 0;
}
.subtitle {
    font-size: 1.2em;
    color: #5d6d7e;
    margin-top: 0;
}
</style>
""", unsafe_allow_html=True)

# --- HEADER BÖLÜMÜ (LOGO ve BAŞLIK) ---
col1, col2 = st.columns([1, 6])

# Logo yolu: son onaylanan yerel yol
with col1:
    try:
        # Streamlit'in yerel olarak dosya okuma yöntemi kullanılıyor.
        st.image("static/au_logo_v2.png", width=100)
    except FileNotFoundError:
        st.warning("Logo dosyası (static/au_logo_v2.png) bulunamadı.")

with col2:
    st.markdown('<p class="main-title">Scrapie Genetik Risk Analizi Uygulaması</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Ankara Üniversitesi Ziraat Fakültesi Zootekni Bölümü Biyometri ve Genetik Anabilim Dalı</p>', unsafe_allow_html=True)

st.divider()

# --- UYGULAMA BİLGİ VE GİRİŞ BÖLÜMÜ ---
st.container(border=True)
st.subheader("Uygulama Amacı ve Kapsamı")

col_info, col_cta = st.columns([3, 1])

with col_info:
    st.markdown("""
    Bu uygulama, küçükbaş hayvanlarda (koyun/keçi) görülen ve ölümcül seyreden **Scrapie (prion) hastalığına** karşı genetik risk seviyesini bilimsel veriler ışığında hesaplamak üzere tasarlanmıştır.

    Analiz, hastalığa karşı direnç ve hassasiyet ile ilişkilendirilen kritik **PRNP geni polimorfizmlerine** (özellikle kodon 136, 154 ve 171) dayanmaktadır. Amacımız, genotip verilerini kullanarak sürüleriniz için şeffaf ve anlaşılır bir risk skoru sağlamaktır.
    """)

with col_cta:
    st.markdown("---")
    # Kullanıcıyı direkt risk hesaplama sayfasına yönlendiren CTA (Call to Action)
    st.markdown("**Hemen analize başlayın!**")
    # Streamlit Cloud'da yan sayfaya linkleme, ancak doğrudan yönlendirme butonları Streamlit'in çoklu sayfa mimarisinde çalışmadığı için, menüyü işaret ediyoruz.
    st.success("⬅️ Sol menüden **Risk Skoru Hesaplaması** sayfasını seçiniz.")
    st.markdown("---")


# --- EK BİLGİ VE FOOTER ---
st.markdown("##") # Boşluk bırakmak için
st.info("Lütfen her analize başlamadan önce sol menüdeki **Scrapie Hastalığı Nedir** sayfasını inceleyerek genetik temeller hakkında bilgi edininiz.")

st.markdown("""
<div style="text-align: center; margin-top: 30px; padding: 10px; border-top: 1px solid #eee;">
    <small>Bu proje, Ankara Üniversitesi Zootekni Bölümü'nün bilimsel araştırmaları kapsamında geliştirilmiştir.</small>
</div>
""", unsafe_allow_html=True)
