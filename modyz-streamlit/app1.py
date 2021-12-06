from langdetect import detect
from modzy import ApiClient
import streamlit as st
SECRET_KEY = 'modzy modelops are incredibles'
API_URL = "https://app.modzy.com/api"
API_KEY ="BLHlhckkavs13Oz3TZqm.MCwXnXb3KaSlLybyEXoP"
client = ApiClient(base_url=API_URL, api_key=API_KEY)
def text_topic_modeling(input_text):
    job = client.jobs.submit_text('m8z2mwe3pt', '0.0.1',  {'input.txt': input_text})
    result = client.results.block_until_complete(job, timeout=None)
    return(result)
def sentimentanalysis(input_text):
	job = client.jobs.submit_text('ed542963de', '1.0.1', {'input.txt': input_text})
	result = client.results.block_until_complete(job, timeout=None)
	return (result['results']['job']['results.json']['data']['result'])
def languageanalysis(input_text):
    return detect(input_text)

def languageTranslation(lang,input_text):
    if lang == 'ru':                                                 
        job = client.jobs.submit_text('5b98cvxsd2', '0.0.1', {'input.txt': input_text})
        result = client.results.block_until_complete(job, timeout=None)
        input_text = result['results']['job']['results.json']['text']
    elif lang == 'en':   
        input_text = input_text
    elif lang == 'ar':  
        job = client.jobs.submit_text('i2gapn1wh7', '0.0.2', {'input.txt': input_text})
        result = client.results.block_until_complete(job, timeout=None)
        input_text = result['results']['job']['results.json']['text']
    elif lang == 'ko':   
        job = client.jobs.submit_text('hprfkvdbgt', '0.0.2', {'input.txt': input_text})
        result = client.results.block_until_complete(job, timeout=None)
        input_text = result['results']['job']['results.json']['text']
    elif lang == 'tr':  
        job = client.jobs.submit_text('ydai26qxaa', '0.0.2', {'input.txt': input_text})
        result = client.results.block_until_complete(job, timeout=None)
        input_text = result['results']['job']['results.json']['text']
    elif lang == 'id':  
        job = client.jobs.submit_text('wn6xe6bizs', '0.0.2', {'input.txt': input_text})
        result = client.results.block_until_complete(job, timeout=None)
        input_text = result['results']['job']['results.json']['text']
    elif lang == 'fa': 
        job = client.jobs.submit_text('u54lgh7rag', '0.0.2', {'input.txt': input_text})
        result = client.results.block_until_complete(job, timeout=None)
        input_text = result['results']['job']['results.json']['text']
    elif lang == 'zh-cn':  
        job = client.jobs.submit_text('24ntd2cn93', '0.0.2', {'input.txt': input_text})
        result = client.results.block_until_complete(job, timeout=None)
        input_text = result['results']['job']['results.json']['text']
    elif lang == 'ur':  
        job = client.jobs.submit_text('vay0g6tavv', '0.0.2', {'input.txt': input_text})
        result = client.results.block_until_complete(job, timeout=None)
        input_text = result['results']['job']['results.json']['text']
    return input_text
  
def textsummaries(input_text):
    job = client.jobs.submit_text('rs2qqwbjwb', '0.0.2', {'input.txt': input_text})
    result = client.results.block_until_complete(job, timeout=None)
    return(result['results']['job']['results.json']['summary'])


def app():  
    input_text = st.text_input('Text')
    submit = st.button('Submit')     
    if submit:     
        if input_text is not None:  
            st.write("Orginal Text : "+input_text)
            lang = languageanalysis(input_text)
            input_text = languageTranslation(lang,input_text)
            data_lang = lang
            st.write("Language : "+data_lang)
            data_inputtext = input_text
            st.write("English text : "+data_inputtext)
            data_texttopic = text_topic_modeling(input_text)
            st.write('Topics : ')
            st.write(data_texttopic)
            data_textsummary = textsummaries(input_text)
            st.write("Summary : "+data_textsummary)
            data_sentiment = sentimentanalysis(input_text)
            st.write("Sentiment : ")
            st.write(data_sentiment)
            