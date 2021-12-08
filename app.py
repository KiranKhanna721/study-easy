from flask import render_template
from forms import *
import json, datetime, requests
from langdetect import detect
from modzy import ApiClient
from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
client = ApiClient(base_url=app.config['API_URL'], api_key=app.config['API_KEY'])

@app.route('/')
def index():   
    return render_template('/index.html')
@app.route('/texttopic', methods=['GET', 'POST'])
def texttopic():
	form = TextTopicModeling()
	if form.validate_on_submit():
		lang = languageanalysis(form.input_text.data)
		input_text = languageTranslation(lang,form.input_text.data)
		data_lang = lang
		data_inputtext = input_text
		data_texttopic = text_topic_modeling(input_text)
		data_textsummary = textsummaries(input_text)
		data_sentiment = sentimentanalysis(input_text)
		data_name = named_entity_recognition(input_text)
		entities = []
		for word in data_name:
			if word[1] !='O':
				entities.append(word)
		data_name = entities
   
		return render_template('/texttopic.html', form=form, data_lang=data_lang, data_inputtext = data_inputtext, data_textsummary = data_textsummary,data_texttopic=data_texttopic,data_name = entities,data_sentiment=data_sentiment)
	return render_template('/texttopic.html', title='Text_Modeling', form=form,data_lang=None, data_inputtext = None, data_textsummary = None,data_texttopic=None,data_name=None,data_sentiment=None)


def text_topic_modeling(input_text):
    job = client.jobs.submit_text('m8z2mwe3pt', '0.0.1',  {'input.txt': input_text})
    result = client.results.block_until_complete(job, timeout=None)
    return(result['results']['job']['results.json'])
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

def named_entity_recognition(input_text):     
    job = client.jobs.submit_text('a92fc413b5', '0.0.12', {'input.txt': input_text})
    result = client.results.block_until_complete(job, timeout=None)
    return(result["results"]['job']['results.json'])
     
 

if __name__ == '__main__':
    app.run()
