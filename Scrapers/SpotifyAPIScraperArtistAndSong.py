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


artistNames = pandas.read_csv("/Users/gimmi/Desktop/Progetto ML/top5000songs-2-8-0023.csv", encoding = 'UTF-8')['artist']
trackNames = pandas.read_csv("/Users/gimmi/Desktop/Progetto ML/top5000songs-2-8-0023.csv", encoding = 'UTF-8')['name']

client_credentials_manager = SpotifyClientCredentials("75d944d4a2f64af3ada75b8d846451a8","399a7ee3bdc947b799148755314b4753")
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
toSave = []
added = set()
contatore = 0
firstTime = False
righe = 16045

for i in range(0, len(artistNames)):
    print("Iterazione su " + str(artistNames[i]))
    if contatore < 5000 and artistNames[i] and not trackNames[i] in added:
        toFind = splitterFunction(artistNames[i])
        results = spotify.search(q='artist:' + toFind +" track:" +trackNames[i], type='track')
        time.sleep(2)
        if results['tracks']['total'] == 0:
            print("Non ho trovato nulla per " + str(artistNames[i]))
            continue
        idTraccia = results['tracks']['items'][0]['id']
        analisiTraccia = spotify.audio_features(idTraccia)
        contatore += 2
        if None in analisiTraccia:
            print("ANALISI NON DISPONIBILI PER " + str(trackNames[i])  + " DI " + str(artistNames[i]))
            continue
        toAppend = []
        toAppend.append(righe)
        righe += 1
        toAppend.append(trackNames[i])
        toAppend.append(artistNames[i])
        toAppend.append(0)
        toAppend.append(analisiTraccia[0]['danceability'])
        toAppend.append(analisiTraccia[0]['energy'])
        toAppend.append(analisiTraccia[0]['loudness'])
        toAppend.append(analisiTraccia[0]['speechiness'])
        toAppend.append(analisiTraccia[0]['acousticness'])
        toAppend.append(analisiTraccia[0]['instrumentalness'])
        toAppend.append(analisiTraccia[0]['liveness'])
        toAppend.append(analisiTraccia[0]['key'])
        toAppend.append(analisiTraccia[0]['mode'])
        toAppend.append(analisiTraccia[0]['duration_ms']/1000)
        with open("/Users/gimmi/Desktop/Progetto ML/datasetFINAL.csv", "a", encoding="UTF-8", newline='') as myfile:
            wr = csv.writer(myfile)
            if firstTime:
                wr.writerow(("track","artist","winner","danceability","energy","loudness","speechiness","acousticness","instrumentalness","liveness","key","mode","duration"))
                firstTime = False
            try:
                wr.writerows([toAppend])
            except Exception:
                print("Ciao")
            myfile.close()
        print("Aggiunto con successo " + str(artistNames[i]))
        added.add(trackNames[i])
    if contatore >= 5000:
        time.sleep(180)
        contatore = 0