from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


def drawfigure(rate, grade, title):
    grade = np.abs(grade)
    if rate < 0.1:
        rate = 0.1
    if rate > 10:
        rate = 10
    if grade < 0.1:
        grade = 0.1
    if grade > 1:
        grade = 1
    grade *= np.sqrt(rate)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-5, 5.1, grade)
    Y = np.arange(-5 * rate, 5.1 * rate, grade)
    X, Y = np.meshgrid(X, Y)
    Z = X**2 + Y**2
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.set_title(title)
    plt.show()


drawfigure(1, 0.2, "Tom's figure")
