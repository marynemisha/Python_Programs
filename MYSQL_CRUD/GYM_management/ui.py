import streamlit as st
from gym_views import GymMemberManager

connection_instance=GymMemberManager()
tab1,tab2=st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add new member")
    name=st.text_input("Enter member name")
    place=st.text_input("Enter place")
    mobile=st.text_input("Enter phone number")
    plan=st.selectbox("Select your plan",["1 month","2 months","4 months","6 months","8 months","1 year"])
    fee=st.text_input("Enter fee")
    joined_on=st.text_input("Enter joined date(yyyy/mm/dd)")
    if st.button("Add new member"):
        connection_instance.post(name=name,place=place,mobile=mobile,plan=plan,fee=fee,joined_on=joined_on)
        st.success("Member added successfully...!")
with tab2:
    st.title("View member details")
    records = connection_instance.get()
    # print(records)
    if records:
        st.table(records)
    else:
        st.warning("No records found")