import WORLDNEWS
import NDTV
import abp
import streamlit as st
PAGES = {
    "WORLD NEWS": WORLDNEWS,
    "NDTV": NDTV,
    "ABP NEWS": abp
}
st.sidebar.title('MENU')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
