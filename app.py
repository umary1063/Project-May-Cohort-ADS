import streamlit as st
from multiapp import MultiApp
from apps import alkaleri, bogoro, bauchi, dass, kirfi, tafawa_balewa,toro
app = MultiApp()

st.markdown("""
# IHP-Bauchi Embedded Office Supported Health Facilities DHIS2 Data & Service Delivery Validation Triggers
""")

# Add all your application here
app.add_app("Alkaleri LGA gap analysis", alkaleri.app)
app.add_app("Bogoro LGA gap analysis", bogoro.app)
app.add_app("Bauchi LGA gap analysis", bauchi.app)
app.add_app("Dass LGA gap analysis", dass.app)
app.add_app("Kirfi LGA gap analysis", kirfi.app)
app.add_app("Tafawa Balewa LGA gap analysis-", tafawa_balewa.app)
app.add_app("Toro LGA gap Analysis", toro.app)

# The main app
app.run()
