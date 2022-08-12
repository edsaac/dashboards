import streamlit as st

listTabs = [
    "A tab",
    "🦈",
    "More tabs",
    "A long loooooong tab",
    "🎨",
    "x²"
]

st.header("Tab alignment")
st.subheader("No fill:")
tabs = st.tabs(listTabs)

st.markdown("----")

whitespace = 9
st.markdown("#### 💡 Center fill with whitespace (em-space):")
## Fills and centers each tab label with em-spaces
tabs = st.tabs([s.center(whitespace,"\u2001") for s in listTabs])

st.markdown("#### 🤔 Center fill with visible character")
tabs = st.tabs([s.center(whitespace,"-") for s in listTabs])

st.markdown("#### ❌ Regular spaces are stripped down by streamlit")
tabs = st.tabs([s.center(whitespace," ") for s in listTabs])

# st.markdown("""
#     <style>
#     .stTabs {
#         border:solid 2px #0094ff;
#         padding:10px;
#         border-radius:5px;
#     }
#     .st-ce {
#         font-size:20px;
#         font-weight:bold;
#     }
#     </style>
# """,unsafe_allow_html=True)

st.markdown("""
    <style>
    button[data-baseweb="tab"] {
    font-size: 26px;
    }
    </style>
""",unsafe_allow_html=True)
