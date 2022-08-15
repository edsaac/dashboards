import streamlit as st

st.title("Main Page")

reset_button = st.sidebar.button("🔁 Restart",key='reset_button')

# Empty placeholders
start_btn_ph = st.empty()
text_input_ph = st.empty()
submit_btn_ph = st.empty()

# Check the button state
if 'true_button' in st.session_state: 
    st.session_state.true_button = True
else:
    start_btn_ph.button("Show text input widget",key='true_button')

# On button click but controlled by the session state:
if st.session_state.true_button:
    my_input = text_input_ph.text_input("Input a text here")
    submit = submit_btn_ph.button("Submit",key='submit')
    if submit: st.write(f"You have entered: {my_input}")

# Empty containers and restart
if reset_button:
    del st.session_state.true_button
    text_input_ph.empty()
    submit_btn_ph.empty()
    start_btn_ph.button("Show input",key='true_button')