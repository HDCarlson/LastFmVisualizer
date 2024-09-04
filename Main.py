import Pull
import Pipeline
import json


def load_config(filename='config.json'):
    with open(filename, 'r') as f:
        return json.load(f)

config = load_config()
API_KEY = config.get('API_KEY')
Username = config.get('Username')
start = 1722484800 #aug 1
end = start + 604800 #add a week to start
end = start + 2628288 #add a month

Pull.RecentTracks(API_KEY, Username, start, end)

