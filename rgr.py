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

    FS.add_linguistic_variable("x", LinguisticVariable([FuzzySet(function=Crisp_MF(a=8.0, b=10.8), term="very_low"),
                                                        FuzzySet(function=Crisp_MF(a=10.75, b=12.2),term="low"),
                                                        FuzzySet(function=Crisp_MF(a=11.7, b=12.7), term="average"),
                                                        FuzzySet(function=Crisp_MF(a=12.5, b=15.8), term="large"),
                                                        FuzzySet(function=Crisp_MF(a=15.3, b=18), term="very_large")], concept="First arg",
                                                            universe_of_discourse=[8, 18]))

    FS.add_linguistic_variable("y", LinguisticVariable([FuzzySet(function=Gaussian_MF(mu=3.105, sigma=0.2), term="very_low"),
                                                        FuzzySet(function=Triangular_MF(a=3.2, b=5.0, c=5.4),term="low"),
                                                        FuzzySet(function=Triangular_MF(a=4.2, b=5.0, c=5.4), term="average"),
                                                        FuzzySet(function=Triangular_MF(a=5.3, b=6.2, c=6.7), term="large"),
                                                        FuzzySet(function=Triangular_MF(a=6.6, b=7.6, c=8), term="very_large")], concept="Second arg",
                                                        universe_of_discourse=[3, 8]))

    FS.add_linguistic_variable("z", LinguisticVariable([FuzzySet(function=Triangular_MF(a=0.13823, b=0.15832, c=0.17854), term="very_low"),
                                                      FuzzySet(function=Triangular_MF(a=0.17414, b=0.23421, c=0.65423), term="low"),
                                                      FuzzySet(function=Triangular_MF(a=1.1, b=1.2, c=1.6), term="average"),
                                                      FuzzySet(function=Triangular_MF(a=1.5, b=2.0, c=2.2),term="large"),
                                                      FuzzySet(function=Triangular_MF(a=2.0, b=2.8, c=3.0),term="very_large")], concept = "Third arg",
                                                      universe_of_discourse=[0.13824, 2.985984]))

    RULES = [
        "IF (x IS very_low) AND (y IS very_low) THEN (z IS very_low)",
        "IF (x IS very_low) AND (y IS low) THEN (z IS very_low)",
        "IF (x IS very_low) AND (y IS average) THEN (z IS low)",
        "IF (x IS very_low) AND (y IS large) THEN (z IS average)",
        "IF (x IS very_low) AND (y IS very_large) THEN (z IS large)",
        "IF (x IS low) AND (y IS very_low) THEN (z IS very_low)",
        "IF (x IS low) AND (y IS low) THEN (z IS very_low)",
        "IF (x IS low) AND (y IS average) THEN (z IS low)",
        "IF (x IS low) AND (y IS large) THEN (z IS average)",
        "IF (x IS low) AND (y IS very_large) THEN (z IS large)",
        "IF (x IS average) AND (y IS very_low) THEN (z IS low)",
        "IF (x IS average) AND (y IS low) THEN (z IS low)",
        "IF (x IS average) AND (y IS average) THEN (z IS average)",
        "IF (x IS average) AND (y IS large) THEN (z IS average)",
        "IF (x IS average) AND (y IS very_large) THEN (z IS large)",
        "IF (x IS large) AND (y IS very_low) THEN (z IS low)",
        "IF (x IS large) AND (y IS low) THEN (z IS average)",
        "IF (x IS large) AND (y IS average) THEN (z IS large)",
        "IF (x IS large) AND (y IS large) THEN (z IS very_large)",
        "IF (x IS large) AND (y IS very_large) THEN (z IS very_large)",
        "IF (x IS very_large) AND (y IS very_low) THEN (z IS average)",
        "IF (x IS very_large) AND (y IS low) THEN (z IS average)",
        "IF (x IS very_large) AND (y IS average) THEN (z IS large)",
        "IF (x IS very_large) AND (y IS large) THEN (z IS very_large)",
        "IF (x IS very_large) AND (y IS very_large) THEN (z IS very_large)"
    ]

    FS.add_rules(RULES)

    return FS

def use_fuzzy_system(FS, x, y):
    FS.set_variable("x", x)
    FS.set_variable("y", y)
    results = FS.Mamdani_inference(["z"])
    return results['z']

#plot_graphic()


FS = fuzzy_rules_and_system_create()
result_fuzzy_var = use_fuzzy_system(FS, 8, 3)

x = 8.1
y = 3.1
delta_sum = 0
steps = 1

while x < 10.9 and steps <= 50:
    while y < 8:
#        fuzzy_var = use_fuzzy_system(FS, x, y) * 1000000
        func_value = function(x, y)
        fuzzy_var = use_fuzzy_system(FS, x, y) * 100000
        delta = math.fabs(fuzzy_var - function(x, y))
        print('x : ', x, ' y : ', y, ' fuzzy_var : ', fuzzy_var, ' func_value : ', func_value, ' delta : ', delta)
        delta = math.fabs(fuzzy_var - func_value)
        delta_sum = delta_sum + delta
        y = y + 0.1
    steps = steps + 1
    x = x + 0.1

print('delta_sum : ', delta_sum / 1000000)