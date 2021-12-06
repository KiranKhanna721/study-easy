import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'modzy modelops are incredibles'

	API_URL = os.environ.get('API_URL') or "https://app.modzy.com/api"
	API_KEY = os.environ.get('API_KEY') or "BLHlhckkavs13Oz3TZqm.MCwXnXb3KaSlLybyEXoP"
	
	DEBUG =  os.environ.get('FLASK_DEBUG') or 0