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
df = pandas.read_csv('final_training_dataset_with_output_presets_317.csv')
#print()
#Input array
X=np.array(df[['Avg.PCC','Avg.Motion..','Scene.Count','Frames.per.Second','Original.Bitrate','Width','Height']])

#Output ,'Average Intensity'
y=np.squeeze(np.array(df[['Compression.Preset']]))
#X = np.random.randint(1,10,size = (100,8))
#y = np.random.choice([0,1],size = (100))
#print(X)
#print(y.shape)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(10,5,5,5,6), random_state=1)

clf.fit(X_train, y_train)

y_pred_t = clf.predict(X_train)

#print(X)
print(y_train)
print(train_error)


y_pred = clf.predict(X_test)
print(y_pred)
#confusion_matric2 = confusion_matrix(y_test, y_pred, binary=False)

#fig, ax = plot_confusion_matrix(conf_mat=confusion_matric2)
#plt.show()
test_error = np.mean(np.equal(y_test,y_pred))
print(test_error)

'''
import numpy as np
import itertools 
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
#from mlxtend.evaluate import confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
#from mlxtend.plotting import plot_confusion_matrix
import matplotlib.pyplot as plt
import pandas

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

df = pandas.read_csv('dataset_317_2class.csv')
#print()
#Input array
X=np.array(df[['Avg.PCC','Avg.Motion..','Scene.Count','Frames.per.Second','Original.Bitrate','Width','Height']])
#X=np.array(df[['Avg.PCC','Avg.Motion..','Original.Bitrate']])
#Output ,'Average Intensity' 40 2 0.15/65 2 0.20/
y=np.squeeze(np.array(df[['Compression.Preset']]))
#X = np.random.randint(1,10,size = (100,8))
#y = np.random.choice([0,1],size = (100))
#print(X)
#print(y.shape)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)


#clf = RandomForestClassifier(n_estimators=65, max_depth = 7, random_state=0)
clf = GradientBoostingClassifier(n_estimators=35, max_depth = 4, random_state=0)

clf.fit(X_train, y_train)

y_pred_t = clf.predict(X_train)

#confusion_matric = confusion_matrix(y_train, y_pred_t, binary=False)
confusion_matric = confusion_matrix(y_train, y_pred_t, labels=['veryfast', 'faster','fast', 'medium', 'slow', 'slower'])
np.set_printoptions(precision=2)

plt.figure()
plot_confusion_matrix(confusion_matric, classes=['veryfast', 'faster','fast', 'medium', 'slow', 'slower'],
                      title='Confusion matrix')
train_error = np.mean(np.equal(y_train,y_pred_t))
#print(y_test)
print(train_error)


y_pred = clf.predict(X_test)
#print(y_pred)
confusion_matric2 = confusion_matrix(y_test, y_pred, labels=['veryfast', 'faster','fast', 'medium', 'slow', 'slower'])
plt.figure()
plot_confusion_matrix(confusion_matric2, classes=['veryfast', 'faster','fast', 'medium', 'slow', 'slower'],
                      title='Confusion matrix')
test_error = np.mean(np.equal(y_test,y_pred))
print(test_error)

print(precision_recall_fscore_support(y_train, y_pred_t, average='weighted'))

print(precision_recall_fscore_support(y_test, y_pred, average='weighted'))


