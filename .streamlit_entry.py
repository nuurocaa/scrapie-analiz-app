import streamlit as st

# Yeni satır: Bu sayfanın adını menüde gizler
st.set_page_config(page_title="Ana Sayfa", layout="wide")
st.title("Scrapie Genetik Risk Analizi Uygulaması")
st.markdown("---")
st.markdown("""
**Hoş Geldiniz!**
Lütfen sol menüden **Scrapie Hakkında Genel Bilgiler**, **Scrapie Risk Skoru Hesaplama** veya **Örnek Çalışmalar** seçeneklerinden uygun olanı tıklayınız.
""")
