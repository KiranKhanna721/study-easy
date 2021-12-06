from langdetect import detect
from modzy import ApiClient
import streamlit as st
SECRET_KEY = 'modzy modelops are incredibles'
API_URL = "https://app.modzy.com/api"
API_KEY ="BLHlhckkavs13Oz3TZqm.MCwXnXb3KaSlLybyEXoP"
client = ApiClient(base_url=API_URL, api_key=API_KEY)

def deepfake(input_text):
    job = client.jobs.submit_files('93ltr2oepu', '0.0.6', {'input.mp4': input_text})
    result = client.results.block_until_complete(job, timeout=None)
    return(result.get_first_outputs()['results.json'])
def caption(input_text):
    job = client.jobs.submit_files('cyoxn54q5g', '0.0.2', {'input.mp4': input_text})
    result = client.results.block_until_complete(job, timeout=None)
    return(result.get_first_outputs()['results.json'])


def app():    
    video = st.file_uploader("Choose an video...", type="mp4")
    submit = st.button('Predict')
    if submit:  
        if video is not None:  
            data_deep = deepfake(video)
            st.write("Fake ratio : ")
            st.write(data_deep['input.mp4'])
  
