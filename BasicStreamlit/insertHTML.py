import streamlit as st

path_to_html = "./the_html_file_i_wanna_show.html" 

# Read file and keep in variable
with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
st.header("Show an external HTML")
st.components.v1.html(html_data,height=200)