
# function that creates a flower_dictionary from filename
def load_pressures(filename):
    flower_dict = list()
    with open(filename) as f:
        for line in f:
            coord = float(line.split(" ")[0])
            press = float(line.split(" ")[1])
            val   = int(line.split(" ")[2])
            flower_dict.append((coord, press, val))
        return flower_dict

def nullify_values(pressures_list):
    for pressure in pressures_list:
        pressure[2] = 0

    return pressures_list