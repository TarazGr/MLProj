import matplotlib
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, RobustScaler
import matplotlib.pyplot as plt

data = pd.read_csv("dataset.csv", encoding="latin1", header=0)

features = data[["Listeners", "Plays", "Duration", "Followers", "Popularity"]]
target = data["Winner"]

scaler = RobustScaler()

train_features, test_features, train_target, test_target = train_test_split(features, target)

scaler.fit(train_features)

train_features = scaler.transform(train_features)
test_features = scaler.transform(test_features)

clf = MLPClassifier(hidden_layer_sizes=(20, 400, 80000), max_iter=999999999, verbose=True)
clf.fit(train_features, train_target)

predictions = clf.predict(test_features)

print(confusion_matrix(test_target, predictions))

print(classification_report(test_target, predictions))
