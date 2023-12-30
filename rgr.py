import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def plotGraphic():
    fig = plt.figure(figsize = (10,10))
    ax = plt.axes(projection='3d')
    x = np.arange(8, 18, 0.1)
    y = np.arange(3, 8, 0.1)

    X, Y = np.meshgrid(x, y)
    Z = np.power(X, 3) * np.power(Y, 3)

    surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis)

    # Set axes label
    ax.set_xlabel('x', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    ax.set_zlabel('z', labelpad=20)

    fig.colorbar(surf, shrink=0.5, aspect=8)

    plt.show()

plotGraphic()