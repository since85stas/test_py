""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.

    The objective of this exercise is to recreate the decision
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """

from course_naive_base.prep_terrain_data import makeTerrainData
# from class_vis import prettyPicture, output_image
from course_naive_base.class_vis import prettyPicture, output_image
from course_naive_base.ClassifyNB import classify, NBAccuracy, classifySVM

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii] == 1]

# You will need to complete this function imported from the ClassifyNB script.
# Be sure to change to that code tab to complete this quiz.
clf = classifySVM(features_train, labels_train)

# acc = clf.score(features_test)

print(NBAccuracy(features_train, labels_train, features_test, labels_test))

### draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test)
# output_image("test_nb.png", "png", open("test_nb.png", "rb").read())