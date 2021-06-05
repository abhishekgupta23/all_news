import WORLDNEWS
import NDTV
import streamlit as st
PAGES = {
    "WORLD NEWS": WORLDNEWS,
    "NDTV": NDTV
}
st.sidebar.title('MENU')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
