import requests
import json

def load_config(filename='config.json'):
    with open(filename, 'r') as f:
        return json.load(f)

config = load_config()
API_KEY = config.get('API_KEY')
Username = config.get('Username')
period = '1month'


# Construct the URL
url = f"https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={Username}&api_key={API_KEY}&format=json&period={period}"

# Make the request
response = requests.get(url)

data = response.json()

tracks = data.get('toptracks', {}).get('track', [])

for track in tracks:
    name = track.get('name')
    artist = track.get('artist', {}).get('name')
    rank = track.get('rank')
    playcount = track.get('playcount')
    print(f"Name: {name}, artist: {artist}")