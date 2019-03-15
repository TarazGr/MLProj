from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas
import time
import csv

def splitter_function(artista):
    if "featuring" in artista.lower():
        to_return = artista.lower().split("featuring")
        return to_return[0].strip()
    if "feature" in artista.lower():
        to_return = artista.lower().split("feature")
        return to_return[0].strip()
    if "&" in artista.lower():
        to_return = artista.lower().split("&")
        return to_return[0].strip()
    return artista


data = pandas.read_csv("/Users/gimmi/Desktop/Progetto ML/datasetRidottoInterpolated.csv", encoding='UTF-8')


client_credentials_manager = SpotifyClientCredentials("75d944d4a2f64af3ada75b8d846451a8",
                                                      "399a7ee3bdc947b799148755314b4753")
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
toSave = []
added = set()
contatore = 0
firstTime = False

for row in data.itertuples():
    if contatore < 5000:
        toFind = splitter_function(row.artist)
        track = row.title
        results = spotify.search(q='artist:' + toFind + " track:" + track, type='track')
        time.sleep(2)
        if results['tracks']['total'] == 0:
            continue
        idArtista = results['tracks']['items'][0]['album']['artists'][0]['id']
        artista = spotify.artist(idArtista)
        contatore += 2
        if None in artista:
            continue
        toAppend = []

        toAppend.append(row.acousticness)
        toAppend.append(row.artist)
        toAppend.append(row.billboarder)
        toAppend.append(row.danceability)
        toAppend.append(row.duration)
        toAppend.append(row.energy)
        toAppend.append(row.instrumentalness)
        toAppend.append(row.key)
        toAppend.append(row.liveness)
        toAppend.append(row.loudness)
        toAppend.append(row.mode)
        toAppend.append(row.speechiness)
        toAppend.append(row.title)
        toAppend.append(artista['followers']['total'])
        toAppend.append(artista['popularity'])
        with open("/Users/gimmi/Desktop/Progetto ML/datasetRidottoInterpolated2.csv", "a", encoding="UTF-8", newline='') as myfile:
            wr = csv.writer(myfile)
            if firstTime:
                wr.writerow(("track", "artist", "winner", "danceability", "energy", "loudness", "speechiness",
                             "acousticness", "instrumentalness", "liveness", "key", "mode", "duration"))
                firstTime = False
            try:
                wr.writerows([toAppend])
            except Exception:
                print("Ciao")
            myfile.close()
    if contatore >= 5000:
        time.sleep(180)
        contatore = 0
