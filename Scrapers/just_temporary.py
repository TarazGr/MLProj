import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("SUPERTEST.csv", encoding="latin1", header=None,
                 names=["acousticness", "artist", "billboarder", "danceability", "duration", "energy",
                        "instrumentalness", "key", "liveness", "loudness", "mode", "speechiness", "title",
                        "followers", "popularity"],
                 usecols=["acousticness", "billboarder", "danceability", "duration", "energy", "instrumentalness",
                          "key", "liveness", "loudness", "mode", "speechiness", "followers", "popularity"])

to_scale = df[["loudness", "followers", "popularity"]]

scaled = MinMaxScaler().fit_transform(to_scale)

df["loudness"] = scaled[:, 0]
df["followers"] = scaled[:, 1]
df["popularity"] = scaled[:, 2]



df.to_csv("../scaled.csv", index=False, encoding="latin1")
