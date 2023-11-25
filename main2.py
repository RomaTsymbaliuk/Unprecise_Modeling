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
        self.rules =

    def function_unprecise_belonging(self, x, intervals):
        if len(intervals) == 4:
            if x <= intervals[0]:
                self.fuzzicated_data.append([1, 1])
            elif x > intervals[0] and x <= intervals[1]:
                self.fuzzicated_data.append([2, (x - intervals[0]) / (intervals[1] - intervals[0])])
            elif x > intervals[1] and x <= intervals[2]:
                self.fuzzicated_data.append([3, (x - intervals[1]) / (intervals[2] - intervals[1])])
            else:
                self.fuzzicated_data.append([4, 0])
        elif len(intervals) == 3:
            if x <= intervals[0]:
                self.fuzzicated_data.append([1, 1])
            elif x > intervals[0] and x <= intervals[1]:
                self.fuzzicated_data.append([2, (x - intervals[0]) / (intervals[1] - intervals[0])])
            else:
                self.fuzzicated_data.append([3, 0])

    def fuzzification_data(self):
        for interval, x in zip([a1, a2, b1, b2, b3], [self.area_cottage, self.area_building, self.money_benefits, self.money_losses, self.money_lost_benefits]):
            self.function_unprecise_belonging(x, interval)

    def agregation_data(self):
        pass


first_vector = inputData(35, 20, 24000, 5, 12)
first_vector.fuzzification_data()
print(first_vector.fuzzicated_data)
