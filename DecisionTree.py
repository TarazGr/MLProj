import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split, KFold

data = pd.read_csv('datasetRidotto.csv', encoding='UTF-8')
features = data[["danceability", "energy", "loudness", "speechiness", "acousticness", "instrumentalness", "liveness",
                 "key", "mode", "duration"]]
target = data["billboarder"]

train_features, test_features, train_target, test_target = train_test_split(features, target)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_features, train_target)
predictions = clf.predict(test_features)

print(confusion_matrix(test_target, predictions))

print(classification_report(test_target, predictions))

# dump(clf, "DTree_Model.joblib")

# DTree k-fold cross-validation

fold = KFold(100, True)

scores = []
for train_index, test_index in fold.split(data):
    train_set = data.iloc[train_index]
    test_set = data.iloc[test_index]
    train_features = train_set[["danceability", "energy", "loudness", "speechiness", "acousticness",
                                "instrumentalness", "liveness", "key", "mode", "duration"]]
    test_features = test_set[["danceability", "energy", "loudness", "speechiness", "acousticness",
                              "instrumentalness", "liveness", "key", "mode", "duration"]]
    train_target = train_set["billboarder"]
    test_target = test_set["billboarder"]

    clf = tree.DecisionTreeClassifier()
    clf.fit(train_features, train_target)
    predictions = clf.predict(test_features)
    scores.append(accuracy_score(test_target, predictions))

print("best: " + str(np.max(scores)), " average: " + str(np.mean(scores)) + " worst: " + str(np.min(scores)))
