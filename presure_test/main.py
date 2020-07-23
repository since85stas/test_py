from presure_test.plot_functions import  create_plot, create_sin
from presure_test.pressure_data_init import load_pressures, nullify_values, set_rain_values

print("init")
pressure = load_pressures("test-press.txt")
pressure_null = nullify_values(pressure)
presure_rain = set_rain_values( ( (450.0, 550.0),), 1, pressure_null)
create_plot(presure_rain)
# create_sin()

