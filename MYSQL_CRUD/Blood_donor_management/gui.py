import streamlit as st
from blood_donor_view import BloodDonorManager


donor_instance=BloodDonorManager()
tab1,tab2=st.tabs(["ADD","VIEW"])

with (tab1):
    st.title("Add New Blood Donors")
    name=st.text_input("Enter Blood Donor Name")
    blood_group=st.selectbox("Select Blood Group",["A+","A-","B+","B-","AB+","AB-","O+","O-"])
    phone=st.text_input("Enter Phone Number")
    city=st.text_input("Enter City")
    last_donation=st.text_input("Enter Last Donation(YYYY/MM/DD)")
    if st.button("Add New Donor"):
        donor_instance.post(name=name,blood_group=blood_group,phone=phone,city=city,last_donation=last_donation)
        st.success("Donor added successfully...!")
with tab2:
    st.title("View Blood Donor Details")
    records=donor_instance.get()
    # print(records)
    if records:
        st.table(records)
    else:
        st.warning("No records found")

