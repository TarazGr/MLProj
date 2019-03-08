from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas
import time
import csv


toLookFor = [("Nothing But Thieves", "Excuse Me",0), ("Muse", "Dead Inside",1), ("The Killers", "Run For Cover",0),
("U2","One", 1), ("Linkin Park", "Final Masquerade",0), ("Green Day", "Working Class Hero",1),
("Caparezza","Una Chiave",0), ("Tiziano Ferro", "Sere Nere", 1),("Three Days Grace", "Pain",1),
("Imagine Dragons", "Radioactive",1), ("Imagine Dragons", "Believer",1), ("Katy Perry", "Dark Horse",1),
("Disturbed", "The Sound of Silence",1), ("Coldplay", "Till Kingdom Come",0), ("Francesco Gabbani", "Occidentali's Karma",0),
("All Time Low", "Therapy",0),("The Postal Service", "Such Great Heights",0), ("Artic Monkeys", "Do I Wanna Know?",1),
("Jovanotti", "Welcome",1),("Dark Polo Gang", "Cambiare Adesso",0),("Muse", "Time Is Running Out",1),("Coldplay", "The Scientist",1),
("Guns N' Roses", "Sweet Child O' Mine", 1), ("Oasis", "The Masterplan", 0), ("Metallica", "Enter Sandman",1), ("Nothing But Thieves", "Sorry",1),
("AC/DC", "Highway To Hell",1)
]

client_credentials_manager = SpotifyClientCredentials("75d944d4a2f64af3ada75b8d846451a8",
                                                      "399a7ee3bdc947b799148755314b4753")
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
toSave = []
added = set()
contatore = 0
firstTime = True

for tupla in toLookFor:
    if contatore < 5000:
        artist = tupla[0]
        track = tupla[1]
        results = spotify.search(q='artist:' + artist + " track:" + track, type='track')
        time.sleep(2)
        if results['tracks']['total'] == 0:
            continue
        idTraccia = results['tracks']['items'][0]['id']
        analisiTraccia = spotify.audio_features(idTraccia)
        contatore += 2
        if None in analisiTraccia:
            continue
        toAppend = []
        toAppend.append(track)
        toAppend.append(artist)
        toAppend.append(tupla[2])
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
        with open("./testingDataset.csv", "a", encoding="UTF-8", newline='') as myfile:
            wr = csv.writer(myfile)
            if firstTime:
                wr.writerow(("track", "artist", "billboarder", "danceability", "energy", "loudness", "speechiness",
                             "acousticness", "instrumentalness", "liveness", "key", "mode", "duration"))
                firstTime = False
            try:
                wr.writerows([toAppend])
            except Exception:
                myfile.close()
        added.add(track)
    if contatore >= 5000:
        time.sleep(180)
        contatore = 0
