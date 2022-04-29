import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_data():
    scope = "user-read-playback-state"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

    user = sp.current_user_playing_track()

    info = user['item']

    print(info['name'])

    


def main():
    try:
        get_data()
    except Exception as e:
        print(e)
main()