import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint






def get_cur_artist_name(sp):
    user = sp.current_user_playing_track()

    return user["item"]["artists"][0]["name"]

def get_cur_album_name(sp):
    user = sp.current_user_playing_track()

    return user["item"]["album"]["name"]



# Formats the data to make it look nice
def print_results(output, song_name, album_name, band_name):
        print(f"""{output} 
    {song_name}

    On {album_name} 
        
    By {band_name}
        """)



def main():
    scope = "user-read-playback-state"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    
    print(get_cur_album_name(sp))
main()