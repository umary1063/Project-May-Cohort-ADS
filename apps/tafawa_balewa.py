
import streamlit as st
import pandas as pd
import numpy as np
import xlrd as x
def app():
    st.title('Tafawa Balewa LGA')
    # In[3]:
    melt=pd.read_excel('melt.xls')
    melt.set_index("Ward", inplace=True)

    #st.header("Tafawa Balewa LGA--Service and Data Gap Analysis July - September 2021")
    st.write("This page display both service & data gap analysis for Tafawa Balewa LGA Main PHCs + GH, kindly scroll-down to review by facility ")



    st.subheader("Bulan Gawo PHC")
    #creating a filter which is similar to a groupby

    filt = melt['Facility Name']== ' Bulan Gawo Maternal and Child Health'
    hf1 = melt.loc[filt]
    st.dataframe(hf1)


    # In[5]:

    st.subheader("Bununu Town PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Bununu Town Maternity'
    hf2 = melt.loc[filt]
    st.dataframe(hf2)


    # In[6]:
    st.subheader("Burga PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Burga Primary Health Centre'
    hf3 = melt.loc[filt]
    st.dataframe(hf3)


    # In[7]:
    st.subheader("Dajin PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Dajin Primary Health Centre'
    hf4 = melt.loc[filt]
    st.dataframe(hf4)


    # In[8]:
    st.subheader("Daranji PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Daranji Health Clinic'
    hf5 = melt.loc[filt]
    st.dataframe(hf5)



    # In[9]:
    st.subheader("Dul PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Dull Primary Health Centre'
    hf6 = melt.loc[filt]
    st.dataframe(hf6)


    # In[10]:
    st.subheader("Gital PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Gital Primary Healthc Centre'
    hf7 = melt.loc[filt]
    st.dataframe(hf7)


    # In[11]:
    st.subheader("Kardam PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Kardam Primary  Health Centre'
    hf8 = melt.loc[filt]
    st.dataframe(hf8)


    # In[12]:
    st.subheader("Lere PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Lere Primary Health Centre'
    hf9 = melt.loc[filt]
    st.dataframe(hf9)


    # In[13]:
    st.subheader("Lim PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Lim Primary Health Centre'
    hf10 = melt.loc[filt]
    st.dataframe(hf10)

    # In[14]:
    st.subheader("Maijuju PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Maijuju Tasha Health Clinic'
    hf11 = melt.loc[filt]
    st.dataframe(hf11)


    # In[15]:

    st.subheader("Mball")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Mball Health Clinic'
    hf12 = melt.loc[filt]
    st.dataframe(hf12)

    # In[16]:

    st.subheader("Sara PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Sara Primary Health Clinic'
    hf13 = melt.loc[filt]
    st.dataframe(hf13)

    # In[17]:

    st.subheader("T-Balewa Town PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Tafawa Balewa Town Primary Health Centre'
    hf14 = melt.loc[filt]
    st.dataframe(hf14)

    # In[18]:

    st.subheader("T-Balewa General Hospital")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Tafawa-Balewa General Hospital'
    hf15 = melt.loc[filt]
    st.dataframe((hf15))

    # In[19]:

    st.subheader("Tapshin PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Tapshin Model Primary Health Centre'
    hf16 = melt.loc[filt]
    st.dataframe(hf16)

    # In[20]:

    st.subheader("Zwall PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Zwall Health Clinic'
    hf17 = melt.loc[filt]
    st.dataframe(hf17)

    # In[21]:

