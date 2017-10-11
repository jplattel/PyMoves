# A python class for easy access to the Moves App data.
# Created by Joost Plattel [http://github.com/jplattel]

import requests


class Moves():
    def __init__(self, client_id, client_secret, redirect_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_url = redirect_url
        self.api_url = 'https://api.moves-app.com/oauth/v1/'

    # Generate an request URL
    def request_url(self):
        u = 'authorize?response_type=code'
        c = '&client_id=' + self.client_id
        s = '&scope=' + 'activity location'
        url = u + c + s
        return url  # Open this URL for the PIN, then authenticate

    # Get access_token
    def auth(self, code):
        a = 'access_token?code=' + code
        c = '&client_id=' + self.client_id
        r = '&redirect_uri=' + self.redirect_url
        s = '&client_secret=' + self.client_secret
        g = '&grant_type=authorization_code'
        j = requests.post(self.API_URL + a + g + c + s + r)
        token = j.json()['access_token']
        return token

    # Standard GET and profile requests

    # Base request
    def get(self, token, endpoint):
        token = '?access_token=' + token
        return requests.get(self.api_url + endpoint + token).json()

    # /user/profile
    def get_profile(self, token):
        token = '?access_token=' + token
        return requests.get(self.api_url + 'user/profile' + token).json()

    # Summary requests

    # /user/summary/daily/<date>
    # /user/summary/daily/<week>
    # /user/summary/daily/<month>
    def get_summary(self, token, date):
        t = '?access_token=' + token
        return requests.get(self.api_url + '/user/summary' + date + t).json()

    # Range requests, max range of 7 days!

    # /user/summary/daily?from=<start>&to=<end>
    # /user/activities/daily?from=<start>&to=<end>
    # /user/places/daily?from=<start>&to=<end>
    # /user/storyline/daily?from=<start>&to=<end>
    def get_range(self, access_token, endpoint, start, end):
        export = get(access_token, endpoint + '?from=' + start + '&to=' + end)
        return export
