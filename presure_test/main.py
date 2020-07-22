from presure_test.functions import  create_plot, create_sin
from presure_test.pressure_data_init import load_pressures, nullify_values

print("init")
pressure = load_pressures("test-press.txt")
pressure_null = nullify_values(pressure)
# create_plot(pressure)
# create_sin()

