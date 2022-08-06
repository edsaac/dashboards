import streamlit as st

def func1(): st.write("Function 1 executed.")
def func2(): st.write("Function 2 executed.")
def func3(): st.write("Function 3 executed.")

# function to run chosen function(s)
def execute():
    if cb1: func1()
    if cb2: func2()
    if cb3: func3()

# checkbox shenanigans 
cbAll = st.sidebar.checkbox("Select All")

if cbAll:
    cb1 = st.sidebar.checkbox("Func 1",value=cbAll,disabled=True,key=1)
    cb2 = st.sidebar.checkbox("Func 2",value=cbAll,disabled=True,key=2)
    cb3 = st.sidebar.checkbox("Func 3",value=cbAll,disabled=True,key=3)
else:
    cb1 = st.sidebar.checkbox("Func 1",key=4)
    cb2 = st.sidebar.checkbox("Func 2",key=5)
    cb3 = st.sidebar.checkbox("Func 3",key=6)

run_btn = st.sidebar.button('Run', on_click=execute, key='e')

## Does not work
# import streamlit as st

# def func1(): st.write("Function 1 executed.")
# def func2(): st.write("Function 2 executed.")
# def func3(): st.write("Function 3 executed.")

# # function to run chosen function(s)
# def execute():
#     if multiselect:
#         for i,func in enumerate(functionList):
#             if multiselect[i]: func()
#     else:
#         st.warning(":warning: No functions were selected")

# # checkbox shenanigans 
# cbAll = st.sidebar.checkbox("Select All")

# optionList = ["Function 1","Function 2","Function 3"]
# functionList = [func1,func2,func3]

# if cbAll:
#     multiselect = st.sidebar.multiselect("Select functions",options=optionList,default=optionList,disabled=True,key=2)

# else:
#     multiselect = st.sidebar.multiselect("Select functions",options=optionList,default=None,key=1)

# run_btn = st.sidebar.button('Run', on_click=execute, key='e')