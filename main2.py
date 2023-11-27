# Start lab2
# Aij and Bij unprecise sets and u(x) function
a1 = [20, 40, 60, 80]
a2 = [10, 30, 50, 70]
b1 = [20000, 30000, 40000, 50000]
b2 = [10, 30, 50]
b3 = [10, 30, 50]

class inputData:
    def __init__(self, area_cottage, area_building, money_benefits, money_losses, money_lost_benefits):
        self.area_cottage = area_cottage
        self.area_building = area_building
        self.money_benefits = money_benefits
        self.money_losses = money_losses
        self.money_lost_benefits = money_lost_benefits
        self.fuzzicated_data = []

    def u_x(self, x):
        if x == 'a11':
            return 1
        elif x == 'a12':
            return 1
        elif x == 'a13':
            return 1
        elif x == 'a14':
            return 1
        elif x == 'a15':
            return 1
        elif x == 'a21':
            return 1
        elif x == 'a22':
            return 1
        elif x == 'a23':
            return 1
        elif x == 'a24':
            return 1
        elif x == 'a25':
            return 1
        elif x == 'b11':
            return 1
        elif x == 'b12':
            return 1
        elif x == 'b13':
            return 1
        elif x == 'b21':
            return 1
        elif x == 'b22':
            return 1
        elif x == 'b23':
            return 1
        elif x == 'b31':
            return 1
        elif x == 'b32':
            return 1
        elif x == 'b33':
            return 1

    def category_decising(self, name, x, intervals):
        if len(intervals) == 4:
            if x <= intervals[0]:
                self.fuzzicated_data.append([(name + "1"), x])
            elif x > intervals[0] and x <= intervals[1]:
                self.fuzzicated_data.append([(name + "2"), x])
            elif x > intervals[1] and x <= intervals[2]:
                self.fuzzicated_data.append([(name + "3"), x])
            elif x > intervals[2] and x <= intervals[3]:
                self.fuzzicated_data.append([(name + "4"), x])
            else:
                self.fuzzicated_data.append([(name + "5"), x])
        elif len(intervals) == 3:
            if x <= intervals[0]:
                self.fuzzicated_data.append([(name + "1"), x])
            elif x > intervals[0] and x <= intervals[1]:
                self.fuzzicated_data.append([(name + "2"), x])
            else:
                self.fuzzicated_data.append([(name + "3"), x])

    def fuzzification_data(self):
        for name, interval, x in zip(['a1', 'a2', 'b1', 'b2', 'b3'], [a1, a2, b1, b2, b3], [self.area_cottage, self.area_building, self.money_benefits, self.money_losses, self.money_lost_benefits]):
            self.category_decising(name, x, interval)

    def L_rules(self, x):
        if x[0][0] == 'a11' or x[0][0] == 'a12':
            if x[1][0] == 'a21' or x[1][0] == 'a22':
                return [min(max(self.u_x('a11'), self.u_x('a12')), max(self.u_x('a21'), self.u_x('a22'))), 'c1']
            elif x[1][0] == 'a23':
                #min(max(a11, a12), max(a23))
                return [min(max(self.u_x('a11'), self.u_x('a12')), self.u_x('a23')), 'c2']
            elif x[1][0] == 'a24' or x[1][0] == 'a25':
                #min(max(a11, a12), max(a24, a25))
                return [min(max(self.u_x('a11'), self.u_x('a12')), max(self.u_x('a24'), self.u_x('a25'))), 'c2']
        elif x[0][0] == 'a13' or x[0][0] == 'a14':
            if x[1][0] == 'a21' or x[1][0] == 'a22':
                # min(max(a13, a14), max(a21, a22))
                return [min(max(self.u_x('a13'), self.u_x('a14')), max(self.u_x('a21'), self.u_x('a22'))), 'c2']
            elif x[1][0] == 'a23':
                # min(max(a13, a14), max(a23))
                return [min(max(self.u_x('a13'), self.u_x('a14')), self.u_x('a23')), 'c2']
            elif x[1][0] == 'a24' or x[1][0] == 'a25':
                # min(max(a13, a14), max(a24, a25))
                return [min(max(self.u_x('a13'), self.u_x('a14')), max(self.u_x('a24'), self.u_x('a25'))), 'c3']
        elif x[0][0] == 'a15':
            if x[1][0] == 'a21' or x[1][0] == 'a22':
                # min(max(a15), max(a21, a22))
                return [min(self.u_x('a15'), max(self.u_x('a21'), self.u_x('a22'))), 'c3']
            elif x[1][0] == 'a23':
                # min(max(a15), max(a23))
                return [min(self.u_x('a15'), self.u_x('a23')), 'c3']
            elif x[1][0] == 'a24' or x[1][0] == 'a25':
                # min(max(a15), max(a24, a25))
                return [min(self.u_x('a15'), max(self.u_x('a24'), self.u_x('a25'))), 'c3']
        if x[4][0] == 'b31' or x[4][0] == 'b32':
            if x[3][0] == 'b21':
                # min(max(b31, b32), b21)
                return [min(max(self.u_x('b31'), self.u_x('b32')), self.u_x('b21')), 'c2']
            elif x[3][0] == 'b22':
                # min(max(b31, b32), b22)
                return [min(max(self.u_x('b31'), self.u_x('b32')), self.u_x('b22')), 'c2']
            elif x[3][0] == 'b23':
                # min(max(b31, b32), b23)
                return [min(max(self.u_x('b31'), self.u_x('b32')), self.u_x('b23')), 'c1']
        elif x[4][0] == 'b33':
            # min(b33)
            return [self.u_x('b33'), 'c1']
    def agregation_data(self):
        return self.L_rules(self.fuzzicated_data)
    def defuzzification_data(self):
        pass

first_vector = inputData(35, 20, 24000, 5, 12)
first_vector.fuzzification_data()
print(first_vector.agregation_data())
