import climage
import requests
import os

class User:
    def __init__(self,sp):  
        self.data = sp.current_user_playing_track()


    def get_data(self):
        return self.data

    def get_cur_artist_name(self):
        try:
            return self.data["item"]["artists"][0]["name"]
        except TypeError:
            return None

    def print_cur_album_cover(self):
        try:
            album_cover_url = self.data["item"]["album"]["images"][0]["url"]

            img_data = requests.get(album_cover_url).content

            album_name = self.get_cur_album_name()
            with open(f'album_covers/{album_name}.jpg', 'wb') as handler:
                handler.write(img_data)
        
            output = climage.convert(f'album_covers/{album_name}.jpg') 
  
            print(output)

            os.remove(f"album_covers/{album_name}.jpg")
            
        except TypeError:
            return None

    def get_cur_album_name(self):
        try:
            return self.data["item"]["album"]["name"]
        except TypeError:
            return None
    
    def get_cur_album_cover_url(self):
        try:
            return self.data["item"]["album"]["images"][0]["url"]
        except TypeError:
            return None

    def get_cur_song_name(self):
        try:
            return self.data["item"]["name"]
        except TypeError:
            return None

    def update(self,sp):
        self.data = sp.current_user_playing_track()

    def is_playing(self):

        try:
            return self.data["is_playing"]

        except TypeError:
            return False

    def discover_weekly(self,sp):
        try:

            # TODO: does this URL change every week IDK. Have a way for a user to update it...maybe pass it in the request?
            data = sp.playlist("https://open.spotify.com/playlist/37i9dQZEVXcPT2N8xDTnKa?si=d6a5ddc3f46b48ea")

            return data["tracks"]["items"][0]
        except TypeError:
            return None