import requests
import json

class API:
	def __init__(self, access_token):
		self.access_token = access_token
		self.auth_header = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(access_token)
    	}
		self.top_artists = []
		self.top_tracks = []
		self.genre = "hip-hop"

	def get_top_artists_or_tracks(self, code):
		url = "https://api.spotify.com/v1/me/top/{}".format(code)
		params = {
			"limit": "2",
			"time_range": "long_term"
		}
		r = requests.get(url, headers=self.auth_header, params=params)
		resp_json = r.json()
		for item in resp_json['items']:
			if code == "artists":
				uri = item['uri']
				parsed_uri = uri.split(":")[2]
				self.top_artists.append(parsed_uri)
			else:
				uri = item['uri']
				parsed_uri = uri.split(":")[2]
				self.top_tracks.append(parsed_uri)
		return

	def get_seed_recommendations(self):
		url = "https://api.spotify.com/v1/recommendations"
		top_artists_string = ','.join(self.top_artists)
		top_tracks_string = ','.join(self.top_tracks)
		params = {
			"limit": "5",
			"seed_artists": top_tracks_string,
			"seed_tracks" : top_tracks_string,
			"seed_genres" : self.genre 
		}
		r = requests.get(url, headers=self.auth_header, params=params)
		resp_json = r.json()
		track_recommendations = []
		track_uris = []
		for item in resp_json['tracks']:
			track_recommendations.append(item['name'])
			track_uris.append(item['uri'])
		return track_recommendations, track_uris

	def get_recommendations(self):
		self.get_top_artists_or_tracks("artists")
		self.get_top_artists_or_tracks("tracks")
		rec = self.get_seed_recommendations()

		return rec