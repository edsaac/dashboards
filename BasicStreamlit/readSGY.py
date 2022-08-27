import streamlit as st
import tempfile
from segysak.segy import segy_header_scan

## Your uploaded SGY file now exists in memory
uploadedSGY = st.file_uploader("Upload file","SGY")

if uploadedSGY:
    
    ## Creates a temporal file
    with tempfile.NamedTemporaryFile() as tempSGY:
        ## Writes the SGY to the temporal file
        tempSGY.write(uploadedSGY.getbuffer())
        
        ## Now you can use the temporal file path
        scan = segy_header_scan(tempSGY.name)
        
        ## Show the data
        st.dataframe(scan)