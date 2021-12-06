import numpy as np
import streamlit as st
import app1
import app2
import app3
PAGES = {
    "Text Analysis": app1 , 
    "Named_entity_recognition" : app2 , 
    "Deep" : app3
    
}
st.sidebar.title('Study_Easy')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()