from flask import Flask, request, render_template
import json
import requests
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sqlite3
from modules.counter import counter
from modules.playcnt import playcount
from modules.date_retrieve import date_retrieve
from modules.urnconv import to_urn
from modules.data_retrieve import data_retrieve
from modules.data_inputter import data_input
from datetime import datetime

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    dates = []
    playcnts = []
    followers = []
    today = datetime.today()
    date = today.strftime('%B %d, %Y')
    text = request.form['songid']
    urn = to_urn(text)
    track = sp.track(urn)
    name = track['artists'][0]['name']
    album_name = track['album']['name']
    song_name = track['name']
    in_db = data_retrieve(song_name)

    if in_db == []:
        print('Could not be found in the database currently')
    else:

        resp = in_db[0]
        dates = date_retrieve(song_name)
        estearn = format(int((resp[0] / 1000) * 3), ',d')
        return render_template('return.html', earnings=estearn,dates=dates,playcount=format(resp[0],',d'), totalplays=format(resp[1],',d'), followers=format(resp[2],',d'), song = resp[3], album = resp[4], artist=resp[5], artistpfp=resp[6], duration=resp[7], rating=resp[8],artistlink=resp[9])
    
    track = sp.track(urn)
    name = track['artists'][0]['name']
    album_name = track['album']['name']
    song_name = track['name']
    artistpfp = track['album']['images'][0]['url']
    popularity = track['popularity']
    song_len = '{0:.2f}'.format(track['duration_ms'] / 60000)
    artist_url = track['artists'][0]['external_urls']['spotify']
    albumid = track['album']['external_urls']['spotify'].split('/')[4]
    artist ='spotify:artist:'+track['artists'][0]['uri']
    albums = sp.artist_albums(artist, album_type='album')
    total_plays = 0
    
    for i in albums['items']:
        album_url = i['external_urls']['spotify']
        album_id = album_url.split('/')[4]
        total_plays += counter(album_id)


    total_plays = format(total_plays, ",d")
    playcnt = format(playcount(albumid, urn), ",d")
    artistsrch = sp.artist(artist)
    followers = format(artistsrch['followers']['total'], ",d")
    estearn = '{0:2f}'.format((playcnt / 1000) * 3)
    data_input(date, urn,playcnt,total_plays,artistsrch['followers']['total'], song_name,album_name, name, artistpfp, song_len, popularity, artist_url)
    return render_template('return.html',earnings=estearn,rating=popularity, artistlink=artist_url, duration=song_len, playcount=playcnt, totalplays=total_plays, followers=followers, song=song_name, album= album_name, artist=name, artistpfp=artistpfp)

if __name__ == "__main__":
    app.run(debug=True, port=3444)