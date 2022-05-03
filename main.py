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
    # Defines access scope for the spotify API so that I can access user data
    scope = "user-read-playback-state"

    # Creates "sp" object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    user = sp.current_user_playing_track()

    # Pretty Self explanatory, access's the dict  that the previous line returns, and  gets the 
    # data associated with the var name
    song_name = user['item']['name']
    
    album_name = user['item']['album']['name']

    band_name = user['item']['album']['artists'][0]['name']

    progress = user["progress_ms"]

    # Makes sure  that the album art doesn't already exists withing the "pics" directory, otherwise it grabs it from the dict as well
    if os.path.exists(f"pics/{album_name}.png") == False:
        album_art = user['item']['album']['images'][2]['url']
        response = requests.get(album_art)
        file = open(f"pics/{album_name}.png", "wb")
        file.write(response.content)
        file.close()

    # Converts the image into album art to the pixel-esque art displayed on the terminal
    output = climage.convert(f"pics/{album_name}.png",width=50)

    
    # deletes any unnecessary album covers
    for x in os.listdir('pics'):
        if x != f"{album_name}.png":
            os.remove(f"pics/{x}")
    
    return song_name, album_name,band_name, output, progress


# Formats the data to make it look nice
def print_results(output, song_name, album_name, band_name):
        print(f"""{output} 
    {song_name}

    On {album_name} 
        
    By {band_name}
        """)


# Single use function, only used for getting the current total time from the "time.txt" file
def read(additional_num):
    with open("time.txt","r") as f:
        contents = f.readlines()
        new_num = int(contents[0]) + int(additional_num)
        f.close()
        return str(new_num)

# Another single use function, returns the backup_time.txt (or the previous API calls progrss) 
def return_file_contents():
    with open("backup_time.txt","r") as f:
        ls = f.readlines()
        f.close()
    return ls[0]



def main():
    try:
        songs = []
        
        # Goes until user interrupt; fix?
        while True:
            song_name, album_name, band_name, output, progress = get_data()

            # Constanlty updates the "songs" list so that I can check it later
            songs.append(song_name)

            # Deletes any unnecessary songs
            if len(songs) > 2:
                del songs[0]

            # makes sure the length of songs is >1 so it doesn't throw an error when the list is empty.
            # Also executes the code if the song changes
            if len(songs) > 1 and songs[0] != songs[1]:

                print_results(output, song_name, album_name, band_name)
                backup_ms = return_file_contents()

                total = read(backup_ms)
                print(total)

                # Write the total time to file
                with open("time.txt","w") as f:
                    f.write(str(total))
                    f.close()
        
            # writes down backup time, I only do this at the end so that I don't have to worry about losing this var
            with open("backup_time.txt","w") as f:
                f.write(str(progress))

            # only necessary to call the API every second, no more
            time.sleep(1)

    except Exception as e:
        print(e)

        main()
main()