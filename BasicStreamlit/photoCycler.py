import streamlit as st
import os

col1,col2 = st.columns(2)

if 'counter' not in st.session_state: 
    st.session_state.counter = 0

def showPhoto(photo):
    col2.image(photo,caption=photo)
    col1.write(f"Index as a session_state attribute: {st.session_state.counter}")
    
    ## Increments by one the counter for the next photo
    st.session_state.counter += 1
    if st.session_state.counter >= len(pathsImages):
        st.session_state.counter = 0

# Get list of images in folder
folderWithImages = r"images"
pathsImages = [os.path.join(folderWithImages,f) for f in os.listdir(folderWithImages)]

col1.subheader("List of images in folder")
col1.write(pathsImages)

# Select photo a send it to button
photo = pathsImages[st.session_state.counter]
show_btn = col1.button("Show next pic ⏭️",on_click=showPhoto,args=([photo]))

# import streamlit as st
# import os
# from itertools import cycle

# print("----------")

# col1,col2 = st.columns(2)

# def showPhoto(photo):
#     col2.image(photo,caption=photo)

# folderWithImages = r"images"
# pathsImages = [os.path.join(folderWithImages,f) for f in os.listdir(folderWithImages)]

# if 'counter' not in st.session_state:
#     cycleImages = cycle(pathsImages)
#     st.session_state.counter = next(cycleImages)
# else:
#     st.session_state.counter = next(cycleImages)

# col1.subheader("List of images in folder")
# col1.write(pathsImages)
# col1.write(st.session_state.counter)

# photo = st.session_state.counter
# show_btn = col1.button("Show next pic ⏭️",on_click=showPhoto,args=([photo]))





