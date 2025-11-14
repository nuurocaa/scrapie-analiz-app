import streamlit as st

st.set_page_config(layout="wide")
st.title("Scrapie ve Genetik Analiz Hakkında")

st.markdown("""
### 1. Scrapie Hastalığına Giriş

Scrapie, **keçilerde** görülen, fatal (ölümcül) ve dejeneratif bir prion hastalığıdır. Hastalık, beynin normal hücre proteinlerinin (PrPC) yanlış katlanması sonucu anormal, bulaşıcı prion proteinlerine (PrPSc) dönüşmesiyle karakterizedir. Bu prionlar sinir dokularında birikerek nörolojik semptomlara yol açar.

Hastalık, sinir sistemini etkileyerek hayvanlarda kaşıntı (scrapie ismini buradan alır), titreme, koordinasyon bozukluğu ve sonunda ölüme neden olur.

### 2. PRNP Geni ve Genetik Direnç

Scrapie'ye karşı direnç ve hassasiyet, ağırlıklı olarak **PRNP (Prion Protein) geni** üzerinde bulunan polimorfizmler ile yakından ilişkilidir. Genotip analizi, sürülerdeki risk seviyesini belirlemede kritik rol oynar.

Hastalığa karşı direnç ve hassasiyet, özellikle aşağıdaki üç kritik kodondaki (amino asit pozisyonu) varyasyonlarla belirlenir:

| Kodon | Hassasiyet (Riskli) | Direnç (Korumalı) | Açıklama |
|---|---|---|---|
| **136** | Valin (V) | Alanin (A) | Önemli bir hassasiyet belirleyicisidir. |
| **154** | Histidin (H) | Arjinin (R) | Direnç mekanizmasında rol oynar. |
| **171** | Glutamin (Q) | Arjinin (R) | Koyunlarda en güçlü direnç belirleyicisidir. |

Uygulamamız, genotip verilerinizi bu kodonlardaki varyasyonlara göre analiz ederek sürünüzün genetik risk skorunu hesaplar.
""")
