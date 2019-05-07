# -*- coding: utf-8 -*-
"""NN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19TGIaFZY1x3qabN-6fBMrDYv2en0FtP5
"""
'''
import sklearn
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

import pandas
df = pandas.read_csv('dataset with replication.csv')
#print()
#Input array
X_train=np.array(df[['Avg.PCC','Avg.Motion..','Scene.Count','Frames.per.Second','Original.Bitrate','Width','Height']])

#Output ,'Average Intensity'
y_train=np.squeeze(np.array(df[['Compression.Preset']]))
#X = np.random.randint(1,10,size = (100,8))
#y = np.random.choice([0,1],size = (100))
#print(X)
#print(y.shape)
#X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)
df1 = pandas.read_csv('testing.csv')

X_test=np.array(df1[['Avg.PCC','Avg.Motion..','Scene.Count','Frames.per.Second','Original.Bitrate','Width','Height']])

y_test=np.squeeze(np.array(df1[['Compression.Preset']]))

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(10,5,5,5,6), random_state=0)

clf.fit(X_train, y_train)

y_pred_t = clf.predict(X_train)

#print(X)


#confusion_matric = confusion_matrix(y_train, y_pred_t, binary=False)
#fig, ax = plot_confusion_matrix(conf_mat=confusion_matric)
#plt.show()
train_error = np.mean(np.equal(y_train,y_pred_t))





y_pred = clf.predict(X_test)
print(y_test+" : "+y_pred)
#confusion_matric2 = confusion_matrix(y_test, y_pred, binary=False)

#fig, ax = plot_confusion_matrix(conf_mat=confusion_matric2)
#plt.show()

test_error = np.mean(np.equal(y_test,y_pred))
print("Training accuracy ")
print(train_error)
print("Testing accuracy ")
print(test_error)

'''
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
#from mlxtend.evaluate import confusion_matrix
#from mlxtend.plotting import plot_confusion_matrix
import matplotlib.pyplot as plt

import pandas
df = pandas.read_csv('dataset with replication.csv')
#print()
#Input array
X_train=np.array(df[['Avg.PCC','Avg.Motion..','Scene.Count','Frames.per.Second','Original.Bitrate','Width','Height']])
#X=np.array(df[['Avg.PCC','Avg.Motion..','Original.Bitrate']])
#Output ,'Average Intensity' 40 2 0.15/65 2 0.20/
y_train=np.squeeze(np.array(df[['Compression.Preset']]))

df1 = pandas.read_csv('testing.csv')

X_test=np.array(df1[['Avg.PCC','Avg.Motion..','Scene.Count','Frames.per.Second','Original.Bitrate','Width','Height']])

y_test=np.squeeze(np.array(df1[['Compression.Preset']]))

#X = np.random.randint(1,10,size = (100,8))
#y = np.random.choice([0,1],size = (100))
#print(X)
#print(y.shape)
#X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)


clf = RandomForestClassifier(n_estimators=50, max_depth = 6, random_state=0)
n_estimators=50
max_depth=6
#clf = GradientBoostingClassifier(n_estimators=50, max_depth = 3, random_state=1)

clf.fit(X_train, y_train)

y_pred_t = clf.predict(X_train)

#confusion_matric = confusion_matrix(y_train, y_pred_t, binary=False)
#fig, ax = plot_confusion_matrix(conf_mat=confusion_matric)
#plt.show()
train_error = np.mean(np.equal(y_train,y_pred_t))





y_pred = clf.predict(X_test)
print(y_test+" : "+y_pred)
#confusion_matric2 = confusion_matrix(y_test, y_pred, binary=False)

#fig, ax = plot_confusion_matrix(conf_mat=confusion_matric2)
#plt.show()

print("Estimators")
print(n_estimators)
print("Max depth of tree")
print(max_depth)
test_error = np.mean(np.equal(y_test,y_pred))
print("Training accuracy ")
print(train_error)
print("Testing accuracy ")
print(test_error)

