import streamlit as st
import requests
import pandas
import base64
from bs4 import BeautifulSoup
def app():
    st.title('CRYPTO CURRENCY DETAILS')
    st.write('Details related to CRYPTO CURRENCY')
    def get_url():
        domain='https://gadgets.ndtv.com/bitcoin-price-today-india-inr-usd-compare-koinex-zebpay-price-litecoin-iota'
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
    def u(n,p1):
        for j in p1[0:n]:
            x=j
        return x
    def l(f,q):
        for j in q[0:f]:
            x=j
        return x
    def n(f,r):
        for j in r[0:f]:
            x=j
        return x
    def h(f,c):
        for j in c[0:f]:
            x=j.text
        return x   
    def world_news():
        soup=None 
        try:
            data=fetchdata(get_url())
            if data.status_code==200:
                soup=parseData(data.text)
        except Exception as e:
            print(e)
        st.write(soup.find('h1').text)
        st.write(soup.find('h2').text)
        a=soup.find_all('div',attrs={'class':'_flx _cpnm'})
        b=soup.find_all('td',attrs={'class':'_lft'})
        c=soup.find_all('span',attrs={'class':'_rtxt'})
        d=[]
        for i in b:
            details = {}
            details =i.text
            d.append(details)
        p=[]
        for t in d[::3]:
            w={}
            w=t
            p.append(w)
        q=[]
        for m in d[1::3]:
            v={}
            v=m
            q.append(v)
        r=[]
        for s in d[2::3]:
            t={}
            t=s
            r.append(t)
        covid_data=[]
        k=1
        for j in a:
            data={}
            z=u(k,p)
            y=l(k,q)
            o=n(k,r)
            v=h(k,c)
            k=k+1
            data['coin name(code)'] =j.text
            data['price']=z
            data['Change (24h)'] = v
            data['Market Cap'] = y
            data['Volume (24h)'] = o
            covid_data.append(data)
        df = pandas.DataFrame(covid_data)
        
        st.table(df)
        def get_table_download_link(df):
            """Generates a link allowing the data in a given panda dataframe to be downloaded
            in:  dataframe
            out: href string
            """
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/csv;base64,{b64}" download = "Crypto Data.csv">Download csv file</a>'
            return href
        
        st.write("To Download the above data click below button :-")
        if st.button('Download'):
            st.markdown(get_table_download_link(df),unsafe_allow_html=True)
    world_news()
