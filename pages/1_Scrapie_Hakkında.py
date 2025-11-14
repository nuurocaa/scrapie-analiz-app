import streamlit as st

st.set_page_config(layout="wide") 
st.title("🐑 Scrapie ve Genetik Analiz Hakkında")
st.header("1. Scrapie Hastalığına Giriş")
st.markdown("""
Scrapie, koyun ve keçilerde görülen ölümcül, dejeneratif bir prion hastalığıdır. 
Hastalığın genetik yatkınlığı, özellikle PRNP geni üzerindeki polimorfizmler ile yakından ilişkilidir.
""")
st.subheader("2. PRNP Geni ve Dirençlilik")
st.markdown("Hastalığa karşı direnç ve hassasiyet, kodon 136, 154 ve 171'deki varyasyonlarla belirlenir.")
# st.image("scrapie_gen.jpg") # İlgili bir genetik şema görseli eklenebilir.
