# Start lab2
# Aij and Bij unprecise sets and u(x) function
from scipy.integrate import quad
from functions import *
from sympy import Symbol, integrate

number_input_variables = 5
number_output_variables = 1

class inputData:
    def __init__(self, area_cottage, area_building, money_benefits, money_losses, money_lost_benefits):
        self.area_cottage = area_cottage
        self.area_building = area_building
        self.money_benefits = money_benefits
        self.money_losses = money_losses
        self.money_lost_benefits = money_lost_benefits
        self.fuzzicated_data = []
        self.aggregated_data = []
        self.activated_data = []
        self.defuzzificated_data = []

    def u_x(self, x, value):
        if x == 'a11':
            return a11(value[0][1])
        elif x == 'a12':
            return a12(value[0][1])
        elif x == 'a13':
            return a13(value[0][1])
        elif x == 'a14':
            return a14(value[0][1])
        elif x == 'a15':
            return a15(value[0][1])
        elif x == 'a21':
            return a21(value[1][1])
        elif x == 'a22':
            return a22(value[1][1])
        elif x == 'a23':
            return a23(value[1][1])
        elif x == 'a24':
            return a24(value[1][1])
        elif x == 'a25':
            return a25(value[1][1])
        elif x == 'b11':
            return b11(value[2][0])
        elif x == 'b12':
            return b12(value[2][1])
        elif x == 'b13':
            return b13(value[2][2])
        elif x == 'b21':
            return b21(value[3][0])
        elif x == 'b22':
            return b22(value[3][1])
        elif x == 'b23':
            return b23(value[3][2])
        elif x == 'b31':
            return b31(value[4][0])
        elif x == 'b32':
            return b32(value[4][1])
        elif x == 'b33':
            return b33(value[4][2])

    def category_decising(self, name, x, intervals):
        if len(intervals) == 4:
            if x <= intervals[0]:
                self.fuzzicated_data.append([(name + "1"), x, eval(name + "1")])
            elif x > intervals[0] and x <= intervals[1]:
                self.fuzzicated_data.append([(name + "2"), x, eval(name + "2")])
            elif x > intervals[1] and x <= intervals[2]:
                self.fuzzicated_data.append([(name + "3"), x, eval(name + "3")])
            elif x > intervals[2] and x <= intervals[3]:
                self.fuzzicated_data.append([(name + "4"), x, eval(name + "4")])
            else:
                self.fuzzicated_data.append([(name + "5"), x, eval(name + "5")])
        elif len(intervals) == 3:
            if x <= intervals[0]:
                self.fuzzicated_data.append([(name + "1"), x, eval(name + "1")])
            elif x > intervals[0] and x <= intervals[1]:
                self.fuzzicated_data.append([(name + "2"), x, eval(name + "2")])
            else:
                self.fuzzicated_data.append([(name + "3"), x, eval(name + "3")])

    def fuzzification_data(self):
        for name, interval, x in zip(['a1', 'a2', 'b1', 'b2', 'b3'], [a1, a2, b1, b2, b3], [self.area_cottage, self.area_building, self.money_benefits, self.money_losses, self.money_lost_benefits]):
            self.category_decising(name, x, interval)

    def L_rules(self, x):
        if x[0][0] == 'a11' or x[0][0] == 'a12':
            if x[1][0] == 'a21' or x[1][0] == 'a22':
                return [min(max(self.u_x('a11', x), self.u_x('a12', x)), max(self.u_x('a21', x), self.u_x('a22', x))), 'c1']
            elif x[1][0] == 'a23':
                #min(max(a11, a12), max(a23))
                return [min(max(self.u_x('a11', x), self.u_x('a12', x)), self.u_x('a23', x)), 'c2']
            elif x[1][0] == 'a24' or x[1][0] == 'a25':
                #min(max(a11, a12), max(a24, a25))
                return [min(max(self.u_x('a11', x), self.u_x('a12', x)), max(self.u_x('a24', x), self.u_x('a25', x))), 'c2']
        elif x[0][0] == 'a13' or x[0][0] == 'a14':
            if x[1][0] == 'a21' or x[1][0] == 'a22':
                # min(max(a13, a14), max(a21, a22))
                return [min(max(self.u_x('a13', x), self.u_x('a14', x)), max(self.u_x('a21', x), self.u_x('a22', x))), 'c2']
            elif x[1][0] == 'a23':
                # min(max(a13, a14), max(a23))
                return [min(max(self.u_x('a13', x), self.u_x('a14', x)), self.u_x('a23', x)), 'c2']
            elif x[1][0] == 'a24' or x[1][0] == 'a25':
                # min(max(a13, a14), max(a24, a25))
                return [min(max(self.u_x('a13', x), self.u_x('a14', x)), max(self.u_x('a24', x), self.u_x('a25', x))), 'c3']
        elif x[0][0] == 'a15':
            if x[1][0] == 'a21' or x[1][0] == 'a22':
                # min(max(a15), max(a21, a22))
                return [min(self.u_x('a15', x), max(self.u_x('a21', x), self.u_x('a22', x))), 'c3']
            elif x[1][0] == 'a23':
                # min(max(a15), max(a23))
                return [min(self.u_x('a15', x), self.u_x('a23', x)), 'c3']
            elif x[1][0] == 'a24' or x[1][0] == 'a25':
                # min(max(a15), max(a24, a25))
                return [min(self.u_x('a15', x), max(self.u_x('a24', x), self.u_x('a25', x))), 'c3']
        if x[4][0] == 'b31' or x[4][0] == 'b32':
            if x[3][0] == 'b21':
                # min(max(b31, b32), b21)
                return [min(max(self.u_x('b31', x), self.u_x('b32', x)), self.u_x('b21', x)), 'c2']
            elif x[3][0] == 'b22':
                # min(max(b31, b32), b22)
                return [min(max(self.u_x('b31', x), self.u_x('b32', x)), self.u_x('b22', x)), 'c2']
            elif x[3][0] == 'b23':
                # min(max(b31, b32), b23)
                return [min(max(self.u_x('b31', x), self.u_x('b32', x)), self.u_x('b23', x)), 'c1']
        elif x[4][0] == 'b33':
            # min(b33)
            return [self.u_x('b33', x), 'c1']
    def agregation_data(self):
        self.agregated_data = self.L_rules(self.fuzzicated_data)

    def activization_data(self, y):
        return min(eval(self.agregated_data[1])(y), self.agregated_data[0])
    def defuzzification_data(self):
        interval_a = eval(self.agregated_data[1] + "_interval")[0]
        interval_b = eval(self.agregated_data[1] + "_interval")[1]
        num1 = quad(lambda x: x * self.activization_data(x), interval_a, interval_b)
        num2 = quad(lambda x: self.activization_data(x), interval_a, interval_b)
        print(num1[0] / num2[0])


first_vector = inputData(35, 20, 24000, 5, 12)
first_vector.fuzzification_data()
first_vector.agregation_data()
first_vector.defuzzification_data()

second_vector = inputData(50, 10, 12000, 1, 9)
second_vector.fuzzification_data()
second_vector.agregation_data()
second_vector.defuzzification_data()