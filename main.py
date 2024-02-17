import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
from User import User
from fastapi import FastAPI


app = FastAPI()

scope = "user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


user = User(sp)   



@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/api/current_artist")
def read_artist():
    artist_name = user.get_cur_artist_name()
    return {"artist_name":  artist_name if artist_name != None and user.is_playing() == True else None}

@app.get("/api/current_album")
def read_album():
    album_name = user.get_cur_album_name()
    user.update(sp)
    return {"album_name":  album_name if album_name != None and user.is_playing() == True else None}


@app.get("/api/current_song")
def read_song():
    song_name = user.get_cur_song_name()
    user.update(sp)
    return {"song_name":  song_name if song_name != None and user.is_playing() == True else None}

@app.get("/api/current_album_cover_url")
def read_album_cover_url():
    album_cover_url = user.get_cur_album_cover_url()
    user.update(sp)
    return {"album_cover_url":  album_cover_url if album_cover_url != None and user.is_playing() == True else None}

@app.get("/api/is_playing")
def read_is_playing():

    user.update(sp)
    return {"is_playing": user.is_playing()}


@app.get("/api/get_playlist/songs/{share_link}")
def discover_weekly(share_link: str):
    return {"data" : user.get_songs_on_playlist(sp,"https://open.spotify.com/playlist/" + share_link)}


