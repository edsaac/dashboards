import streamlit as st

st.set_page_config(layout='wide')

st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(1)
        {
            border:1px solid red;
        } 

        div[data-testid="column"]:nth-of-type(2)
        {
            border:1px solid blue;
            text-align: end;
        } 
    </style>
    """,unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    """
    ## Column 1 
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
    sed do eiusmod tempor incididunt ut labore et dolore 
    magna aliqua. Volutpat sed cras ornare arcu dui vivamus.
    """
with col2:
    """
    ## Column 2
    Stuff aligned to the right
    """
    st.button("➡️")
with col3:
    """
    ## Column 3
    This column was untouched by our CSS 
    """
    st.button("🐈")