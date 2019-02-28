import matplotlib
import numpy as np
import pandas as pd

spotify = pd.read_csv("spotifyAPIScraping.csv", encoding="latin1", header=0,
                      names=["Artist", "Gen", "Followers", "Popularity"],
                      usecols=["Artist", "Followers", "Popularity"],
                      na_values=["ND", 0]).dropna(how="any")
lastFM = pd.read_csv("lastFMAPIScraping.csv", encoding="latin1", header=0,
                     names=["Track", "Artist", "Listeners", "Plays", "Duration", "Gen"],
                     usecols=["Track", "Artist", "Listeners", "Plays", "Duration"],
                     na_values=["ND", 0]).dropna(how="any")

dataset = pd.merge(lastFM, spotify, on="Artist", how="outer").dropna(how="any")

dataset = dataset.drop_duplicates(subset=["Artist", "Track"])

dataset["Winner"] = 0

dataset.to_csv("merged.csv", encoding="latin1", index=False)

spotifyEur = pd.read_csv("spotifyAPIScrapingEUROVISION.csv", encoding="latin1", header=0,
                         names=["Artist", "Gen", "Followers", "Popularity"],
                         usecols=["Artist", "Followers", "Popularity"],
                         na_values="ND").dropna(how="all")
lastFMEur = pd.read_csv("lastFMAPIScrapingEUROVISION.csv", encoding="latin1", header=0,
                        names=["Track", "Artist", "Listeners", "Plays", "Duration", "Gen"],
                        usecols=["Track", "Artist", "Listeners", "Plays", "Duration"],
                        na_values="ND").dropna(how="all")

datasetEur = pd.merge(lastFMEur, spotifyEur, on="Artist", how="outer")

datasetEur["Winner"] = 1

datasetEur.to_csv("mergedEur.csv", encoding="latin1", index=False)

final_data = pd.concat([dataset, datasetEur])

final_data["Duration"] = final_data["Duration"]/1000

final_data.to_csv("dataset.csv", encoding="latin1", index=False)
