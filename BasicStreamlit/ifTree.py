import streamlit as st

def func1(): st.info("Function 1 executed.")
def func2(): st.info("Function 2 executed.")

# Function to run chosen function(s)
def execute():
    if cb1: func1()
    if cb2: func2()

# Sidebar configurations
cb1 = st.sidebar.checkbox('Function 1', key='a')
cb2 = st.sidebar.checkbox('Function 2', key='b')
run_btn = st.sidebar.button('Run', on_click=execute, key='c')