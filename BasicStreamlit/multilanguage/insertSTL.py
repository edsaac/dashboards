import streamlit as st
import pyvista as pv

import gettext
_ = gettext.gettext

language = st.sidebar.selectbox('', ['en', 'es'])
try:
  localizator = gettext.translation('base', localedir='locales', languages=[language])
  localizator.install()
  _ = localizator.gettext 
except:
    pass

## Using pythreejs as pyvista backend
pv.set_jupyter_backend('pythreejs')

## Download an stl file
# filename = examples.download_cad_model(load=False)
uploadedFile = st.file_uploader(_("Upload a STL:"),["stl"],False)

## Streamlit layout
st.sidebar.title(_("STL viewer"))

if uploadedFile:
    
    stlTemp = "./temp.stl"
    with open(stlTemp, "wb") as f: 
        f.write(uploadedFile.getbuffer())

    color = st.sidebar.color_picker(_("Pick a color"),"#1f1f10")

    ## Initialize pyvista reader and plotter
    reader = pv.STLReader(stlTemp)
    plotter = pv.Plotter(
        border=True,
        window_size=[580,400]) 
    plotter.background_color = "white"

    ## Read data and send to plotter
    mesh = reader.read()
    plotter.add_mesh(mesh,color=color)

    ## Export to an external pythreejs
    model_html = "model.html"
    other = plotter.export_html(model_html, backend='pythreejs')

    ## Read the exported model
    with open(model_html,'r') as file: 
        model = file.read()

    ## Show in webpage
    st.components.v1.html(model,height=500)

    ## Final write
    var = 100.0
    st.write(_("Some final text to show with an f-string = {var}"))