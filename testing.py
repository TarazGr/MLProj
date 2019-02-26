from sklearn.tree import DecisionTreeClassifier
import math
import numpy as np

def NDChecker(value):
    toCheck = [3,4,6,7,8]
    for number in toCheck:
        if value[number] is None or value[number] == "ND":
            return True
    return False

def nanchecker(value):
    toCheck = [3,4,6,7,8]
    for number in toCheck:
        if math.isnan(float(value[number])) or float(value[number]) is None:
            return True
    return False

import pandas as pd

trainingSet = []
testSet = []
dt = pd.read_csv('C:\\Users\\Gianmarco\\Desktop\\MLProj\\merged.csv', header=None)
dtEur = pd.read_csv('C:\\Users\\Gianmarco\\Desktop\\MLProj\\mergedEur.csv', header=None)

for row in dt.itertuples():
    if row[3] == 'Followers' or row[3] == 'followers':
        continue
    if NDChecker(row):
        continue
    toAppend = [float(row[3]), float(row[4]), float(row[6]), float(row[7]), float(row[8])]
    trainingSet.append(toAppend)
    testSet.append(row[9])

for row in dtEur.itertuples():
    if row[3] == 'Followers' or row[3] == 'followers':
        continue
    toAppend = [float(row[3]), float(row[4]), float(row[6]), float(row[7]), float(row[8])]
    trainingSet.append(toAppend)
    testSet.append(float(row[9]))
x = len(testSet)
y = len(trainingSet)
clf = DecisionTreeClassifier()


clf.fit(trainingSet,testSet)
test = [31295.0,54.0,23700.0,219700.0,247000.0]
risultato = clf.predict([test])
print("e quindi")