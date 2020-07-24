from time import time

from presure_test.plot_functions import  create_pressure_plot, create_sin, create_weight_plot
from presure_test.pressure_data_init import load_pressures, generate_pressure_interv,\
   generate_press_vectors_list, generate_init_data
from presure_test.neural_functions import get_interval_weight, classify, get_intervals_weights

print("init")

# string = "xx.07.20"
files_list = ["16.07.20","17.07.20", "20.07.20"]
# files_list = ["15.07.20"]
# files_list = list()
# for i in range (14, 16):
#    file = string.replace("xx" , str(i))
#    files_list.append(file)

all_press = list()
for name in files_list:
   pressure = load_pressures("pressure/" + name + " .txt")
   # pressure_null = nullify_values(pressure)
   # presure_rain = set_rain_values( ( (450.0, 550.0),), 1, pressure_null)
   presure_rain = generate_init_data(pressure)
   # create_pressure_plot(presure_rain, name, True)
   all_press.extend(presure_rain)

# create_plot(all_press, "all_pressure.png")

# split = int(0.5*len(presure_rain))
pressure_interv = generate_pressure_interv(all_press, 20)

press_vector_list = generate_press_vectors_list(all_press, 20)

# weights = list()
# for i in range(0, len(pressure_interv)):
#    # create_plot(train_interv[i], "interval" + str(i) +".png", True)
#    weights.append(get_interval_weight(pressure_interv[i]))
weights = get_intervals_weights(pressure_interv)

t0 = time()
clf = classify(press_vector_list, weights)
print ("training time:", round(time()-t0, 3), "s")

test_press = load_pressures("pressure/15.07.20 .txt")
test_rain = generate_init_data(test_press)
test_interv = generate_pressure_interv(test_rain, 20)

goal_weights = get_intervals_weights(test_interv)

test_press_vector_list = generate_press_vectors_list(test_press, 20)

t0 = time()
pred = clf.predict(test_press_vector_list)
print ("pred time:", round(time()-t0, 3), "s")

for i in range(0, len(pred)-1):
   print(str(goal_weights[i]) + " " + str(pred[i]))

create_weight_plot(goal_weights, "weight", False)
create_weight_plot(pred, "weight", False)
# create_sin()

