import numpy as np

# def add_dimen(array):
#     for interv in array:
from keras import Sequential
from keras.layers import Conv1D, Dropout, MaxPooling1D, Flatten, Dense
from keras.utils import to_categorical
from presure_test.pressure_data_linear import generate_linear_vectors_list, generate_nonlin_vectors_list

# fit and evaluate a model
def evaluate_model(trainX, trainy, testX, testy):
    verbose, epochs, batch_size = 0, 10, 32
    n_timesteps, n_features, n_outputs = trainX.shape[1], trainX.shape[2], trainy.shape[1]
    model = Sequential()
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(n_timesteps, n_features)))
    model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
    model.add(Dropout(0.5))
    model.add(MaxPooling1D(pool_size=2))
    model.add(Flatten())
    model.add(Dense(100, activation='relu'))
    model.add(Dense(n_outputs, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit network
    model.fit(trainX, trainy, epochs=epochs, batch_size=batch_size, verbose=verbose)

    pred = model.predict(testX)
    # evaluate model
    _, accuracy = model.evaluate(testX, testy, batch_size=batch_size, verbose=0)
    return accuracy


# fit and evaluate a model
def evaluate_model_dense(trainX, trainy, testX, testy):
    verbose, epochs, batch_size = 2, 10, 32
    n_timesteps, n_features, n_outputs = trainX.shape[0], trainX.shape[1], trainy.shape[1]
    model = Sequential()
    model.add(Dense(n_features, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(n_outputs, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit network
    model.fit(trainX, trainy, epochs=epochs, batch_size=batch_size, verbose=verbose)

    pred = model.predict(testX)
    # evaluate model
    _, accuracy = model.evaluate(testX, testy, batch_size=batch_size, verbose=0)
    return accuracy

# ширина рассматриваемого интервала в записях
interval_width = 20

# Load data
data = np.load('./signal_waves_medium.npy')
x_val, y_val = data[:, 0], data[:, 1]
y_test = data[0:100, 1]

weigts = np.full(data.shape[0], 1)
weigts_test = np.full(100,1)

# Load data
data_lin = np.load('./signal_waves_linear.npy')
x_lin, y_lin = data_lin[:, 0], data_lin[:, 1]
y_lin_test = data_lin[0:100, 1]

weigts_lin = np.full(data_lin.shape[0], 0)
weigts_lin_test = np.full(100, 0)

all_vectors = np.concatenate((y_val, y_lin), 0)
all_vectors_test = np.concatenate((y_test, y_lin_test), 0)

all_weights = np.concatenate((weigts, weigts_lin), 0)
all_weights_test = np.concatenate((weigts_test, weigts_lin_test),0)

evaluate_model_dense(all_vectors, to_categorical(all_weights), all_vectors_test, to_categorical(all_weights_test))

print("")