# import streamlit as st
# import extra_streamlit_components as stx

# whichStep = stx.stepper_bar(steps=["Ready", "Get Set", "Go"])
# placeholder = st.container()

# if whichStep == 0:
#     placeholder.markdown(f"## Welcome to `step {whichStep}`")
#     placeholder.text_input("Give me a message:",max_chars=1000,key="message_og")
#     placeholder.image("https://placekitten.com/g/1400/600",caption=f"Meowhy from {whichStep}")

# elif whichStep == 1:
#     placeholder.markdown(f"## Hello, this is `step {whichStep}`")
#     if "message_og" in st.session_state.keys():
#         if st.session_state.message_og:
#             placeholder.markdown(f"It's ok, I'm keeping this message:\n `{st.session_state.message_og}`")
#             placeholder.text_input("Add something else",key="message_add")
#             placeholder.radio("Pick one:", ["♣","♦","♥","♠"],key="radio_option")
#             if placeholder.button("GO!"): placeholder.success("Now move to step 3")
#         else:
#             placeholder.warning("Don't skip step 1! ",icon="🐈")
# elif whichStep == 2:
#     message = st.session_state.message_og + st.session_state.message_add + st.session_state.radio_option
#     placeholder.write(message)

#     # if st.form_submit_button("Submit"):
#     #     moreText = st.text_input("Add something else?")
#     #     anotherButton = st.download_button(
#     #         "Download",
#     #         data = st.session_state.message + st.session_state.radio_option)
# else:
#     placeholder = st.empty()

 
# # I have a streamlit app that uses st.tabs for guiding a user through 
# # a workflow. For the first two tabs, the user is just selecting the 
# # parameters for the main functionality on tab 3 and I don’t run into 
# # any issues there.

# # The issue arises on the 3rd tab, where 
# # I have an st.form_submit_button that in turn helps me generate an st.download_button for the user. After the user presses the form submit button, streamlit refreshes and st.tab default view returns to tab 1, causing the user to navigate back to the third tab for their download button. This makes the overall process feel less seamless. Hoping to find a work around if there is one. Would appreciate any help on this.
# # st.info(f"Phase #{val}")

import streamlit as st
if 'page' not in st.session_state: st.session_state.page = 0
def nextPage(): st.session_state.page += 1
def firstPage(): st.session_state.page = 0

ph = st.empty()

## Page 1
if st.session_state.page == 0:
    with ph.container():
        st.header("This is page 1")
        st.button("Go to page 2",on_click=nextPage)

## Page 2
elif st.session_state.page == 1:
    with ph.container():
        st.header("This is page 2")
        st.write("Other stuff in page 2")
        st.write("More stuff in page 2")
        st.write("More more stuff in page 2")
        st.write("More more more stuff in page 2")
        st.button("Go to page 3",on_click=nextPage)

## Page 3
elif st.session_state.page == 2:
    with ph.container():
        st.header("This is page 3")
        st.image("https://placekitten.com/g/1400/600",caption=f"Meowhy")
        st.button("Go back",on_click=firstPage)

# for k,v in st.session_state.items():
#     st.sidebar.markdown(f"### Key `{k}` is `{v}`")

# import streamlit as st 

# ##  Logic control
# def c(): st.session_state.b1 = True
# def d(): st.session_state.b2 = True
# if 'b1' not in st.session_state: st.session_state.b1 = False
# if 'b2' not in st.session_state: st.session_state.b2 = False

# ## Think of the placeholder here as a list initialized with no elements
# ph = st.empty()

# ## Here you start adding elements to the placeholder 
# with ph.container():
#     st.write("1️⃣ First element in placeholder")       # ph[0] = a st.write        
#     st.button("1️⃣ Second element in ph (Go to page 2)",on_click=c)   # ph[1] = a st.button

# if st.session_state.b1:
#     with ph.container():
#         st.write("2️⃣ This overwrites the first element")    # ph[0] = a new st.write
#         st.write("2️⃣ This overwrites the second element")   # ph[1] = a new st.write
#         st.write("2️⃣ Third element in placeholder")         # ph[2] = a st.write
#         st.button("2️⃣ Fourth element in ph (Go to page 3)",on_click=d)     # ph[3] = a st.button

# if st.session_state.b2:
#     with ph.container():
#         st.write("3️⃣ This replaces again the first element")   # ph[0] = a new st.write
#         st.write("3️⃣ This replaces again the second element")  # ph[1] = a new st.write
#         ## Nothing is replacing the third element              # ph[2] = a st.write
#         ## Nothing is replacing the fourth element             # ph[3] = a st.button

# for k,v in st.session_state.items():
#     st.sidebar.markdown(f"### Key `{k}` is `{v}`")

# import streamlit as st
# placeholder = st.empty()

# # Replace the placeholder with some text:
# placeholder.text("Hello")


# # Replace the chart with several elements:
# with placeholder.container():
#      st.write("This is one element")
#      st.write("This is another")
#      st.write("This is another kind")

# # Replace the text with a chart:
# placeholder.line_chart({"data": [1, 5, 2, 6]})

# # Clear all those elements:
# # placeholder.empty()