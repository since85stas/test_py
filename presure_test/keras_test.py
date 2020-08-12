# import activation as activation
from keras import regularizers
from keras.regularizers import l2
from keras.models import Sequential
from keras.layers import Dense, Conv1D
from presure_test.utils import mass_to_nump_mass
from keras.utils import to_categorical
from presure_test.plot_functions import plot_pred_results

# define classification model
def classification_model(num_inputs, num_1layer_neur, num_2layer_neur):
    input_shape = ( 20, 2)

    # create model
    model = Sequential()
    model.add(Conv1D(num_inputs, kernel_size=(2), activation='relu', kernel_initializer='he_uniform', input_shape=input_shape))
    model.add(Conv1D(10, kernel_size=(2),  activation='relu', kernel_initializer='he_uniform', input_shape=input_shape))
    # model.add(Dense(10, activation='sigmoid'))
    # model.add(Dense(num_2layer_neur, activation='relu'))
    # model.add(Dense(num_2layer_neur, activation='relu'))
    model.add(Dense(2, activation='softmax')) #, kernel_regularizer=regularizers.l2(0.01)

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

def classify_keras(model ,X_train, y_train, X_test, y_test, num_inp):
    # model = classification_model(num_inp,15,15)
    #
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    # fit the model
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100, verbose=2)

    # evaluate the model
    # scores = model.evaluate(X_test, y_test, verbose=0)
    # print('Accuracy: {}% \n Error: {}'.format(scores[1], 1 - scores[1]))
    return model

def test_diff_model_shapes(features_train, labels_train, features_test, labels_test, num_inp):
    for i in range(2,15):
        for j in range(50,51):
            model = classification_model(num_inp, i, j)
            train_model = classify_keras(model, features_train, labels_train, features_test, labels_test, num_inp)
            pred = train_model.predict(features_test)
            plot_pred_results(pred, labels_test, i, j)
            print("start "+ str(i) + " " + str(j))