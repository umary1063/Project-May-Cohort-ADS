import streamlit as st
import pandas as pd
import numpy as np
import xlrd as x


def app():
    st.title('Bogoro LGA')
    # ### Importing data

    # In[3]:
    melt=pd.read_excel('melt.xls')
    melt.set_index("Ward", inplace=True)

    #st.header("Bogoro LGA--Service and Data Gap Analysis July - September 2021")
    st.write("This page display both service & data gap analysis for Bogoro LGA Main PHCs + GH, kindly scroll-down to review by facility ")


    # ### Filtring by Facility

    # In[4]:
    st.subheader("Bogoro General Hospital")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Bogoro General Hospital'
    hf1 = melt.loc[filt]
    st.dataframe(hf1)

    # In[5]:
    st.subheader("Boi PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Boi Primary Health Centre'
    hf2 = melt.loc[filt]
    st.dataframe(hf2)


    # In[6]:
    st.subheader("Datsang PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Datsang Primary Health Care Centre'
    hf3 = melt.loc[filt]
    st.dataframe(hf3)


    # In[7]:
    st.subheader("Dutsen Lawan PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Dutsen Lawan Health Care Centre'
    hf4 = melt.loc[filt]
    st.dataframe(hf4)


    # In[8]:
    st.header("Gambar PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Gambar Primary  Health Centre'
    hf5 = melt.loc[filt]
    st.dataframe(hf5)

    # In[9]:
    st.subheader("Bugun PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Bugun Primary Health Care Centre'
    hf6 = melt.loc[filt]
    st.dataframe(hf6)

    # In[10]:
    st.subheader("Gobbiya MPHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Gobbiya Model Primary Health Care'
    hf7 = melt.loc[filt]
    st.dataframe(hf7)


    # In[11]:
    st.subheader("Gyara PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Gyara Primary Health Care Centre'
    hf8 = melt.loc[filt]
    st.dataframe(hf8)


    # In[12]:
    st.subheader("Kurum PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Kurum Primary Health Centre'
    hf9 = melt.loc[filt]
    st.dataframe(hf9)


    # In[13]:
    st.subheader("Lusa PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Lusa Primary Health Care Centre'
    hf10 = melt.loc[filt]
    st.dataframe(hf10)

    # In[14]:
    st.subheader("Mwari PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Mwari Primary Health Care Centre'
    hf11 = melt.loc[filt]
    st.dataframe(hf11)

    # In[15]:
    st.subheader("Tadnum PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Tadnum Primary Health Care Centre'
    hf12 = melt.loc[filt]
    st.dataframe(hf12)


    # In[16]:
    st.subheader("Unguwan Rimi PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Unguwan Rimi Primary Health Care Centre'
    hf13 = melt.loc[filt]
    st.dataframe(hf13)


    # In[17]:
    st.subheader("Lafiyan Sara PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Lafiyan Sara Primary Health Care Centre'
    hf14 = melt.loc[filt]
    st.dataframe(hf14)
