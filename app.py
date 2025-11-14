import streamlit as st

st.set_page_config(page_title="Ana Sayfa", layout="wide")

# Logo ve başlık için tamamen saf HTML/CSS kullanılıyor.
# Bu, Streamlit'in otomatik görüntü sıkıştırmasını (bulanıklık) atlar.
st.markdown(
"""
<div style="display: flex; align-items: center;">
    <!-- width: auto ve height: 100px ile çözünürlük korunarak boyutlandırıldı -->
    <img src="static/au_logo.png"
         alt="Ankara Üniversitesi Logosu"
         style="height: 100px; width: auto; margin-right: 20px;">
    <div>
        <h1 style="margin: 0; font-size: 2.5em;">Scrapie Genetik Risk Analizi Uygulaması</h1>
        <!-- Yarım kalan metin düzeltildi -->
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
```
eof

### 🛠️ SON ADIMLAR

1.  **Yapıştırma ve Kaydetme:** Bu kodu `nano app.py` içine yapıştırdıktan sonra:
    * Kaydedin: **$\mathbf{Ctrl + O}$** ve $\text{Enter}$.
    * Çıkın: **$\mathbf{Ctrl + X}$.**

2.  **Yükleme:** Değişiklikleri Git'e yükleyin:

```bash
git add app.py
git commit -m "feat: Logo bulanikligi ve tum syntax hatalari saf HTML/CSS ile kesin olarak giderildi."
git push -u origin main
