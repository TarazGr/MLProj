from sklearn import tree
import matplotlib
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn import svm
import matplotlib.pyplot as plt
# import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\Graphviz2.38\\bin\\'

train_set = pd.read_csv("dataset.csv", encoding="latin1", header=0)

train_set["Popularity"].apply(lambda x: 1 if x > 70 else 0)

test_set = pd.read_csv("mergedEur2018.csv", encoding="latin1", header=0,
                       names=["Track", "Artist", "Listeners", "Plays", "Duration", "Followers", "Popularity"],
                       usecols=["Track", "Artist", "Listeners", "Plays", "Duration", "Followers", "Popularity"])

test_set["Popularity"].apply(lambda x: 1 if x > 70 else 0)

testing = {}
for index, row in enumerate(test_set.values):
    testing[row[0], row[1]] = [row[2], row[3], row[4], row[5], row[6]]

target = train_set["Winner"]
features = train_set[["Listeners", "Plays", "Duration", "Followers", "Popularity"]]

clf = MLPClassifier(max_iter=100000)
clf.fit(features, target)

true = []
pred = []
for k, v in testing.items():
    print(k, clf.predict([v]))
    pred.append(clf.predict([v])[0])
    true.append(1 if k == ('Toy', 'Netta') else 0)
print(confusion_matrix(true, pred))
