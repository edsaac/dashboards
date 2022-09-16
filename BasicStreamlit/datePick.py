import streamlit as st
import datetime

d = st.date_input(
    "Date input",
    value = datetime.date(50,1,1),
    min_value= datetime.date(1,1,1),
    max_value= datetime.date(200,1,1)
)

print(d)