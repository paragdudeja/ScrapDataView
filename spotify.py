import spotipy.util as util

endpoint = 'https://accounts.spotify.com/authorize?'
client_id = 'd3bb240edf044e34b92d9843f5fd2c80'
client_secret = '789d207613ee4e2fa509c355afeaf22c'
response_type = 'code'
redirect_uri = 'http://localhost:8888/callback'
scope = 'playlist-modify-private playlist-modify-public user-read-private user-read-email playlist-read-private playlist-read-collaborative'

token = util.prompt_for_user_token(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
print(token)