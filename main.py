
import authenticate
import api

if __name__ == "__main__":
	auth = authenticate.Authenticate()
	token = auth.spotipy_call()
	api_obj = api.API(token)
	tracks, uris = api_obj.get_recommendations()
	print(tracks)
