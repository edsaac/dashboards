import streamlit as st
import plotly.express as px

fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16],
                labels={
                    'x':r"$ x \to x^2 $",
                    'y':r"$ x^2 $" })

"## ❌ Using streamlit"
with st.echo():
    st.plotly_chart(fig)

"## ❌ Rendering the exported HTML"
with st.echo():
    st.components.v1.html(fig.to_html(),height=500)

"## ❌ Using streamlit with kwarg `include_mathjax`"
with st.echo():
    ## This is not really a kwarg to be passed to a plotly fig
    st.plotly_chart(fig,include_mathjax="cdn")

"## ✅ Rendering the exported HTML with kwarg `include_mathjax`:"
with st.echo():
    st.components.v1.html(fig.to_html(include_mathjax='cdn'),height=500)