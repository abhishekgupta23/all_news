import streamlit as st
import requests
import pandas
import base64
from bs4 import BeautifulSoup
def app():
    st.title('COVID-19 UPDATES')
    st.write('covid-19 cases analysis through out india')
    def get_url():
        domain='https://news.google.com/covid19/map?hl=en-IN&mid=%2Fm%2F03rk0&gl=IN&ceid=IN%3Aen'
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
        

    def s(n,b):
        for j in b[0:n]:
            x=j
        return x
    def l(f,p):
        for j in p[0:f]:
            x=j
        return x
    def n(f,q):
        for j in q[0:f]:
            x=j
        return x
    
    def world_news():
        soup=None 
        try:
            data=fetchdata(get_url())
            if data.status_code==200:
                soup=parseData(data.text)
        except Exception as e:
            print(e)
        rows = soup.find_all('div', attrs={ 'class' : 'pcAJd' })
        row = soup.find_all('td',attrs={'class':'l3HOY'})
        a=[]
        for d in row[10:]:
            details = {}
            details =d.text
            a.append(details)
        b=[]
        for i in a[::5]:
            f={}
            f=i
            b.append(f)
        p=[]
        for t in a[1::5]:
            w={}
            w=t
            p.append(w)
        q=[]
        for m in a[4::5]:
            v={}
            v=m
            q.append(v)
        covid_data=[]
        k=1
        for r in rows[2:]:
            data={}
            z=s(k,b)
            y=l(k,p)
            o=n(k,q)
            k=k+1
            data['States'] =r.text
            data['Total cases']=z
            data['New cases (1 day*)'] = y
            data['deaths'] = o
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
            href = f'<a href="data:file/csv;base64,{b64}" download = "COVID Data.csv">Download csv file</a>'
            return href
        
        st.write("To Download the above data click below button:-")
        if st.button('Download'):
            st.markdown(get_table_download_link(df),unsafe_allow_html=True)
    world_news()
