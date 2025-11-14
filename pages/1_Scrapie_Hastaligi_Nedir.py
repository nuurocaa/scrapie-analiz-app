import streamlit as st

st.set_page_config(layout="wide")
st.title("Scrapie ve Genetik Analiz Hakkında")

st.markdown("""
### 1. Scrapie Hastalığına Giriş

Scrapie, **koyun ve keçilerde** görülen, fatal (ölümcül) ve dejeneratif bir prion hastalığıdır. Hastalık, beynin normal hücre proteinlerinin (PrPC) yanlış katlanması sonucu anormal, bulaşıcı prion proteinlerine (PrPSc) dönüşmesiyle karakterizedir. Bu prionlar sinir dokularında birikerek nörolojik semptomlara yol açar.

Bu hastalık 250 yıldan fazla bir zamandır bilinen (ilk defa 1732 yılında İngiltere’de farkına varılmıştır) TSE grubu bir hastalıktır (Poser 2002). Hastalığın sığırlarda ortaya çıkan formu, halk arasında deli dana hastalığı olarak bilinen BSE (Bovine spongiform encephalopathy) ise ilk defa 1986 yılında İngiltere’de görülmüştür. BSE’nin ortaya çıkışıyla ilgili en önemli hipotez, BSE’nin koyunlarda görülen scrapie hastalığından köken almış olabileceğidir. Koyun ve keçi artıkları ile kadavralarının hayvan yemi üretiminde kullanılması, BSE’nin koyunlardan sığırlara bulaştığı görüşünü destekleyen önemli bir olgudur (Goldmann et al. 1994, Hunter 1997, Arnold et al. 2002, Sipos et al. 2002, Philippe et al. 2005, Molina et al. 2006, Hunter 2007, Martin et al. 2007, Ün et al. 2008). 

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
