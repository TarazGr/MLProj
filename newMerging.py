import pandas as pd 

#Feature Engineering: drop all values with not defined values
data = pd.read_csv('billboard_2000_2018_spotify_lyrics.csv',encoding='latin1', na_values=['unknown', 'NaN']).dropna(how="any")

#now: let's drop the following columns:
#"date","year","title","simple_title","artist","main_artist","peak_pos","last_pos","weeks","rank","change","spotify_link","spotify_id","video_link","genre","broad_genre","analysis_url","lyrics"

whatWillBeConsidered = data[["title","artist","energy","liveness","speechiness","acousticness","instrumentalness","danceability","key","duration_ms","loudness","mode"]]

whatWillBeConsidered['duration_ms'] = whatWillBeConsidered["duration_ms"] / 1000

whatWillBeConsidered['duration'] = whatWillBeConsidered['duration_ms']

whatWillBeConsidered["billboarder"] = 1

whatWillBeConsidered['duration_ms'].drop()

toMerge = pd.read_csv('datasetFINAL.csv', names=["index","track","artist","billboarder","danceability","energy","loudness","speechines","acousticness","instrumentalness","liveness","key","mode","duration"])

toMerge = toMerge[["track","artist","billboarder","danceability","energy","loudness","speechines","acousticness","instrumentalness","liveness","key","mode","duration"]]

#forse usare useCols nel load?