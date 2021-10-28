import streamlit as st
import pandas as pd
import numpy as np
import xlrd as x
def app():

    st.title('Kirfi LGA')

    # In[3]:
    melt=pd.read_excel('melt.xls')
    melt.set_index("Ward", inplace=True)

    #st.header("Kirfi LGA--Service and Data Gap Analysis July - September 2021")
    st.write("This page display both service & data gap analysis for Kirfi LGA Main PHCs + GH, kindly scroll-down to review by facility ")



    #creating a filter which is similar to a groupby
    st.subheader("Baba PHC")
    filt = melt['Facility Name']== ' Baba Primary Health Centre'
    hf1 = melt.loc[filt]
    st.dataframe(hf1)


    # In[5]:
    st.subheader("")
    #creating a filter which is similar to a groupby
    st.subheader("Badara PHC")
    filt = melt['Facility Name']== ' Badara Primary Health Centre'
    hf2 = melt.loc[filt]
    st.dataframe(hf2)


    # In[6]:
    st.subheader("Bara PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Bara Primary Health Centre'
    hf3 = melt.loc[filt]
    st.dataframe(hf3)


    # In[17]:
    st.subheader("Beni PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Beni Primary Health Centre'
    hf14 = melt.loc[filt]
    st.dataframe(hf14)



    # In[7]:
    st.subheader("Dewu PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Dewu Primary Health Centre'
    hf4 = melt.loc[filt]
    st.dataframe(hf4)


    # In[8]:
    st.subheader("Guyaba PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Guyaba Primary Health Centre'
    hf5 = melt.loc[filt]
    st.dataframe(hf5)


    # In[9]:
    st.subheader("Kafin-Iya PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Kafin-Iya Primary Health Centre'
    hf6 = melt.loc[filt]
    st.dataframe(hf6)


    # In[10]:

    st.subheader("Kirfi General Hospital")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Kirfi General Hospital'
    hf7 = melt.loc[filt]
    st.dataframe(hf7)



    # In[11]:
    st.header("kirfi Town PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Kirfi Town Primary Health Centre'
    hf8 = melt.loc[filt]
    st.dataframe(hf8)


    # In[12]:
    st.header("Kwagal PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Kwagal Primary Health Centre'
    hf9 = melt.loc[filt]
    st.dataframe(hf9)


    # In[13]:
    st.subheader("Lariski PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Lariski Primary Health Centre'
    hf10 = melt.loc[filt]
    st.dataframe(hf10)

    # In[14]:
    st.subheader("Shango PHc")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Shango Health Clinic'
    hf11 = melt.loc[filt]
    st.dataframe(hf11)


    # In[15]:
    st.subheader("Tubule PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Tubule Primary Health Centre'
    hf12 = melt.loc[filt]
    st.dataframe(hf12)


    # In[16]:
    st.subheader("Wanka PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Wanka Primary Health Centre'
    hf13 = melt.loc[filt]
    st.dataframe(hf13)


