import streamlit as st

st.set_page_config(page_title="Ana Sayfa", layout="wide")

# 1. Logoyu st.image ile yükle ve başlıkları HTML ile yanına al
# Bu yöntem, logo yüklemede en güvenilir yoldur.
st.image("static/au_logo.png", width=100, use_column_width="always", output_format="PNG")

st.markdown(
    """
    <div style="margin-top: -100px; margin-left: 120px;">
        <h1 style="margin: 0; font-size: 2.5em;">Scrapie Genetik Risk Analizi Uygulaması</h1>
        <p style="margin: 0; font-size: 1.2em;">Ankara Üniversitesi Ziraat Fakültesi Zootekni Bölümü Biyometri ve Genetik Anabilim Dalı</p>
    </div>
    <hr>
    """,
    unsafe_allow_html=True
)

st.markdown("""
**Hoş Geldiniz!**
Lütfen sol menüden **Risk Skoru Hesaplaması** seçeneğine tıklayarak analize başlayınız.
""")

# 2. Menüdeki "app" başlığını gizlemek için CSS (en kesin yöntem)
st.markdown(
"""
<style>
/* Varsayılan ana sayfa başlığını tamamen gizler (genellikle ilk öğe) */
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
