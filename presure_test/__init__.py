from time import time

from presure_test.plot_functions import  create_pressure_plot, create_sin, create_weight_plot
from presure_test.pressure_data_init import load_pressures, generate_pressure_interv,\
   generate_press_vectors_list, generate_init_data
from presure_test.neural_functions import get_interval_weight, classify_svc_lin, get_intervals_weights, classify_svc_rbf