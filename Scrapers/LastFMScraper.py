import requests
import json
import pandas
import time
import csv

trackTitles = pandas.read_csv("/Users/gimmi/Desktop/Progetto ML/tracklistEUROVISION.csv", encoding='latin1')['Track']
artistNames = pandas.read_csv("/Users/gimmi/Desktop/Progetto ML/tracklistEUROVISION.csv", encoding='latin1')['Artist']
toSave = []
contatore = 0
firstTime = True

for i in range(0, len(trackTitles)):
    if contatore < 5000:
        richiesta = requests.get("http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=007bb7dc4b7d8eef22dddd17427dc720&artist={artista}&track={traccia}&format=json".format(
            artista = artistNames[i],
            traccia = trackTitles[i]
            ))
        time.sleep(2)
        try:
            answer = json.loads(richiesta.text)
        except Exception:
            print("HO SALTATO " + str(artistNames[i]) + " - " + str(trackTitles[i]) + " PER ECCEZIONE")
            continue
        print('error' in answer)
        if richiesta.status_code == 200 and not ('error' in answer and answer['error'] == 6):
            contatore += 1
            #DO SOME LOGIC HERE
            durata = answer['track']['duration'] if 'duration' in answer['track'] else 0
            genre = answer['track']['toptags']['tag'][0]['name'] if len(answer['track']['toptags']['tag']) > 0 else "ND"
            toAppend = [trackTitles[i], artistNames[i], answer['track']['listeners'], answer['track']['playcount'],durata, genre]
            with open("/Users/gimmi/Desktop/Progetto ML/lastFMScrapingEUR.csv", "a", encoding="UTF-8", newline='') as myfile:
                wr = csv.writer(myfile)
                if firstTime:
                    wr.writerow(("track", "artist", "listeners", "playcount", "duration", "genre"))
                    firstTime = False
                wr.writerows([toAppend])
            myfile.close()
        else:
            print("HO SALTATO " + str(trackTitles[i]) + " di "  + str(artistNames[i]) + " ALL'INDICE " + str(i))
    else:
        time.sleep(180)
        contatore = 0