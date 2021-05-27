import streamlit as st
from cowin_api import CoWinAPI
import pandas as pd
def app ():
    cowin = CoWinAPI()
    st.title("Slot availability")
    choice1 = ['By Pincode','District Code','By district']
    select = st.selectbox(options=choice1, label="Choose Option")
    if select == choice1[0]:
        pin_code = st.text_input("Enter pin code")
        date = st.date_input("Enter date")
        btn = st.button("FIND")
        if btn:
            available_centers = cowin.get_availability_by_pincode(pin_code, date)
            st.write("All Available Centers [ By Pincode ] : ")
            st.table(available_centers)
    if select == choice1[1]:
        states = cowin.get_states()
        st.write("All States List : ")
        st.table(states)
    if select == choice1[2]:
        st.write("To Know the state code check the above option in dropdown")
        state_id = st.text_input("Enter state id")
        btn1 = st.button("Find Code")
        if btn1:
            districts = cowin.get_districts(state_id)
            st.write("District code :-")
            st.table(districts)
        district_id = st.text_input("Enter District id ")
        date = st.date_input("Enter date")
        btn = st.button("FIND")
        if btn:
            available_centers = cowin.get_availability_by_district(district_id, date)
            st.write("All Available Centers [ By district ] : ")
            st.table(available_centers)
