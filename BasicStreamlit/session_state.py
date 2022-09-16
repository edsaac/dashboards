import streamlit as st

if 'button_1' not in st.session_state:
    st.session_state.button_1 = False
if 'button_2' not in st.session_state:
    st.session_state.button_2 = False