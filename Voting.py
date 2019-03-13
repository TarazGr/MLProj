import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, KFold
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
data = pd.read_csv('/Users/gimmi/Desktop/Progetto ML/datasetRidotto.csv')
clf1 = LogisticRegression(solver='lbfgs', multi_class='multinomial',random_state=1)
clf2 = RandomForestClassifier(n_estimators=50, random_state=1)
clf3 = GaussianNB()
features = data[["danceability", "energy", "loudness", "speechiness", "acousticness", "instrumentalness", "liveness","key", "mode", "duration", "followers","popularity"]]
target = data["billboarder"]
train_features, test_features, train_target, test_target = train_test_split(features, target)
eclf1 = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)], voting='hard')
eclf1 = eclf1.fit(train_features,train_target)
print(eclf1.predict(test_features))
eclf2 = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)],voting='soft')
eclf2 = eclf2.fit(train_features,train_target)
print(eclf2.predict(test_features))
eclf3 = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)],voting='soft', weights=[2,1,1],flatten_transform=True)
eclf3 = eclf3.fit(train_features,train_target)
print(eclf3.predict(test_features))
print(eclf3.transform(test_features).shape)
for clf, label in zip([clf1, clf2, clf3, eclf3], ['Logistic Regression', 'Random Forest', 'naive Bayes', 'Ensemble']):
    scores = cross_val_score(clf, train_features, train_target, cv=5, scoring='accuracy')
    print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))