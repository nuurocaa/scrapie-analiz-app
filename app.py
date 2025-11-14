import streamlit as st

st.set_page_config(page_title="Ana Sayfa", layout="wide")

# Logo ve başlık için HTML kullanıyoruz
st.markdown( # <-- Bu parantez burada açılmalı
    """
    <div style="display: flex; align-items: center;">        <img src="au_logo.png"
             alt="Ankara Üniversitesi Logosu"
             style="height: 100px; margin-right: 20px;">
        <div>
            <h1 style="margin: 0; font-size: 2.5em;">Scrapie Genetik Risk Analizi Uygulaması</h1>
            <p style="margin: 0; font-size: 1.2em;">Ankara Üniversitesi Ziraat Fakültesi Zootekni Bölümü Biyometri ve Genetik Anabilim Dalı</p>
        </div>
    </div>
    <hr>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] div[data-testid="stStatusWidget"] button[kind="secondary"] {
        visibility: hidden;
    }
    </style>
    """, # <-- BU VİRGÜL VE YENİDEN """ KAPANMASI GEREKİR
    unsafe_allow_html=True
)

# Menüdeki Ana Sayfa başlığını gizlemek için stil ekleniyor
st.markdown(
    """
    <style>
    section[data-testid="stSidebar"] div[data-testid="stStatusWidget"] button[kind="secondary"] {
        visibility: hidden;
    }
    /* BURASI DÜZELTİLDİ: CSS bloğu kapatıldı */
    </style>
    """,
    unsafe_allow_html=True,
)
             alt="Ankara Üniversitesi Logosu" 
             style="height: 100px; margin-right: 20px;">
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
