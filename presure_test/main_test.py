import numpy as np

# def add_dimen(array):
#     for interv in array:


from presure_test.pressure_data_linear import generate_linear_vectors_list, generate_nonlin_vectors_list

# ширина рассматриваемого интервала в записях
interv_width = 20

# Load data
data = np.load('./signal_waves_medium.npy')
x_val, y_val = data[:, 0], data[:, 1]

sub1 = np.split(y_val, 1)

weigts = np.full(data.shape[0], 1)

# Load data
data_lin = np.load('./signal_waves_linear.npy')
x_lin, y_lin = data_lin[:, 0], data_lin[:, 1]

weigts_lin = np.full(data_lin.shape[0], 0)

all_vectors = np.concatenate((y_val, y_lin), 0)

all_weights = np.concatenate((weigts, weigts_lin), 0)
print("")