import WORLDNEWS
import COVID
import NDTV
import Criptocurrency
import main
import streamlit as st
PAGES = {
    "WORLD NEWS": WORLDNEWS,
    "COVID-19": COVID,
    "NDTV": NDTV,
    "CRYPTO CURRENCY DETAILS": Criptocurrency,
    "COVID SLOT AVAILABILITY": main
}
st.sidebar.title('MENU')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
