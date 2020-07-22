import matplotlib

matplotlib.use('agg')

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np




def create_plot(point_list):
    x_min = 0.0;
    x_max = 1500.0
    y_min = 800.0;
    y_max = 1000.0

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    h = 100  # step size in the mesh
    # xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # plt.pcolormesh(xx, yy, Z, cmap=pl.cm.seismic)
    x = list()
    y = list()
    for i in range(0, len(point_list)):
        x.append(point_list[i][0])
        y.append(point_list[i][1])
        # plt.scatter(point_list[i][0], point_list[i][1], s=1)
    plt.plot(x,y)

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

    # plt.text(np.pi - 0.5, 0, '1 Axes', fontsize=26, bbox=dict(edgecolor='w', color='w'))
    # plt.text(0.1, 0, '3 Yaxis', fontsize=18, bbox=dict(edgecolor='w', color='w'), rotation=90)
    # plt.text(5, -0.9, '2 Xaxis', fontsize=18, bbox=dict(edgecolor='w', color='w'))
    #
    # plt.title('1a TITLE')
    # plt.ylabel('3a Ylabel')
    # plt.xlabel('2a Xlabel ')
    #
    # plt.text(5, 0.85, '6 Xticks', fontsize=12, bbox=dict(edgecolor='w', color='w'), rotation=90)
    # plt.text(0.95, -0.55, '6 Xticks', fontsize=12, bbox=dict(edgecolor='w', color='w'), rotation=90)
    #
    # plt.text(5.75, -0.5, '7 Yticks', fontsize=12, bbox=dict(edgecolor='w', color='w'))
    # plt.text(0.15, 0.475, '7 Yticks', fontsize=12, bbox=dict(edgecolor='w', color='w'))

    plt.grid(True)

    # смотри преамбулу
    plt.savefig('pic_1_5_1', fmt='png')