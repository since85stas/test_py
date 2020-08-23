
# function that creates a flower_dictionary from filename
from numpy import dstack


def generate_init_data(pressures):

    # бнуляем значения о дожде
    pressure_null = nullify_values(pressures)

    # записываем 1 в заданный интервал по времени
    presure_rain = set_rain_values(((450.0, 550.0),), 1, pressure_null)
    presure_rain = set_rain_values(((1050.0, 1150.0),), 1, presure_rain)
    return presure_rain

def load_pressures(filename):
    flower_dict = list()
    with open("pressure/" + filename) as f:
        for line in f:
            coord = float(line.split(" ")[0])
            press = float(line.split(" ")[1])
            val   = int(line.split(" ")[2])
            flower_dict.append([coord, press, val])
        return flower_dict

# обнуляем данные о дожде
def nullify_values(pressures_list):
    for pressure in pressures_list:
        pressure[2] = 0

    return pressures_list

# записываем данные о дожде нужным значением в интервале времени
def set_rain_values(ranges, value, pressure_list):
    for pressure in pressure_list:
        if (is_in_many_range(ranges, pressure[0])):
            pressure[2] = value
    return pressure_list

# проверяем попадает ли значение в интервал
def is_in_many_range(ranges, number):
    for pair in ranges:
        if ( number > pair[0] and number < pair[1]):
            return True
    else: return False

# генерирует список интервалов
def generate_pressure_interv(pressure_list, points_num):
    interval_list = list()
    for i in range (0, len(pressure_list) - points_num):
        interval_list.append(pressure_list[i:i+points_num])
    return interval_list

def generate_press_vectors_list(pressure_list, points_num):
    interval_list = list()
    for i in range (0, len(pressure_list) - points_num):
        full_int = pressure_list[i:i+points_num]
        new_int = list()
        first_val = full_int[0]
        for point in full_int:
            new_int.append(point[1])
            # new_int.append(point[1]/1000.)
        interval_list.append(new_int)
    return interval_list

#  делим на 1000, чтобы получить значения от 0 до 1
def normalize_interv(intervs):
    first_val = intervs[0]
    for i in range(0, len(intervs)):
        # intervs[i] = intervs[i] - first_val
        intervs[i] = (intervs[i])/1000.
    return intervs

# load a list of files into a 3D array of [samples, timesteps, features]
def load_group(pressure_list, points_num):
	loaded = list()
	for i in (0,2):
		data = generate_press_vectors_list(pressure_list, points_num)
		loaded.append(data)
	# stack group so that features are the 3rd dimension
	loaded = dstack(loaded)
	return loaded