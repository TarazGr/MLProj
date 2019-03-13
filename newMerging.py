import pandas as pd 

# Feature Engineering: drop all values with not defined values
data = pd.read_csv('billboard_2000_2018_spotify_lyrics.csv', encoding='latin1', na_values=['unknown', 'NaN'],
                   header=0).dropna(how="any")

# now: let's drop the following columns:
# "date","year","title","simple_title","artist","main_artist","peak_pos","last_pos","weeks","rank","change",
# "spotify_link","spotify_id","video_link","genre","broad_genre","analysis_url","lyrics"

whatWillBeConsidered = data[["title", "artist", "energy", "liveness", "speechiness", "acousticness",
                             "instrumentalness", "danceability", "key", "duration_ms", "loudness", "mode"]]

whatWillBeConsidered['duration'] = whatWillBeConsidered['duration_ms']/1000

whatWillBeConsidered["billboarder"] = 1

whatWillBeConsidered = whatWillBeConsidered.drop("duration_ms", axis=1)

toMerge = pd.read_csv('datasetFINAL.csv', header=0, names=["index", "title", "artist", "billboarder", "danceability",
                                                           "energy", "loudness", "speechiness", "acousticness",
                                                           "instrumentalness", "liveness", "key", "mode", "duration"])

toMerge = toMerge[["title", "artist", "billboarder", "danceability", "energy", "loudness", "speechiness",
                   "acousticness", "instrumentalness", "liveness", "key", "mode", "duration"]]

dataset = pd.concat([toMerge, whatWillBeConsidered], sort=True).drop_duplicates(["artist", "title"])

dataset.to_csv("Brand New Dataset.csv", encoding="latin1", index=False)
