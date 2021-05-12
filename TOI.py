import streamlit as st
import requests
import pandas
from bs4 import BeautifulSoup
def app():
    st.title('TIMES OF INDIA')
    st.write('Top 10 head lines of TOI')
    def get_url1():
        domain='https://timesofindia.indiatimes.com/'
    
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
            data=fetchdata(get_url1())
            if data.status_code==200:
                soup=parseData(data.text)
        except Exception as e:
            print(e)
        around=soup.find_all('figcaption')
        image=soup.find_all('div',attrs={'class':'_1vDEx cardactive'})
        link=soup.find_all('figure',attrs={'class':'_1Fkp2   '})
        d=[]
        img=[]
        for i in image:
            img.append(i.find('img').get('src'))
        c=0
        for a in around:
            dets = {}
            st.image(img[c])
            dets['heading']=a.text

            st.write(a.text)
            d.append(dets)
            c+=1
            df=pandas.DataFrame(d)
        st.table(df)
        if st.button('Download'):
            df.to_csv('TIMES OF INDIA.csv')
    world_news()