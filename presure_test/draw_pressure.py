from presure_test.pressure_data_init import load_pressures, generate_init_data
from presure_test.plot_functions import create_pressure_plot

# string = "xx.07.20"
# files_list = ["15.07.20"]
# files_list = list()
# for i in range (14, 16):
#
#
#    file = string.replace("xx" , str(i))
#    files_list.append(file)

from os import listdir
from os.path import isfile, join

mypath = "pressure/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# имена файлов из которых берем информацию для обучения
# files_list = ["16.07.20","17.07.20", "20.07.20"]
all_press = list()

for name in onlyfiles:
   # считываем файл получаем массив из элементов типа [время, давление, дождь]
   pressure = load_pressures(name)

   # подготавливаем данные: обнуляем данные о дожде и записываем в нужные интервалы значения
   presure_rain = generate_init_data(pressure)

   # если надо рисуем график
   create_pressure_plot(presure_rain, name[:-5], True)