import streamlit as st

st.set_page_config(page_title="Ana Sayfa", layout="wide") 
st.title("Scrapie Genetik Risk Analizi Uygulaması")
st.markdown("---")
st.markdown("""
**Hoş Geldiniz!**
Lütfen sol menüden **Scrapie Risk Skoru Hesaplama** seçeneğine tıklayarak analize başlayınız.
""")
# Menüdeki Ana Sayfa başlığını gizlemek için stil ekleniyor
st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] div[data-testid="stStatusWidget"] button[kind="secondary"] {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
