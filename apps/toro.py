import streamlit as st
import pandas as pd

def app():
        st.title('Toro LGA')


        melt=pd.read_excel('melt.xls')
        melt.set_index("Ward", inplace=True)
        #st.subheader("Toro LGA--Service and Data Gap Analysis July - September 2021")
        st.write("This page display both service & data gap analysis for Toro LGA Main PHCs + GH, kindly scroll-down to review by facility ")





        #creating a filter which is similar to a groupby
        st.subheader("Bukka Tulai PHC")
        filt = melt['Facility Name']== ' Bukka Tulai Primary Health Care Centre'
        hf1 = melt.loc[filt]
        st.dataframe(hf1)

        # In[5]:


        #creating a filter which is similar to a groupby
        st.subheader("Geljaule PHC")
        filt = melt['Facility Name']== ' Geljaule Primary Health Care Centre'
        hf2 = melt.loc[filt]
        st.dataframe(hf2)

        # In[6]:


        #creating a filter which is similar to a groupby
        st.subheader("Gumau PHC")
        filt = melt['Facility Name']== ' Gumau Primary Health Care  Center'
        hf3 = melt.loc[filt]
        st.dataframe(hf3)

        # In[7]:


        #creating a filter which is similar to a groupby
        st.subheader("Gwalfada PHC")
        filt = melt['Facility Name']== ' Gwalfada Primary Health Care Centre'
        hf4 = melt.loc[filt]
        st.dataframe(hf4)

        # In[8]:


        #creating a filter which is similar to a groupby
        st.subheader("Jamaa PHC")
        filt = melt['Facility Name']== " Jama'a Primary Health Clinic"
        hf5 = melt.loc[filt]
        st.dataframe(hf5)

        # In[9]:


        #creating a filter which is similar to a groupby
        st.subheader("Lame PHC")
        filt = melt['Facility Name']== ' Lame Primary Health Care Center'
        hf6 = melt.loc[filt]
        st.dataframe(hf6)

        # In[10]:


        #creating a filter which is similar to a groupby
        st.subheader("Magaman Gumau PHC")
        filt = melt['Facility Name']== ' Magaman Gumau Primary Health care Centre'
        hf7 = melt.loc[filt]
        st.dataframe(hf7)

        # In[11]:


        #creating a filter which is similar to a groupby
        st.subheader("Nahuta PHC")
        filt = melt['Facility Name']== ' Nahuta Primary Health Care Center'
        hf8 = melt.loc[filt]
        st.dataframe(hf8)

        # In[12]:


        #creating a filter which is similar to a groupby
        st.subheader("Nabardo PHC")
        filt = melt['Facility Name']== ' Nabardo Primary Health Centre'
        hf9 = melt.loc[filt]
        st.dataframe(hf9)

        # In[13]:


        #creating a filter which is similar to a groupby
        st.subheader("Rahama PHC")
        filt = melt['Facility Name']== ' Rahama Model Primary Health Centre'
        hf10 = melt.loc[filt]
        st.dataframe(hf10)

        # In[14]:


        #creating a filter which is similar to a groupby
        st.subheader("Rimin Zayam PHC")
        filt = melt['Facility Name']== ' Rimin Zayam Primary Health Care Centre'
        hf11 = melt.loc[filt]
        st.dataframe(hf11)

        # In[15]:


        #creating a filter which is similar to a groupby
        st.subheader("Rinjin Gaini PHC")
        filt = melt['Facility Name']== ' Rinjin Gaini Primary Health Care Centre'
        hf12 = melt.loc[filt]
        st.dataframe(hf12)

        # In[16]:


        #creating a filter which is similar to a groupby
        st.subheader("Rishi PHC")
        filt = melt['Facility Name']== ' Rishi Primary Health Centre'
        hf13 = melt.loc[filt]
        st.dataframe(hf13)

        # In[17]:


        #creating a filter which is similar to a groupby
        st.subheader("Tilden Fulani PHc")
        filt = melt['Facility Name']== ' Tilden Fulani Primary Health Clinic'
        hf14 = melt.loc[filt]
        st.dataframe(hf14)

        # In[18]:


        #creating a filter which is similar to a groupby
        st.subheader("Toro General Hospital")
        filt = melt['Facility Name']== ' Toro General Hospital'
        hf15 = melt.loc[filt]
        st.dataframe(hf15)

        # In[19]:


        #creating a filter which is similar to a groupby
        st.subheader("Tulu PHC")
        filt = melt['Facility Name']== ' Tulu Primary Health Care Centre'
        hf16 = melt.loc[filt]
        st.dataframe(hf16)

        # In[20]:


        #creating a filter which is similar to a groupby
        st.subheader("Zakshi PHC")
        filt = melt['Facility Name']== ' Zakshi Primary Health Care Centre'
        hf17 = melt.loc[filt]
        st.dataframe(hf17)

        # In[21]:


        #creating a filter which is similar to a groupby
        st.subheader("Zalau PHC")
        filt = melt['Facility Name']== ' Zalau Primary Health  Care Centre'
        hf18 = melt.loc[filt]
        st.dataframe(hf18)