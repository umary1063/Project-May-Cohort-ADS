import streamlit as st
import pandas as pd


def app():
    st.title('Dass LGA')

    # In[3]:
    melt=pd.read_excel('melt.xls')
    melt.set_index("Ward", inplace=True)

    #st.header("Dass LGA--Service and Data Gap Analysis July - September 2021")
    st.write("This page display both service & data gap analysis for Dass LGA Main PHCs + GH, kindly scroll-down to review by facility ")


    # ### Filtering by Facility

    # In[4]:
    st.subheader("Badel MCH")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Badel Maternal And Child Health Clinic'
    hf1 = melt.loc[filt]
    st.dataframe(hf1)


    # In[5]:
    st.subheader("Bajar PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Bajar Maternal And Child Health Clinic'
    hf2 = melt.loc[filt]
    st.dataframe(hf2)

    # In[6]:
    st.subheader("Baraza PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Baraza Primary Health Centre'
    hf3 = melt.loc[filt]
    st.dataframe(hf3)


    # In[7]:
    st.subheader    ("Bashi MCH")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Bashi Maternal And Child Health Clinic'
    hf4 = melt.loc[filt]
    st.dataframe(hf4)

    # In[8]:
    st.subheader("Bununu Town PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Bununu Town Primary Health Care Center'
    hf5 = melt.loc[filt]
    st.dataframe(hf5)

    # In[9]:
    st.subheader("Dardak MCH")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Dardak Maternal And Child Health Clinic'
    hf6 = melt.loc[filt]
    st.dataframe(hf6)


    # In[10]:
    st.subheader("Dass General Hospital")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Dass General Hospital'
    hf7 = melt.loc[filt]
    st.dataframe(hf7)



    # In[11]:


    #creating a filter which is similar to a groupby
    st.subheader("Dott PHC")
    filt = melt['Facility Name']== ' Dott Primary Health Centre'
    hf8 = melt.loc[filt]
    st.dataframe(hf8)


    # In[12]:
    st.subheader('Durr MPHC')
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Durr Model Primary Health Centre'
    hf9 = melt.loc[filt]
    st.dataframe(hf9)


    # In[13]:
    st.header("Lukshi MPHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Lukshi Maternal and Health Centre'
    hf10 = melt.loc[filt]
    st.dataframe(hf10)


    # In[14]:
    st.subheader("Polchi PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Polchi Primary Health Centre'
    hf11 = melt.loc[filt]
    st.dataframe(hf11)


    # In[15]:
    st.subheader("Sabon Garin Burgel PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Sabon Gari Burgel Primary Health Centre'
    hf12 = melt.loc[filt]
    st.dataframe(hf12)


    # In[16]:
    st.subheader("Wandi MPHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Wandi Maternaland Child Health Clinic (Dass)'
    hf13 = melt.loc[filt]
    st.dataframe(hf13)


    # In[17]:
    st.subheader("Zumbul MPHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Zumbul Maternal And Child Health Clinic'
    hf14 = melt.loc[filt]
    st.dataframe(hf14)
