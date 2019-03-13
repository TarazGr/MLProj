import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split, KFold
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("scaled.csv", header=0)

positives = df[df["billboarder"] == 1]
negatives = df[df["billboarder"] == 0]

less = positives.sample(len(negatives))

df = pd.concat([less, negatives])

target = df["billboarder"]
features = df.drop(columns="billboarder")

train_features, test_features, train_target, test_target = train_test_split(features, target)

clf = KNeighborsClassifier(10).fit(train_features, train_target)
predictions = clf.predict(test_features)

print(confusion_matrix(test_target, predictions))

print(classification_report(test_target, predictions))

fold = KFold(100, True)

scores = []
for train_index, test_index in fold.split(df):
    train_set = df.iloc[train_index]
    test_set = df.iloc[test_index]
    train_target = train_set["billboarder"]
    test_target = test_set["billboarder"]
    train_features = train_set.drop(columns="billboarder")
    test_features = test_set.drop(columns="billboarder")

    clf = KNeighborsClassifier().fit(train_features, train_target)
    predictions = clf.predict(test_features)
    scores.append(accuracy_score(test_target, predictions))

print("best: " + str(np.max(scores)), " average: " + str(np.mean(scores)) + " worst: " + str(np.min(scores)))
