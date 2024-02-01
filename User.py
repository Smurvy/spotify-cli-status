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
        return self.data["is_playing"]
