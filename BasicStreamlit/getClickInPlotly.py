import streamlit as st
from streamlit_plotly_events import plotly_events

import plotly.graph_objects as go
import numpy as np

corrMatrix = np.array(
       [[2, 6, 3, 3, 8, 0, 1, 7, 1],
       [3, 1, 5, 2, 9, 5, 9, 6, 6],
       [7, 0, 9, 4, 7, 7, 2, 3, 2],
       [9, 8, 3, 0, 3, 0, 3, 0, 6],
       [6, 6, 5, 2, 9, 9, 1, 8, 9],
       [6, 1, 3, 1, 7, 7, 3, 8, 9],
       [9, 0, 9, 9, 6, 1, 1, 2, 4],
       [3, 1, 1, 7, 8, 1, 0, 8, 6]])

st.title("Hello!")

## Create figure and pass it to plotly_events
fig = go.Figure()
heat = fig.add_heatmap(z=corrMatrix)
selected_points = plotly_events(fig, click_event=True)

## Click event on a single figure
point = selected_points[0]

## Where did we click?
st.header(":mouse: Where click?")
st.metric("X",point['x'])
st.metric("Y",point['y'])
