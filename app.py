import streamlit as st
import langchain_helper as lh
import re

st.title = "Resturant Name Generator"

openapi_key = st.sidebar.text_input("Enter OPEN API KEY", key="openapi_key")
cuisine = st.sidebar.selectbox("pick a cuisine",("Indian", "Pakistani", "Chinese", "Russian", "Arabic", "American"))
submit =st.sidebar.button("Submit")

if submit:
    lh.initialize_openAPI_key(openapi_key)
    response = lh.generate_resturant_name(cuisine)
    st.header("Resturant Name: "+ response["name"].strip())
    menu_items = re.split("[,\n]",response["items"].strip())
    st.write("****Menu Items****")
    for item in menu_items:
        st.write(item)
    



