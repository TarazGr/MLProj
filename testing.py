from sklearn.tree import DecisionTreeClassifier
import math
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import tree
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB


def nd_checker(value):
    to_check = [3, 4, 5, 6]
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
dt = pd.read_csv('mergedBillboardAndScraping.csv', header=0)

dtEur = pd.read_csv('mergedEurWinners.csv', header=0)

for i, row in enumerate(dt.itertuples()):
    if row[3] == 'Followers' or row[3] == 'followers' or nd_checker(row):
        continue
    toAppend = [float(row[3]), float(row[4]), float(row[5]), float(row[6])]
    trainingSet.append(toAppend)
    testSet.append(row[7])

for i, row in enumerate(dtEur.itertuples()):
    if row[3] == 'Followers' or row[3] == 'followers' or i == 1:
        continue
    toAppend = [float(row[3]), float(row[4]), float(row[5]), float(row[6])]
    trainingSet.append(toAppend)
    testSet.append(float(row[7]))
x = len(testSet)
y = len(trainingSet)
clf = GaussianNB()
clf.fit(trainingSet,testSet)
score = clf.score(trainingSet,testSet)

newTesting = pd.read_csv("mergedEur2018.csv")
newTesting = newTesting.drop('listeners',1)
dicArtisti = {}
for i, row in enumerate(newTesting.itertuples()):
    if row[3] == 'Followers' or row[3] == 'followers' or nd_checker(row):
        continue
    toAppend = [float(row[3]), float(row[4]), float(row[5]), float(row[6])]
    dicArtisti[row[2]] = toAppend
    
for key in dicArtisti:
    print(str(key) + " risulta che .... " + np.array2string(clf.predict([dicArtisti[key]])) +" eurovision 2018")
print("ciao")
stima = clf.densify()
plt.plot(trainingSet, testSet, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()



test2017 = [142900.0,21100.0,180.0,62405.0,45.0]
test2018 = [219000.0,23600.0,372.0,31179.0,54.0]
risultato = clf.predict([test2018])
risultatoOne = clf.predict([test2017])

clf = MLPClassifier()
clf.fit(trainingSet,testSet)
test2017 = [142900.0,21100.0,180.0,62405.0,45.0]
test2018Second = [24233.0,308732.0,183.0,37065.0,58.0]
test2018 = [219000.0,23600.0,372.0,31179.0,54.0]
test2015 = [672900.0,82100.0,190.0,106829.0,55.0]
test2014 = [314200.0,31800.0,183.0,33123.0,42.0]
test2018Third = [678.0,6400.0,184.0,4236.0,40.0]
risultato = clf.predict([test2018])
risultatoOne = clf.predict([test2017])
risultatoThree = clf.predict([test2015])
risultatoFour = clf.predict([test2014])

print("e quindi")
 #------------------------------
 #Nuovo testing