import streamlit as st

col1, col2 = st.columns(2)

# Keep the list in the session state
if 'myList' not in st.session_state: 
    st.session_state['myList'] = []

symbols_list = st.session_state['myList']

def add_symbols(tckr):
    symbols_list.append(tckr)
    col2.write(symbols_list)

# Reset the session state 
def empty_list(): del st.session_state['myList']

with col1:
    st.button(label="MYTIL", on_click=add_symbols, args=["MYTIL.AT"])
    st.button(label="OPAP", on_click=add_symbols, args=["OPAP.AT"])
    st.button(label="ADMIE", on_click=add_symbols, args=["ADMIE.AT"])
    st.button(label="EYDAP", on_click=add_symbols, args=["EYDAP.AT"])
    st.button(label="ELPE", on_click=add_symbols, args=["ELPE.AT"])
    st.button(label="HTO", on_click=add_symbols, args=["HTO.AT"])

    st.button(label="❌", on_click=empty_list)