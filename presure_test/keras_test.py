# import activation as activation
from keras import regularizers
from keras.regularizers import l2
from keras.models import Sequential
from keras.layers import Dense, Conv1D, Conv2D, Dropout, MaxPooling1D, Flatten
from presure_test.utils import mass_to_nump_mass
from keras.utils import to_categorical
from presure_test.plot_functions import plot_pred_results

# define classification model
def classification_model_conv(num_inputs, n_timesteps, n_features, n_outputs, num_1layer_neur, num_2layer_neur):
    input_shape = ( 20 )
    # n_timesteps, n_features, n_outputs = trainX.shape[1], trainX.shape[2], trainy.shape[1]
    # create model
    model = Sequential()
    # n_timesteps, n_features, n_outputs = trainX.shape[1], trainX.shape[2], trainy.shape[1]
    model = Sequential()
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(n_timesteps, n_features)))
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
    model.add(Dropout(0.5))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(n_outputs, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # compile model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    model.summary()
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

    # fit the model
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=1, verbose=2, batch_size=10)

    # evaluate the model
    # scores = model.evaluate(X_test, y_test, verbose=0)
    # print('Accuracy: {}% \n Error: {}'.format(scores[1], 1 - scores[1]))
    return model

def test_diff_model_shapes(X_train, y_train, X_test, y_test, num_inp):
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)

    # X_train = X_train.reshape( int(X_train.shape[0]), X_train.shape[1], 1)
    # y_train = y_train.reshape(int(y_train.shape[0]), y_train.shape[1])
    n_timesteps, n_features, n_outputs = X_train.shape[1], X_train.shape[2], y_train.shape[1]
    # X_test = X_test.reshape(X_test.shape[0], X_test.shape[1])
    for i in range(10,11):
        for j in range(50,51):
            # n_timesteps, n_features, n_outputs = X_train.shape[1], X_train.shape[2], y_train.shape[1]
            model = classification_model_conv(num_inp, n_timesteps, n_features, n_outputs, i, j)
            train_model = classify_keras(model, X_train, y_train, X_train, y_train, num_inp)
            pred = train_model.predict(X_test)

            pred = pred[0]
            plot_pred_results(pred, y_train[0], i, j)
            print("start "+ str(i) + " " + str(j))