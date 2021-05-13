import WORLDNEWS
import COVID
import NDTV
import Criptocurrency
import streamlit as st
PAGES = {
    "WORLD NEWS": WORLDNEWS,
    "COVID-19": COVID,
    "NDTV": NDTV,
    "CRIPTO CURRENCY DETAILS": Criptocurrency
}
st.sidebar.title('MENU')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
