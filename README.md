# spotify-cli-status
gets user data from spotify api and displays it on the terminal

## Prerequisites
 - Spotify developer account with an application created

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running

*** Windows ***
```shell
set SPOTIPY_CLIENT_ID=$YOUR_CLIENT_ID
set SPOTIPY_CLIENT_SECRET=$YOUR_CLIENT_SECRET
set SPOTIPY_REDIRECT_URI=$YOUR_REDIRECT_URI

gunicorn main:app --reload
```
*** Mac ***
```bash
export SPOTIPY_CLIENT_ID=<SPOTIPY_CLIENT_ID>
export SPOTIPY_CLIENT_SECRET=<SPOTIPY_CLIENT_SECRET>
export SPOTIPY_REDIRECT_URI=<SPOTIPY_REDIRECT_URI>

gunicorn main:app --reload
```

