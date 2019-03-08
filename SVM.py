import matplotlib
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from joblib import dump, load
from sklearn import svm

data = pd.read_csv("datasetRidotto.csv", encoding="latin1", header=0)

features = data[["danceability", "energy", "loudness", "speechiness", "acousticness", "instrumentalness", "liveness",
                 "key", "mode", "duration"]]
target = data["billboarder"]
clf = svm.SVC(gamma='scale')

scaler = RobustScaler()

train_features, test_features, train_target, test_target = train_test_split(features, target)

scaler.fit(train_features)

train_features = scaler.transform(train_features)
test_features = scaler.transform(test_features)

clf = clf.fit(train_features, train_target)

predictions = clf.predict(test_features)

print(confusion_matrix(test_target, predictions))

print(classification_report(test_target, predictions))
