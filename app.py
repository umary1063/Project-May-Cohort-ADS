import streamlit as st
from multiapp import MultiApp
from apps import alkaleri, bogoro, bauchi, dass, kirfi, tafawa_balewa,toro
app = MultiApp()

st.markdown("""
# District Health Information System-2 Data Validation Triggers for Selected Health Facilities in Bauchi State
""")

st.write("This project presents tables by Local Government Areas of Bauchi State, Nigeria that shows a set of data validation triggers for monthly health facility service delivery DATA submitted on the DHIS2 Nigeria instance. Antenetal services, postnetal services, immunization services, labor and delivery services, family planning and malaria services are among the services provided.")

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
