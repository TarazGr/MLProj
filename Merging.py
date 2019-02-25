import matplotlib
import numpy as np
import pandas as pd

spotify = pd.read_csv("spotifyAPIScraping.csv", encoding="latin1", usecols=["Artist", "Followers", "Popularity"],
	names=["Artist", "Gen", "Followers", "Popularity"], header=0, na_values="ND").dropna(how="any")
lastFM = pd.read_csv("lastFMAPIScraping.csv", encoding="latin1", usecols=["Track", "Artist", "Listeners", "Plays", "Duration"],
	names=["Track", "Artist", "Listeners", "Plays", "Duration", "Gen"], header=0, na_values="ND").dropna(how="any")

dataset = pd.merge(spotify, lastFM, on="Artist", how="outer").dropna(how="any")

dataset.to_csv("merged.csv", encoding="latin1", index=False)


spotifyEur = pd.read_csv("spotifyAPIScrapingEUROVISION.csv", encoding="latin1", usecols=["Artist", "Followers", "Popularity"],
	names=["Artist", "Gen", "Followers", "Popularity"], header=0, na_values="ND").dropna(how="all")
lastFMEur = pd.read_csv("lastFMAPIScrapingEUROVISION.csv", encoding="latin1", usecols=["Track", "Artist", "Listeners", "Plays", "Duration"],
	names=["Track", "Artist", "Listeners", "Plays", "Duration", "Gen"], header=0, na_values="ND").dropna(how="all")

datasetEur = pd.merge(spotifyEur, lastFMEur, on="Artist", how="outer")

datasetEur.to_csv("mergedEur.csv", encoding="latin1", index=False)
