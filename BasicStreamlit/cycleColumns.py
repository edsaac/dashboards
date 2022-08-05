import streamlit as st
from itertools import cycle

captions = list(range(100,800,100))
filteredImages = [f"https://dummyimage.com/400x{w}/d4c9d4/3740bd.jpg&text=Cat_{w}" for w in captions]
cols = cycle(st.columns(4))
checkboxes = []

key = 0
for caption,filteredImage in zip(captions,filteredImages):
    col = next(cols)   
    col.image(filteredImage, use_column_width=True)
    checkboxes.append(col.checkbox(label=f"Caption: {caption}",key=key))
    key += 1   ## Generate an unique key for the checkbox

for check in checkboxes:
    st.sidebar.write(check)

st.success("Yay")