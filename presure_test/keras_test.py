import activation as activation
from keras.regularizers import l2
from keras.models import Sequential
from keras.layers import Dense
from presure_test.utils import mass_to_nump_mass

def classify_keras_test(features_train, labels_train):
    numpy_features_train = mass_to_nump_mass(features_train)
    numpy_labels_train = mass_to_nump_mass(labels_train)
    model = Sequential()
    model.add(Dense(64, activation='relu'))
    # model.add(Dense(1), W_regularizer=l2(0.01))
    model.add(Dense(1), l2(0.01))
    model.add(activation('softmax'))
    model.compile(loss='squared_hinge',
                  optimizer='adadelta',
                  metrics=['accuracy'])
    model.fit(numpy_features_train, numpy_labels_train)
    return model