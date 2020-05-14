import requests
import json
import spotipy.util as util

from secrets import client_id, client_secret

redirect_uri = 'http://localhost:8888/callback'
code = 'code'
username = 'kampfwagen'
scope='user-top-read'

class Authenticate:
	def __init__(self):
		self.access_token = ""

	def spotipy_call(self):
		token = util.prompt_for_user_token(username=username, scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
		self.access_token = token
		return token

		'''
	# Step 1
	def request_authorization(self):
		auth_url = 'https://accounts.spotify.com/authorize'
		payload = {'client_id' : client_id, 'response_type' : code, 'redirect_uri' : redirect_uri}vi
		r = requests.get(auth_url, params=payload)
		print(r.text)
		return

	# Step 2
	def request_access_and_refresh(self):
		return

	# Step 4
	def request_refresh(self):
		return
	'''