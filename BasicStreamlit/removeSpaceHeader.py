import streamlit as st

st.title("Site")
st.write("Some text")
st.file_uploader("Upload a file",["jpg"])
st.sidebar.info("Show the sidebar")

## Add background image
st.markdown(
    '''
    <style>
    header[data-testid="stHeader"]{
        background-image: url(https://placekitten.com/g/100/50);
        background-repeat: repeat;
        background-position: center;
    }
    </style>
    ''',unsafe_allow_html=True)

## Change padding
st.markdown(
    '''
    <style>
    .stApp {
        background: rgb(255,255,240);
    }
    .block-container {
        padding-top: 15rem;
    }
    </style>
    ''',unsafe_allow_html=True)

# ## Center stuff??
# st.markdown(
#     '''
#     <style>
#     div[data-testid="stFileUploader"] {
#         width: 50%;
#         justify-content:center;
#     }
#     </style>
#     ''',unsafe_allow_html=True)

