import matplotlib
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\Graphviz2.38\\bin\\'

data = pd.read_csv("dataset.csv", encoding="latin1", header=0)

# data["Popularity"].apply(lambda x: 1 if x > 70 else 0)

features = data[["Listeners", "Plays", "Duration", "Followers", "Popularity"]]
target = data["Winner"]

train_features, test_features, train_target, test_target = train_test_split(features, target)

clf = tree.DecisionTreeClassifier()
clf.fit(train_features, train_target)

predictions = clf.predict(test_features)

print(confusion_matrix(test_target, predictions))

print(classification_report(test_target, predictions))
