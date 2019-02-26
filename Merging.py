import matplotlib
import numpy as np
import pandas as pd

spotify = pd.read_csv("spotifyAPIScraping.csv", encoding="latin1", header=0,
                      names=["Artist", "Gen", "Followers", "Popularity"],
                      usecols=["Artist", "Followers", "Popularity"],
                      na_values="ND").dropna(how="any")
lastFM = pd.read_csv("lastFMAPIScraping.csv", encoding="latin1", header=0,
                     names=["Track", "Artist", "Listeners", "Plays", "Duration", "Gen"],
                     usecols=["Track", "Artist", "Listeners", "Plays", "Duration"],
                     na_values="ND").dropna(how="any")

dataset = pd.merge(spotify, lastFM, on="Artist", how="outer").dropna(how="any")

dataset.to_csv("merged.csv", encoding="latin1", index=False)

spotifyEur = pd.read_csv("spotifyAPIScrapingEUROVISION.csv", encoding="latin1", header=0,
                         names=["Artist", "Gen", "Followers", "Popularity"],
                         usecols=["Artist", "Followers", "Popularity"],
                         na_values="ND").dropna(how="all")
lastFMEur = pd.read_csv("lastFMAPIScrapingEUROVISION.csv", encoding="latin1", header=0,
                        names=["Track", "Artist", "Listeners", "Plays", "Duration", "Gen"],
                        usecols=["Track", "Artist", "Listeners", "Plays", "Duration"],
                        na_values="ND").dropna(how="all")

datasetEur = pd.merge(spotifyEur, lastFMEur, on="Artist", how="outer")

datasetEur.to_csv("mergedEur.csv", encoding="latin1", index=False)
