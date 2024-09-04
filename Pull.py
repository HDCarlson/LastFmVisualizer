import requests
import json

def TopTracks(API_KEY, Username, period):
    #Construct the URL
    url = f"https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={Username}&api_key={API_KEY}&format=json&period={period}"
    # Make the request
    response = requests.get(url)

    data = response.json()

    tracks = data.get('toptracks', {}).get('track', [])

    #print(data)

    for track in tracks:
        name = track.get('name')
        artist = track.get('artist', {}).get('name')
        rank = track.get('rank')
        playcount = track.get('playcount')
        print(f"Name: {name}, artist: {artist}")

def TopArtists(API_KEY, Username, period):
    url = f"https://ws.audioscrobbler.com//2.0/?method=user.gettopartists&user={Username}&api_key={API_KEY}&period={period}&format=json"
    response = requests.get(url)
    data = response.json()
    artists = data.get('topartists', {}).get('artist', [])

    for artist in artists:
        name = artist.get('name')
        playcount = artist.get('playcount')
        print(f"artist: {name} - playcount: {playcount}")

def RecentTracks(API_KEY, Username, start, end):
        url = f"https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={Username}&api_key={API_KEY}&from={start}&to={end}&format=json"
        response = requests.get(url)
        data = response.json()
        PageNum = data.get('recenttracks', {}).get('@attr', {}).get('totalPages')
        PageNum = int(PageNum)
        for Page in range(PageNum):
            url = f"https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={Username}&api_key={API_KEY}&from={start}&to={end}&page={Page}&format=json"
            response = requests.get(url)
            data = response.json()
            RecentTracks = data.get('recenttracks', {}).get('track', [])
            for track in RecentTracks:
                name = track.get('name')
                artist = track.get('artist').get('#text')
                print(f"name: {name} - artist: {artist}")