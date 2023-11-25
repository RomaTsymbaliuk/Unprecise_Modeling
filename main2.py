# Start lab2
# Aij and Bij unprecise sets and u(x) function
a1 = [20, 40, 60, 80]
a2 = [10, 30, 50, 70]
b1 = [20000, 30000, 40000, 50000]
b2 = [10, 30, 50]
b3 = [10, 30, 50]


def function_unprecise_belonging_four_numbers(x, intervals):
    if x <= intervals[0]:
        return 1
    elif x > intervals[0] and x <= intervals[1]:
        return (x - intervals[0]) / (intervals[1] - intervals[0])
    elif x > intervals[1] and x <= intervals[2]:
        return (x - intervals[1]) / (intervals[2] - intervals[1])
    else:
        return 0

def function_unprecise_belonging_three_numbers(x, intervals):
    if x <= intervals[0]:
        return 1
    elif x > intervals[0] and x <= intervals[1]:
        return (x - intervals[0]) / (intervals[1] - intervals[0])
    else:
        return 0

