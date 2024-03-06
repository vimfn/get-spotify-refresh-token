import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values

config = dotenv_values(".env")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=config["SPOTIFY_CLIENT_ID"],
        client_secret=config["SPOTIFY_CLIENT_SECRET"],
        redirect_uri=config["SPOTIFY_REDIRECT_URI"],
        scope="playlist-modify-private",
    )
)

current_user = sp.current_user()

assert current_user is not None

print(current_user["id"], "token saved in '.cache' folder.")