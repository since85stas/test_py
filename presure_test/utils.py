import numpy as np

def mass_to_nump_mass(massive):
    num_arr = np.array(massive )
    return num_arr

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))