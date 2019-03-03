import matplotlib
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, RobustScaler
import matplotlib.pyplot as plt

data = pd.read_csv("datasetFINAL.csv", encoding="latin1", header=0)

features = data[["listeners", "playcount", "duration", "followers", "popularity"]]
target = data["Winner"]

scaler = RobustScaler()

train_features, test_features, train_target, test_target = train_test_split(features, target)

scaler.fit(train_features)

train_features = scaler.transform(train_features)
test_features = scaler.transform(test_features)

clf = MLPClassifier(hidden_layer_sizes=(13,13,13), verbose=True)
clf = clf.fit(train_features, train_target)

predictions = clf.predict(test_features)

print(confusion_matrix(test_target, predictions))

print(classification_report(test_target, predictions))

print("--------------------------------------------------------------------")

from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators=20)
forest = forest.fit(train_features,train_target)
predictioni = forest.predict(test_features)

print(confusion_matrix(test_target, predictioni))

print(classification_report(test_target, predictioni))

datiTesting = pd.read_csv("mergedEur2018.csv", encoding="latin1", header=0)
oggetto = datiTesting[["listeners", "playcount", "duration", "followers", "popularity"]]

predizioni = forest.predict(oggetto)
print("ciao")