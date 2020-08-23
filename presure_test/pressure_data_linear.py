def generate_linear_vectors_list(num_attempts, points_num):
    interval_list = list()
    for i in range (0, num_attempts):
        full_int = 0.5
        new_int = list()
        for j in range (0, points_num):
            new_int.append(full_int)
        interval_list.append(new_int)
    return interval_list

def generate_nonlin_vectors_list(num_attempts, points_num):
    interval_list = list()
    for i in range (0, num_attempts):
        new_int = list()
        for j in range (0, points_num):
            x = 1/points_num * j
            y = (x + 0.5)*(x + 0.5)
            new_int.append(y)
        interval_list.append(new_int)
    return interval_list

