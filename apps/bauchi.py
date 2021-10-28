import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title('Bauchi LGA')
    melt=pd.read_excel('melt.xls')
    melt.set_index("Ward", inplace=True)

    #st.header("Bauchi LGA--Service and Data Gap Analysis July - September 2021")
    st.write("This page display both service & data gap analysis for Bauchi LGA Main PHCs + GH, kindly scroll-down to review by facility ")

    # ### Filtering by Facility

    # In[4]:
    st.subheader("Bauchi Speclaist Hospital")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Bauchi Specialist Hospital'
    hf1 = melt.loc[filt]
    st.dataframe(hf1)


    # In[5]:
    st.subheader("Dandango PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Dandango Primary Health Care Centre'
    hf2 = melt.loc[filt]
    st.dataframe(hf2)


    # In[6]:
    st.subheader("Doya PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Doya Primary Health Care Centre'
    hf3 = melt.loc[filt]
    st.dataframe(hf3)


    # In[7]:
    st.subheader("Durum PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Durum Primary Health Center'
    hf4 = melt.loc[filt]
    st.dataframe(hf4)


    # In[8]:
    st.subheader("Gwaskwaram PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Gwaskwaram Primary Health Centre'
    hf5 = melt.loc[filt]
    st.dataframe(hf5)


    # In[9]:
    st.subheader("Jahun Under 5 PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Jahun Under Five Health Clinic'
    hf6 = melt.loc[filt]
    st.dataframe(hf6)


    # In[10]:
    st.subheader("Kangere PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Kangere Primary Health Care Centre'
    hf7 = melt.loc[filt]
    st.dataframe(hf7)


    # In[11]:
    st.subheader("Kobi PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Kobi Health Post'
    hf8 = melt.loc[filt]
    st.dataframe(hf8)


    # In[12]:
    st.subheader("Kofan Ran PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Kofan Ran Primary Health Centre'
    hf9 = melt.loc[filt]
    st.dataframe(hf9)


    # In[13]:
    st.subheader("Kofan Dumi PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Kofar Dumi Primary Health Care Centre'
    hf10 = melt.loc[filt]
    st.dataframe(hf10)


    # In[14]:
    st.subheader("Liman Katagum PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Liman Katagum Primary Health Care Centre'
    hf11 = melt.loc[filt]
    st.dataframe(hf11)


    # In[15]:
    st.subheader("luda PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Luda Primary Health Center'
    hf12 = melt.loc[filt]
    st.dataframe(hf12)


    # In[16]:
    st.subheader("Miri PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Miri Primary Health Center'
    hf13 = melt.loc[filt]
    st.dataframe(hf13)


    # In[17]:
    st.subheader("Nasarawa Jahun PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Nasarawa Jahun Primary Health Care Centre'
    hf14 = melt.loc[filt]
    st.dataframe(hf14)


    # In[18]:
    st.subheader("State-lowcost PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' State Low-Cost Primary Health Care Centre'
    hf15 = melt.loc[filt]
    st.dataframe(hf15)


    # In[24]:
    st.subheader("Tashan Babiye PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Tashan Babiye Primary Health Care Centre'
    hf21 = melt.loc[filt]
    st.dataframe(hf21)

    # In[19]:
    st.subheader("Tirwun PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Tirwun Primary Health Centre'
    hf16 = melt.loc[filt]
    st.dataframe(hf16)


    # In[20]:
    st.subheader("Tudn Gambo PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Tudun Gambo Primary Health Care Centre'
    hf17 = melt.loc[filt]
    st.dataframe(hf17)


    # In[21]:
    st.subheader("Yalwa PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Yalwa Domiciliary Maternal and Child Health Clinic'
    hf18 = melt.loc[filt]
    st.dataframe(hf18)


    # In[22]:
    st.subheader("Yuguda PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Yuguda Primary Health Care Centre'
    hf19 = melt.loc[filt]
    st.dataframe(hf19)


    # In[23]:
    st.subheader("Zungur PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Zungur Primary Health Centre'
    hf20 = melt.loc[filt]
    st.dataframe(hf20)





