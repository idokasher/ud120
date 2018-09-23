#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from utils import execute


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = execute(lambda : preprocess(), "Process data")




#########################################################
### your code goes here ###
# Imports
from sklearn.naive_bayes import GaussianNB

# Visualize data


# Create classifier
clf = GaussianNB()

# Train
execute(lambda : clf.fit(features_train, labels_train), "Training time")

# Predict
pred = execute(lambda : clf.predict(features_test), "Predict time")

# Compute scores
accuracy1 = sum(1 for p, l in zip(pred, labels_test) if p == l) / float(len(labels_test))
accuracy2 = clf.score(features_test, labels_test)

print("Accuracy1: %.2f" % accuracy1)
print("Accuracy2: %.2f" % accuracy2)

   
#########################################################


