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

    FS.add_linguistic_variable("argument_var", LinguisticVariable([FuzzySet(function=Triangular_MF(a=7, b=9, c=13),    term="low"),
                                                            FuzzySet(function=Triangular_MF(a=10, b=12, c=14),  term="medium"),
                                                            FuzzySet(function=Triangular_MF(a=13, b=16, c=19), term="high")], concept="First arg",
                                                            universe_of_discourse=[8, 18]))

    FS.add_linguistic_variable("ordinat_var", LinguisticVariable([FuzzySet(function=Triangular_MF(a=2, b=4, c=5), term="low"),
                                                              FuzzySet(function=Triangular_MF(a=4, b=5, c=6), term="medium"),
                                                              FuzzySet(function=Triangular_MF(a=5, b=7, c=9), term="high")], concept="Second arg",
                                                              universe_of_discourse=[3, 8]))

    FS.add_linguistic_variable("result_var", LinguisticVariable([FuzzySet(function=Triangular_MF(a=0.13823, b=0.5, c=1.0), term="low"),
                                                      FuzzySet(function=Triangular_MF(a=0.8, b=1.5, c=1.7), term="medium"),
                                                      FuzzySet(function=Triangular_MF(a=1.5, b=1.8, c=2.985985), term="high")], concept="Third arg",
                                                      universe_of_discourse=[0.13824, 2.985984]))

    RULES = [
        "IF (argument_var IS low) AND (ordinat_var IS low) THEN (result_var IS low)",
        "IF (argument_var IS low) AND (ordinat_var IS medium) THEN (result_var IS high)",
        "IF (argument_var IS low) AND (ordinat_var IS high) THEN (result_var IS high)",
        "IF (argument_var IS medium) AND (ordinat_var IS low) THEN (result_var IS medium)",
        "IF (argument_var IS medium) AND (ordinat_var IS medium) THEN (result_var IS high)",
        "IF (argument_var IS medium) AND (ordinat_var IS high) THEN (result_var IS high)",
        "IF (argument_var IS high) AND (ordinat_var IS low) THEN (result_var IS medium)",
        "IF (argument_var IS high) AND (ordinat_var IS medium) THEN (result_var IS medium)",
        "IF (argument_var IS high) AND (ordinat_var IS high) THEN (result_var IS high)"
    ]

    FS.add_rules(RULES)

    return FS

def use_fuzzy_system(FS, x, y):
    FS.set_variable("argument_var", x)
    FS.set_variable("ordinat_var", y)
    results = FS.Mamdani_inference(["result_var"])
    return results['result_var']

#plot_graphic()

FS = fuzzy_rules_and_system_create()
result_fuzzy_var = use_fuzzy_system(FS, 8, 3)

x = 8
y = 3
for i in range(10):
    for j in range(10):
        delta = use_fuzzy_system(FS, x, y) * 100000 - function(x, y)
        print('Delta : ', delta)
        y = y + 0.1
    x = x + 0.1
print('result : ', result_fuzzy_var)