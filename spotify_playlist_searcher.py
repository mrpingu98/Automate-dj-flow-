import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Fill in your Spotify app credentials here
CLIENT_ID = '44deba64e2b04230a4e7c818ca419918'
CLIENT_SECRET = '3dc5be53be4d405ba2235a9c114879a3'
REDIRECT_URI = 'http://localhost:8888/callback'  # Can be any URL you set in Spotify dashboard
SCOPE = 'playlist-read-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

playlist_id = 'spotify:playlist:1ARXalCEk6GjKlAzR6sCkX'

results = sp.playlist_items(playlist_id)

for item in results['items']:
    track = item['track']
    artist_names = ', '.join([artist['name'] for artist in track['artists']])
    print(f"{artist_names} {track['name']}")


