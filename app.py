import WORLDNEWS
import TOI
import COVID
import NDTV
import streamlit as st
PAGES = {
    "WORLD NEWS": WORLDNEWS,
    "TIMES OF INDIA": TOI,
    "COVID-19": COVID,
    "NDTV": NDTV
}
st.sidebar.title('MENU')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()