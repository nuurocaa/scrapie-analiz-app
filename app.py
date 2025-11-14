import streamlit as st

st.set_page_config(page_title="Ana Sayfa", layout="wide")

# LOGO: st.image komutu ile harici linki kesin olarak yüklüyoruz.
# Bu, HTML/Markdown kullanmaktan daha güvenilirdir.
st.image("https://raw.githubusercontent.com/nuurocaa/scrapie-analiz-app/main/au_logo_v2.png", width=100)

# BAŞLIK BÖLÜMÜ (Artık logo burada değil, sadece metin var)
st.markdown(
"""
<div style="display: flex; align-items: center;">
    <div>
        <h1 style="margin: 0; font-size: 2.5em;">Scrapie Genetik Risk Analizi Uygulaması</h1>
        <p style="margin: 0; font-size: 1.2em;">Ankara Üniversitesi Ziraat Fakültesi Zootekni Bölümü Biyometri ve Genetik Anabilim Dalı</p>
    </div>
</div>
<hr>
""",
unsafe_allow_html=True
)

st.markdown("""
**Hoş Geldiniz!**
Lütfen sol menüden **Risk Skoru Hesaplaması** seçeneğine tıklayarak analize başlayınız.
""")

# Menüdeki "app" veya "Ana Sayfa" başlığını gizlemek için kesin CSS
st.markdown(
"""
<style>
/* Varsayılan ana sayfa başlığını tamamen gizler */
li[data-testid="stSidebarNavListItem"]:nth-child(1) {
    display: none;
}
section[data-testid="stSidebar"] div[data-testid="stStatusWidget"] button[kind="secondary"] {
    visibility: hidden;
}
</style>
""",
unsafe_allow_html=True
)
