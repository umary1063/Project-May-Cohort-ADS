import streamlit as st
import pandas as pd
import numpy as np

def app():
    st.title('Alkaleri LGA')
    melt=pd.read_excel('melt.xls')
    melt.set_index("Ward", inplace = True)
    #st.header("Alkaleri LGA--Service and Data Gap Analysis July 2021 -- September 2021")
    st.write("This page display both service & data gap analysis for Alkaleri LGA, kindly scroll-down to review by facility ")

    st.subheader('Alkaleri General Hospital')
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Alkaleri General Hospital'
    hf1 = melt.loc[filt]
    st.dataframe(hf1)

    st.subheader('Alkaleri Town Maternal & Child Health Clinic')
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Alkaleri Town Maternal & Child Health Clinic'
    hf2 = melt.loc[filt]
    st.dataframe(hf2)

    st.subheader("Bajama PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Bajama Primary Health Center'
    hf3 = melt.loc[filt]
    st.dataframe(hf3)

    st.subheader("Bakin Kogi PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Bakin Kogi Model Primary Health Centre'
    hf4 = melt.loc[filt]
    st.dataframe(hf4)

    st.subheader("Digare PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Digare Primary Health center'
    hf5 = melt.loc[filt]
    st.dataframe(hf5)

    st.subheader("Duguri PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Duguri Primary Health Care Centre'
    hf6 = melt.loc[filt]
    st.dataframe(hf6)

    st.subheader("Futuk PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Futuk Primary Health Center'
    hf7 = melt.loc[filt]
    st.dataframe(hf7)

    st.subheader("Gar PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Gar Primary Health Center'
    hf8 = melt.loc[filt]
    st.dataframe(hf8)

    st.subheader("Garin Hamza PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Garin Hamza  PrimaryHealth Center'
    hf9 = melt.loc[filt]
    st.dataframe(hf9)

    st.subheader("Gokaru PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Gokaru Primary Health center'
    hf10 = melt.loc[filt]
    st.dataframe(hf10)


    st.subheader("Gorondo PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Gorondo Primary Health Center'
    hf11 = melt.loc[filt]
    st.dataframe(hf11)

    st.subheader("Gwana PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Gwana Primary Health Center'
    hf12 = melt.loc[filt]
    st.dataframe(hf12)

    st.subheader("Gwaram PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Gwaram Primary Health Center'
    hf13 = melt.loc[filt]
    st.dataframe(hf13)

    st.subheader("Kunduk PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Kundak Primary Health Center'
    hf14 = melt.loc[filt]
    st.dataframe(hf14)

    st.subheader("Maimadi PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Maimadi PrimaryHealth Center'
    hf15 = melt.loc[filt]
    st.dataframe(hf15)

    st.subheader("Mansur PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Mansur  Primary Health Center'
    hf16 = melt.loc[filt]
    st.dataframe(hf16)

    st.subheader("Pali PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Pali Primary Health Centre'
    hf17 = melt.loc[filt]
    st.dataframe(hf17)

    st.subheader("Shira PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Shira Primary Health Center'
    hf18 = melt.loc[filt]
    st.dataframe(hf18)

    st.subheader("Yalo PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Yalo Primary Health Center'
    hf19 = melt.loc[filt]
    st.dataframe(hf19)


    st.subheader("Yalwan Duguri PHC")
    #creating a filter which is similar to a groupby
    filt = melt['Facility Name']== ' Yelwan Duguri Model Primary Health Center'
    hf20 = melt.loc[filt]
    st.dataframe(hf20)