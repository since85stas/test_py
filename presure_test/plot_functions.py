import matplotlib

matplotlib.use('agg')

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator, NullFormatter


def create_plot(pressure_list):
    x_min = 0.0;
    x_max = 1500.0
    y_min = 800.0;
    y_max = 1000.0

    majorLocator = MultipleLocator(100)
    # Автоматический подбор промежуточных делений. Количество созданных делений равно n-1
    minorLocator = AutoMinorLocator(10)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    h = 100  # step size in the mesh
    # xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # plt.pcolormesh(xx, yy, Z, cmap=pl.cm.seismic)
    x = list()
    y = list()
    for i in range(0, len(pressure_list)):
        x.append(pressure_list[i][0])
        y.append(pressure_list[i][1])
        # plt.scatter(point_list[i][0], point_list[i][1], s=1)
    plt.plot(x,y)

    for pressure in pressure_list:
        if (pressure[2] > 0):
            plt.scatter(pressure[0], pressure[1], color= "r", s=8)
    # (fig, ax) = plt.subplots()
    # ax = fig.add_subplot("111")

    # xax = ax.xaxis
    # yax = ax.yaxis
    # xax.set_major_locator(majorLocator)
    # xax.set_minor_locator(minorLocator)
    plt.minorticks_on()
    plt.grid(True, "major")
    plt.grid(True, which='minor', color='grey', linestyle='dashed', alpha=0.5)
    # plt.gca(x_min = 0, x_max = 20, y_min = 800, y_max = 1000)
    # plt.axis(0 , 1000, 800, 1000)
    plt.xlabel("time")
    plt.ylabel("press")

    plt.savefig("test.png")

def create_sin():
    lag = 0.1
    x = np.arange(0.0, 2 * np.pi + lag, lag)
    y = np.cos(x)

    fig = plt.figure()
    plt.plot(x, y)
    plt.grid(True)

    # смотри преамбулу
    plt.savefig('pic_1_5_1', fmt='png')