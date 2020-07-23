
# function that creates a flower_dictionary from filename

def generate_init_data(pressures):
    pressure_null = nullify_values(pressures)
    presure_rain = set_rain_values(((450.0, 550.0),), 1, pressure_null)
    presure_rain = set_rain_values(((1050.0, 1150.0),), 1, pressure_null)
    return presure_rain

def load_pressures(filename):
    flower_dict = list()
    with open(filename) as f:
        for line in f:
            coord = float(line.split(" ")[0])
            press = float(line.split(" ")[1])
            val   = int(line.split(" ")[2])
            flower_dict.append([coord, press, val])
        return flower_dict

def nullify_values(pressures_list):
    for pressure in pressures_list:
        pressure[2] = 0

    return pressures_list

def set_rain_values(ranges, value, pressure_list):
    for pressure in pressure_list:
        if (is_in_many_range(ranges, pressure[0])):
            pressure[2] = 1

    return pressure_list

def is_in_many_range(ranges, number):
    for pair in ranges:
        if ( number > pair[0] and number < pair[1]):
            return True
    else: return False

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
        for point in full_int:
            # point_lsit = list()
            # point_lsit.append(point[0])
            # point_lsit.append(point[1])
            new_int.append(point[1])
        interval_list.append(new_int)
    return interval_list