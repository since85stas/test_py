# import activation as activation
from keras.regularizers import l2
from keras.models import Sequential
from keras.layers import Dense
from presure_test.utils import mass_to_nump_mass
from keras.utils import to_categorical

# define classification model
def classification_model(num_inputs):
    # create model
    model = Sequential()
    model.add(Dense(num_inputs, activation='relu', input_shape=(num_inputs,)))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='softmax'))

    # compile model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def classify_keras_test_csv(features_train, labels_train):
    numpy_features_train = mass_to_nump_mass(features_train)
    numpy_labels_train = mass_to_nump_mass(labels_train)
    model = Sequential()
    model.add(Dense(64, activation='relu'))
    # model.add(Dense(1), W_regularizer=l2(0.01))
    model.add(Dense(1), l2(0.01))
    # model.add(activation('softmax'))
    model.compile(loss='squared_hinge',
                  optimizer='adadelta',
                  metrics=['accuracy'])
    model.fit(numpy_features_train, numpy_labels_train)
    return model

def classify_keras(features_train, labels_train, features_test, labels_test, num_inp):
    X_train = mass_to_nump_mass(features_train)
    y_train = mass_to_nump_mass(labels_train)
    X_test = mass_to_nump_mass(features_test)
    y_test = mass_to_nump_mass(labels_test)
    model = classification_model(num_inp)

    # y_binary = to_categorical(y_train)
    # y_binary_test = to_categorical(y_test)

    # fit the model
    model.fit(X_train, y_binary, validation_data=(X_test, y_binary_test), epochs=10, verbose=2)

    # evaluate the model
    scores = model.evaluate(X_test, y_test, verbose=0)

    print('Accuracy: {}% \n Error: {}'.format(scores[1], 1 - scores[1]))