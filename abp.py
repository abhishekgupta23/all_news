import streamlit as st
import requests
import pandas
import base64
from bs4 import BeautifulSoup
def app():
    st.title('ABP NEWS')
    st.write('TOP HEAD LINES ARE')
    def get_url():
        domain='https://www.abplive.com/news'
        return domain
    def fetchdata(url):
        try:
            data=requests.get(url)
            return data
        except Exception as e:
            print("some error")
            print(e)
    def parseData(text):
        try:
            soup=BeautifulSoup(text,features='html.parser')
            return soup
        except Exception as e:
            print('error while parsing')
            print(e)
    def world_news():
        soup=None 
        try:
            data=fetchdata(get_url())
            if data.status_code==200:
                soup=parseData(data.text)
        except Exception as e:
            print(e)
        around=soup.find_all('div',attrs={'class':'other_news'})
        image=soup.find_all('div',attrs={'class':'img4x3'})
        d=[]
        img=[]
        for i in image[4:]:
            img.append(i.find('img').get('data-src'))
        c=0
        for a in around[:19]:
            dets={}
            st.image(img[c])
            dets['heading']=a.text
            dets['link']=a.find('a').get('href')
            st.write(a.text)
            st.write(a.find('a').get('href'))
            c+=1
            d.append(dets)
        df=pandas.DataFrame(d)
        def get_table_download_link(df):
            """Generates a link allowing the data in a given panda dataframe to be downloaded
            in:  dataframe
            out: href string
            """
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/csv;base64,{b64}" download = "NDTV Data.csv">Download csv file</a>'
            return href
        st.write("  ")
        st.write("  ")
        st.write("To Download the above data click below button :-")
        if st.button('Download'):
            st.markdown(get_table_download_link(df),unsafe_allow_html=True)
        
    world_news()
