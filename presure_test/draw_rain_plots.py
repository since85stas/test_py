
from presure_test.plot_functions import  create_pressure_plot, create_sin, create_weight_plot
from presure_test.pressure_data_init import load_pressures, generate_pressure_interv,\
   generate_press_vectors_list, generate_init_data
from presure_test.neural_functions import get_interval_weight, get_intervals_weights,classify_svc_lin
from presure_test.keras_test import classify_keras_test_csv, classify_keras, test_diff_model_shapes
from  presure_test.utils import mass_to_nump_mass
from os import listdir
from os.path import isfile, join


print("init")

# # имена файлов из которых берем информацию для обучения
files_list = ["14.07.20",
              # "17.07.20",
              "20.07.20",
              # "22.07.20",
              # "27.07.20",
              # "28.07.20",
              # "29.07.20",
              # "30.07.20",
              "31.07.20",
              # "03.08.20",
              # "04.08.20",
              # "05.08.20",
              # "06.08.20"
              ]
all_press = list()

# mypath = "pressure/"
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# имена файлов из которых берем информацию для обучения
# files_list = ["16.07.20","17.07.20", "20.07.20"]
# all_press = list()

for name in files_list:
   # считываем файл получаем массив из элементов типа [время, давление, дождь]
   pressure = load_pressures( name + " .txt")

   # если надо рисуем график
   create_pressure_plot(pressure, name, True)
   # собираем в один файл
   all_press.append(pressure)

crop_press = list()

for i in range (0,3):
    if i == 0:
        pressure = all_press[0]
        len_list = len(pressure)
        for j in range (0, len_list -1):
            if (pressure[j][0] > 450):
                pressure = all_press[0][0:j+5]
                break
        crop_press.append((pressure))
    elif i == 1:
        i_init = 30
        pressure = all_press[1]
        len_list = len(pressure)
        for j in range (0, len_list -1):
            if (pressure[j][0] > 650):
                pressure = all_press[1][i_init:j+5]
                break
        crop_press.append((pressure))

name = 0
for crop in crop_press:
    # если надо рисуем график
    create_pressure_plot(crop, "crop" + str(name), False)
    name = name +1

print("")

# init = 0
# for day in all_press:
#     for point in day:
#         val = point[0]
#         point[0] = val + init
#
#     init = day[len(day) - 1][0]
#
# all_press_new = list()
#
# for intrv in all_press:
#     all_press_new.extend(intrv)
#
# # рисуем график всех данных
# create_pressure_plot(all_press_new, "all_pressure_rain.png", False)
# print("num pressures= {}".format(len(all_press)))