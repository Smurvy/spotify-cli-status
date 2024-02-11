import os 

client_id = input"Enter your spotify client ID: ")
client_secret = input("Enter your spotify client secret: ")
redirect_uri = input("Enter your spotify redirect URI: ")

if platform.system() == "Darwin":
    os.execute(f"export SPOTIPY_CLIENT_ID={client_id}")
    os.execute(f"export SPOTIPY_CLIENT_SECRET={client_secret}")
    os.execute(f"export SPOTIPY_REDIRECT_URI={redirect_uri}")

else:
    os.execute(f"set SPOTIPY_CLIENT_ID={client_id}")
    os.execute(f"set SPOTIPY_CLIENT_SECRET={client_secret}")
    os.execute(f"set SPOTIPY_REDIRECT_URI={redirect_uri}")
   
