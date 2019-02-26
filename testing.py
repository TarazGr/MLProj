from sklearn.tree import DecisionTreeClassifier
import math
import numpy as np
import pandas as pd


def nd_checker(value):
    to_check = [3, 4, 5, 6, 7]
    for number in to_check:
        if value[number] is None or value[number] == "ND":
            return True
    return False


def nan_checker(value):
    to_check = [3, 4, 5, 6, 7]
    for number in to_check:
        if math.isnan(float(value[number])) or float(value[number]) is None:
            return True
    return False


trainingSet = []
testSet = []
dt = pd.read_csv('merged.csv', header=0)
dtEur = pd.read_csv('mergedEur.csv', header=0)

for i, row in enumerate(dt.itertuples()):
    toAppend = [float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7])]
    trainingSet.append(toAppend)
    testSet.append(row[8])

for i, row in enumerate(dtEur.itertuples()):
    toAppend = [float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7])]
    trainingSet.append(toAppend)
    testSet.append(float(row[8]))
x = len(testSet)
y = len(trainingSet)
clf = DecisionTreeClassifier()


clf.fit(trainingSet, testSet)
test = [31295.0, 54.0, 23700.0, 219700.0, 247000.0]
risultato = clf.predict([test])
print("e quindi")
