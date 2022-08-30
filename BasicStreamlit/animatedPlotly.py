import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

# Helix equation
t = np.linspace(0, 10, 50)
x, y, z = np.cos(t), np.sin(t), t

df = pd.DataFrame({
    "t":t,
    "x":x,
    "y":y,
    "z":z})

fig = px.scatter_3d(df,x='x',y='y',z='z',animation_frame='t',
    range_x=[-1.2,1.2],range_y=[-1.2,1.2],range_z=[-1,10])

fig.update_layout(height=600)

st.plotly_chart(fig)

# # Create figure
# fig = go.Figure()

# fig.add_traces([
#     go.Scatter3d(
#         x=[x[0]],
#         y=[y[0]],
#         z=[z[0]],
#         mode="markers",
#         marker=dict(color="red", size=4)),
#     go.Scatter3d(
#         x = x, 
#         y = y,
#         z = z,
#         mode="lines",
#         line= {
#             'width':2,
#             'color':"blue"}
#         )
#     ])
    
# fig.update_layout(
#     height = 600,
#     scene = {
#     "xaxis" : {
#         'range':[-1.2,1.2],
#         'autorange':False,
#         'zeroline':False
#         },
#     "yaxis" : {
#         'range':[-1.2,1.2],
#         'autorange':False,
#         'zeroline':False
#         },
#     "zaxis" : {
#         'range':[-1,10],
#         'autorange':False,
#         'zeroline':False
#         }
#     },
#     updatemenus = [
#         {
#         "buttons": [
#             {
#                 "args": [None],
#                 "label": "Play",
#                 "method": "animate"
#             },
#         ],
#         "direction": "left",
#         "pad": {"r": 10, "t": 87},
#         "showactive": False,
#         "type": "buttons",
#         "x": 0.1,
#         "xanchor": "right",
#         "y": 0,
#         "yanchor": "top"
#         }
#     ] )

# def generateFrame(xi,yi,zi):
#     return go.Frame(
#         data = [go.Scatter3d(
#             x=[xi],
#             y=[yi],
#             z=[zi],
#             mode="markers",
#             marker=dict(color="red", size=4))]
#         )

# fig.frames = [generateFrame(xi,yi,zi) for xi,yi,zi in zip(x,y,z) ]

# fig.layout.updatemenus[0].buttons[0]['args'] = dict(transition=dict(duration=1))

# st.plotly_chart(fig)