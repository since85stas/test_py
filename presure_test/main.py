from time import time

from presure_test.plot_functions import  create_pressure_plot, create_sin, create_weight_plot
from presure_test.pressure_data_init import load_pressures, generate_pressure_interv,\
   generate_press_vectors_list, generate_init_data
from presure_test.neural_functions import get_interval_weight, get_intervals_weights,classify_svc_lin
from presure_test.keras_test import classify_keras_test_csv, classify_keras, test_diff_model_shapes
from  presure_test.utils import mass_to_nump_mass

print("init")

# string = "xx.07.20"

# files_list = ["15.07.20"]
# files_list = list()
# for i in range (14, 16):
#    file = string.replace("xx" , str(i))
#    files_list.append(file)

# имена файлов из которых берем информацию для обучения
files_list = ["16.07.20",
              "17.07.20",
              "20.07.20",
              "22.07.20"
              # "27.07.20",
              # "28.07.20",
              # "29.07.20",
              # "30.07.20",
              # "31.07.20",
              # "03.08.20",
              # "04.08.20",
              # "05.08.20",
              # "06.08.20"
              ]
all_press = list()

for name in files_list:
   # считываем файл получаем массив из элементов типа [время, давление, дождь]
   pressure = load_pressures( name + " .txt")

   # подготавливаем данные: обнуляем данные о дожде и записываем в нужные интервалы значения
   presure_rain = generate_init_data(pressure)

   # если надо рисуем график
   # create_pressure_plot(presure_rain, name, True)

   # собираем в один файл
   all_press.extend(presure_rain)

# рисуем график всех данных
create_pressure_plot(all_press, "all_pressure.png", True)
print("num pressures= {}".format(len(all_press)))

# split = int(0.5*len(presure_rain))

# ширина рассматриваемого интервала в записях
interv_width = 20

# генерируем интервалы из элементов типа [время, давление, дождь]
pressure_interv = generate_pressure_interv(all_press, interv_width)

# генерируем интервалы для обучения только из давлений
press_vector_list = generate_press_vectors_list(all_press, interv_width)

# weights = list()
# for i in range(0, len(pressure_interv)):
#    # create_plot(train_interv[i], "interval" + str(i) +".png", True)
#    weights.append(get_interval_weight(pressure_interv[i]))

# получаем вес для каждого интервала - сумма всех ненулевых згачений дождя в интервале
weights = get_intervals_weights(pressure_interv)


# обучаем сетку
t0 = time()
# clf = classify_svc_lin(press_vector_list, weights)
print ("training time:", round(time()-t0, 3), "s")

# данные для проверки нейросетки
test_press = load_pressures("16.07.20 .txt")
test_rain = generate_init_data(test_press)
test_interv = generate_pressure_interv(test_rain, interv_width)

# валидные значения весов по тестироемуму множеству
goal_weights = get_intervals_weights(test_interv)

# генерируем интервалы только из давлений для предсказания
test_press_vector_list = generate_press_vectors_list(test_press, interv_width)

t0 = time()
# получаем предсказываемые веса

# test_press_vector_list = press_vector_list
# goal_weights = weights

# model = classify_keras(1,features_train=mass_to_nump_mass(press_vector_list),
#                labels_train=mass_to_nump_mass(weights),
#                features_test=mass_to_nump_mass(test_press_vector_list),
#                labels_test=mass_to_nump_mass(goal_weights),
#                num_inp=interv_width
#                )
model = test_diff_model_shapes(
               X_train=mass_to_nump_mass(press_vector_list),
               y_train=mass_to_nump_mass(weights),
               X_test=mass_to_nump_mass(test_press_vector_list),
               y_test=mass_to_nump_mass(goal_weights),
               num_inp=interv_width
               )
print ("pred time:", round(time()-t0, 3), "s")

# pred = model.predict(mass_to_nump_mass(test_press_vector_list))

# pred = clf.predict(test_press_vector_list)
# print(pred)
# for i in range(0, len(goal_weights)-1):
#    pred_1 = pred[i]
#    print("res {} {} {}".format (pred_1[0], pred_1[1], goal_weights[i]))
   # print(str(goal_weights[i]) + " " + str(pred[i]))

# create_weight_plot(goal_weights, "weight", False)
# create_weight_plot(pred, "weight", False)
# create_sin()

