import os
import spotipy
from spotipy import oauth2
from bottle import route, run, request

#from pprint import pprint
#from time import sleep

PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID =os.environ['SPOTIFY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET =os.environ['SPOTIFY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-library-read,user-read-playback-state,user-modify-playback-state'
CACHE = '.spotipyoauthcache'

sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )

@route('/')
def index():

    access_token = ""

    token_info = sp_oauth.get_cached_token()

    if token_info:
        print("Found cached token!")
        access_token = token_info['access_token']
    else:
        url = request.url
        code = sp_oauth.parse_response_code(url)
        if code:
            print("Found Spotify auth code in Request URL! Trying to get valid access token...")
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        print ("Access token available! Trying to get user information...")
        sp = spotipy.Spotify(access_token)
        results = sp.current_user()
        return results

    else:
        return htmlForLoginButton()

def htmlForLoginButton():
    auth_url = getSPOauthURI()
    htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    return htmlLoginButton

def getSPOauthURI():
    auth_url = sp_oauth.get_authorize_url()
    return auth_url

run(host='localhost', port=8080)


# Shows playing devices
#res = sp.devices()
#pprint(res)

# Change track
#sp.start_playback(uris=['spotify:track:6gdLoMygLsgktydTQ71b15'])

# Change volume
#sp.volume(100)
#sleep(2)
#sp.volume(50)
#sleep(2)
#sp.volume(100)