import streamlit as st

st.set_page_config(
    page_title="Dynamical systems", 
    page_icon=None, 
    layout="centered", 
    initial_sidebar_state="auto", 
    menu_items=None)

st.title("Dynamical systems")

st.write('''
    Let's check some phase diagrams from simple cases!
'''
)

st.latex(r'''
    \begin{equation}
    \left\{
    \begin{array}{c}
    \frac{dx}{dt} = f(x,y) \\[1em]
    \frac{dy}{dt} = g(x,y)
    \end{array}
    \right.
    \end{equation}
''')