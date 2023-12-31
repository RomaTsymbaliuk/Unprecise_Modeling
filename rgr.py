import math
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from simpful import *

x_interval = [8, 18]
y_interval = [3, 8]

def function(x, y):
    return math.pow(x, 3) * math.pow(y, 3)
def plot_graphic():
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


def fuzzy_rules_and_system_create():
    FS = FuzzySystem()

    FS.add_linguistic_variable("x", LinguisticVariable([FuzzySet(function=Triangular_MF(a=8, b=9, c=10.8), term="very low"),
                                                        FuzzySet(function=Triangular_MF(a=4.2, b=5, c=5.4),term="low"),
                                                        FuzzySet(function=Triangular_MF(a=4.2, b=5, c=5.4), term="medium"),
                                                        FuzzySet(function=Triangular_MF(a=5.3, b=7, c=6.7), term="large"),
                                                        FuzzySet(function=Triangular_MF(a=6.6, b=7.6, c=8), term="very large")], concept="First arg",
                                                            universe_of_discourse=[8, 18]))

    FS.add_linguistic_variable("y", LinguisticVariable([FuzzySet(function=Triangular_MF(a=3, b=4, c=4.5), term="very low"),
                                                        FuzzySet(function=Triangular_MF(a=4.2, b=5, c=5.4),term="low"),
                                                        FuzzySet(function=Triangular_MF(a=4.2, b=5, c=5.4), term="medium"),
                                                        FuzzySet(function=Triangular_MF(a=5.3, b=7, c=6.7), term="large"),
                                                        FuzzySet(function=Triangular_MF(a=6.6, b=7.6, c=8), term="very large")], concept="Second arg",
                                                        universe_of_discourse=[3, 8]))

    FS.add_linguistic_variable("z", LinguisticVariable([FuzzySet(function=Triangular_MF(a=0.13823, b=0.5, c=0.7), term="very low"),
                                                      FuzzySet(function=Triangular_MF(a=0.6, b=1.0, c=1.2), term="low"),
                                                      FuzzySet(function=Triangular_MF(a=1.1, b=1.2, c=1.6), term="average"),
                                                      FuzzySet(function=Triangular_MF(a=1.5, b=2.0, c=2.2),term="large"),
                                                      FuzzySet(function=Triangular_MF(a=2.0, b=2.8, c=3.0),term="very large")], concept = "Third arg",
                                                      universe_of_discourse=[0.13824, 2.985984]))

    RULES = [
        "IF (x IS low) AND (y IS low) THEN (z IS low)",
        "IF (x IS low) AND (y IS medium) THEN (z IS high)",
        "IF (x IS low) AND (y IS high) THEN (z IS high)",
        "IF (x IS medium) AND (y IS low) THEN (z IS medium)",
        "IF (x IS medium) AND (y IS medium) THEN (z IS high)",
        "IF (x IS medium) AND (y IS high) THEN (z IS high)",
        "IF (x IS high) AND (y IS low) THEN (z IS medium)",
        "IF (x IS high) AND (y IS medium) THEN (z IS medium)",
        "IF (x IS high) AND (y IS high) THEN (z IS high)"
    ]

    FS.add_rules(RULES)

    return FS

def use_fuzzy_system(FS, x, y):
    FS.set_variable("argument_var", x)
    FS.set_variable("ordinat_var", y)
    results = FS.Mamdani_inference(["result_var"])
    return results['result_var']

plot_graphic()


FS = fuzzy_rules_and_system_create()
result_fuzzy_var = use_fuzzy_system(FS, 8, 3)

x = 8.1
y = 3.1

while x < 18:
    while y < 8:
#        fuzzy_var = use_fuzzy_system(FS, x, y) * 1000000
#        delta = fuzzy_var - function(x, y)
        func_value = function(x, y)
        print('x ')
        y = y + 0.1
    x = x + 0.5
