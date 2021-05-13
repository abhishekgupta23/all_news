import WORLDNEWS
import Criptocurrency
import COVID
import NDTV
import streamlit as st
PAGES = {
    "WORLD NEWS": WORLDNEWS,
    "CRIPTO CURRENCY DETAILS": Criptocurrency,
    "COVID-19": COVID,
    "NDTV": NDTV
}
st.sidebar.title('MENU')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
