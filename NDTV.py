import streamlit as st
import requests
import pandas
import base64
from bs4 import BeautifulSoup
def app():
    st.title('NDTV NEWS')
    st.write('TOP HEAD LINES ARE')
    def get_url():
        domain='https://www.ndtv.com/latest'
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
        around=soup.find_all('div',attrs={'class':'news_Itm-cont'})
        image=soup.find_all('div',attrs={'class':'news_Itm-img'})
        d=[]
        img=[]
        for i in image:
            img.append(i.find('img').get('src'))
        c=0
        for a in around:
            dets={}
            st.image(img[c])
            dets['heading']=a.find('h2',{'class':'newsHdng'}).find('a').text
            dets['content']=a.find('p',attrs={'class':'newsCont'}).text
            dets['posted by']=a.find('span',attrs={'class':'posted-by'}).text
            st.write(a.find('h2',{'class':'newsHdng'}).find('a').text)
            st.write(a.find('p',attrs={'class':'newsCont'}).text)
            st.write(a.find('span',attrs={'class':'posted-by'}).text)
            c+=1
            d.append(dets)
        df=pandas.DataFrame(d)
        st.table(df)
        def get_table_download_link(df):
            """Generates a link allowing the data in a given panda dataframe to be downloaded
            in:  dataframe
            out: href string
            """
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/csv;base64,{b64}" download = "NDTV Data.csv">Download csv file</a>'
            return href
        if st.button('Download'):
            st.markdown(get_table_download_link(df),unsafe_allow_html=True)
        
    world_news()
