from genericpath import exists
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from json import dumps
import  climage
import requests
import os
from math import floor
import time



def get_data():
    scope = "user-read-playback-state"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    user = sp.current_user_playing_track()

    song_name = user['item']['name']
    
    album_name = user['item']['album']['name']

    band_name = user['item']['album']['artists'][0]['name']

    progress = user["progress_ms"]

    if os.path.exists(f"/Users/rileymotylinski/Documents/GitHub/spotify-cli-status/pics/{album_name}.png") == False:
        album_art = user['item']['album']['images'][2]['url']
        response = requests.get(album_art)
        file = open(f"/Users/rileymotylinski/Documents/GitHub/spotify-cli-status/pics/{album_name}.png", "wb")
        file.write(response.content)
        file.close()

    output = climage.convert(f"/Users/rileymotylinski/Documents/GitHub/spotify-cli-status/pics/{album_name}.png",width=50)

    

    for x in os.listdir('/Users/rileymotylinski/Documents/GitHub/spotify-cli-status/pics'):
        if x != f"{album_name}.png":
            os.remove(f"/Users/rileymotylinski/Documents/GitHub/spotify-cli-status/pics/{x}")
    
    return song_name, album_name,band_name, output, progress



def print_results(output, song_name, album_name, band_name):
        print(f"""{output} 
    {song_name}

    On {album_name} 
        
    By {band_name}
        """)

def read(additional_num):
    with open("/Users/rileymotylinski/Documents/GitHub/spotify-cli-status/time.txt","r") as f:
        contents = f.readlines()
        new_num = int(contents[0]) + additional_num
        f.close()
        return str(new_num)


def main():
    try:
        songs = []
        while True:
            song_name, album_name, band_name, output, progress = get_data()

            songs.append(song_name)

            if len(songs) > 2:
                del songs[0]

            if len(songs) > 1 and songs[0] != songs[1]:
                print_results(output, song_name, album_name, band_name)

                progress = read(progress)

                print(progress)

                with open("/Users/rileymotylinski/Documents/GitHub/spotify-cli-status/time.txt","w") as f:
                    f.write(progress)
                    f.close()

            time.sleep(1)

    except Exception as e:
        print(e)
        main()
main()