import streamlit as st
import requests
import pandas
from bs4 import BeautifulSoup
def app():
    st.title('WORLD NEWS')
    st.write('Top head lines of WORLD NEWS')
    def get_url():
        domain='https://www.ndtv.com/world-news'
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
        for a in around[1:]:
            dets = {}
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
        if st.button('Download'):
            df.to_csv('WORLDNEW_DATA.csv')
    world_news()