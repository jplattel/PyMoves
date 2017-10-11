# A python class for easy access to the Moves App data. Created by Joost Plattel [http://github.com/jplattel]

import requests

class Moves():

	def __init__(self):
		self.CLIENT_ID = ''	   # Client ID, get this by creating an app
		self.CLIENT_SECRET = '' # Client Secret, get this by creating an app
		self.REDIRECT_URL = ''  # Callback URL for getting an access token
		self.API_URL = 'https://api.moves-app.com/oauth/v1'

	# Generate an request URL
	def request_url(self):
		u = self.API_URL + '/authorize?response_type=code'
		c = '&client_id=' + self.CLIENT_ID
		s = '&scope=' + 'activity location' # Assuming we want both activity and locations
		url = u + c + s 
		return url # Open this URL for the PIN, then authenticate with it and it will redirect you to the callback URL with a request-code, specified in the API access.

	# Get access_token 
	def auth(self, request_token):
		u = self.API_URL + '/access_token'
		c = '&client_id=' + self.CLIENT_ID
		r = '&redirect_uri=' + self.REDIRECT_URL
		s = '&client_secret=' + self.CLIENT_SECRET
		j = requests.post('?grant_type=authorization_code&code=' + request_token + c + s + r)
		token = j.json()['access_token']
		return token 
		
	# Standard GET and profile requests

	# Base request
	def get(self, token, endpoint):
		token = '?access_token=' + token
		return requests.get(self.API_URL + endpoint + token).json()

	# /user/profile
	def get_profile(self, token):
		token = '?access_token=' + token
		return requests.get(self.API_URL + '/user/profile' + token).json()

	# Summary requests

	# /user/summary/daily/<date>
	# /user/summary/daily/<week>
	# /user/summary/daily/<month>
	def get_summary(self, token, date):
		token = '?access_token=' + token
		return requests.get(self.API_URL + '/user/summary' + date + token).json()

	
	# Range requests, max range of 7 days!

	# /user/summary/daily?from=<start>&to=<end>
	# /user/activities/daily?from=<start>&to=<end>
	# /user/places/daily?from=<start>&to=<end>
	# /user/storyline/daily?from=<start>&to=<end>
	def get_range(access_token, endpoint, start, end):
		export = get(access_token, endpoint + '?from=' + start + '&to=' + end) 
		return export


