from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import requests
import pandas
import time
import csv


def splitterFunction(artista):
    if "featuring" in artista.lower():
        toReturn = artista.lower().split("featuring")
        return toReturn[0].strip()
    if "feature" in artista.lower():
        toReturn = artista.lower().split("feature")
        return toReturn[0].strip()
    if "&" in artista.lower():
        toReturn = artista.lower().split("&")
        return toReturn[0].strip()
    return artista

artistNames = pandas.read_csv("/Users/gimmi/Desktop/Progetto ML/tracklist.csv", encoding = 'latin1')['artist']
previouslySeen = pandas.read_csv("/Users/gimmi/Desktop/Progetto ML/spotifyAPIScraping.csv", encoding='latin1')['artist'].values.tolist()
client_credentials_manager = SpotifyClientCredentials("75d944d4a2f64af3ada75b8d846451a8","399a7ee3bdc947b799148755314b4753")
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
toSave = []
added = set()
contatore = 0
firstTime = True

for i in range(0, len(artistNames)):
    print("Iterazione su " + str(artistNames[i]))
    if contatore < 5000 and artistNames[i] and not artistNames[i] in added and artistNames[i] not in previouslySeen:
        toFind = splitterFunction(artistNames[i])
        results = spotify.search(q='artist:' + toFind, type='artist')
        time.sleep(2)
        if results['artists']['total'] == 0:
            print("Non ho trovato nulla per " + str(artistNames[i]))
            continue
        idArtista = results['artists']['items'][0]['id']
        artista = spotify.artist(idArtista)
        time.sleep(2)
        generi = ' '.join(artista['genres'])
        seguaci = artista['followers']['total']
        popularity = artista['popularity']
        name = artista['name']
        toAppend = [name, generi, seguaci, popularity]
        contatore +=1
        with open("/Users/gimmi/Desktop/Progetto ML/spotifyAPIScraping.csv", "a", encoding="ISO-8859-1", newline='') as myfile:
            wr = csv.writer(myfile)
            if firstTime:
                wr.writerow(("artist", "genres", "followers", "popularity"))
                firstTime = False
            try:
                wr.writerows([toAppend])
            except Exception:
                print("Ciao")
            myfile.close()
        print("Aggiunto con successo " + str(artistNames[i]))
        added.add(artistNames[i])
    if contatore >= 5000:
        time.sleep(180)
        contatore = 0