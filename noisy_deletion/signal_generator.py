import matplotlib.pyplot as plt
import numpy as np

# Sample configuration
num_samples = 1000

case_is_lin = 1

# Intrasample configuration
num_elements = 1
interval_per_element = 0.1
total_num_elements = int(num_elements / interval_per_element)
starting_point = int(0 - 0.5*total_num_elements)

# Other configuration
num_samples_visualize = 1

# Containers for samples and subsamples
samples = []
xs = []
ys = []

# Generate samples
for j in range(0, num_samples):
  # Report progress
  if j % 100 == 0:
    print(j)
  # Generate wave
  for i in range(starting_point, total_num_elements):
    x_val = i * interval_per_element
    #
    if case_is_lin == 0:
        y_val = x_val
    else:
        y_val = x_val * x_val
    xs.append(x_val)
    ys.append(y_val)
  # Append wave to samples
  samples.append((xs, ys))
  # Clear subsample containers for next sample
  xs = []
  ys = []

# Input shape
print(np.shape(np.array(samples[0][0])))

# Save data to file for re-use
if case_is_lin == 0:
    np.save('signal_waves_linear.npy', samples)
else:
    np.save('signal_waves_medium.npy', samples)

# Visualize a few random samples
for i in range(0, num_samples_visualize):
    random_index = np.random.randint(0, len(samples) - 1)
    x_axis, y_axis = samples[random_index]
    plt.plot(x_axis, y_axis)
    plt.title(f'Visualization of sample {random_index} ---- y: f(x) = x^2')
    plt.show()