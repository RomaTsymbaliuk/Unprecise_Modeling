# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# A = {<u(x), x>}
A = []
B = []
V = 12
A_flag = 1
B_flag = 2

class unpresice_set_U:
    def __init__(self, set_flag):
        self.supr = -1
        self.mode = []
        self.carrier = []
        self.core = []
        self.height = -1
        self.set = []
        if set_flag == A_flag:
            for i in range(V + 1):
                self.set.append([i, round(i / V, 2)])
        if set_flag == B_flag:
            for i in range(V + 1):
                self.set.append([0.5 * i, round(i / (4 * V), 2)])

    def find_height_set(self):
        sup_A = self.set[0][1]
        for i in range(V + 1):
            if self.set[i][1] >= sup_A:
                sup_A = self.set[i][1]
        self.supr = sup_A
        print('Set height : ', self.supr)

    def find_mode_set(self):
        if self.supr == -1:
            self.find_height_set()

        for i in range(V + 1):
            if self.set[i][1] == self.supr:
                self.mode = self.set[i]
                break
        print('Set mode : ', self.mode)

    def find_carrier_set(self):
        for i in range(V + 1):
            if self.set[i][1] > 0:
                self.carrier.append(self.set[i])
        print('Set carrier :', self.carrier)

    def find_core_set(self):
        for i in range(V + 1):
            if self.set[i][1] == 1:
                self.core.append(self.set[i])
        print('Set core :', self.core)

    def find_alhpa_set(self, alpha):
        alpha_set = []
        for i in range(V + 1):
            if self.set[i][1] >= alpha:
                alpha_set.append(self.set[i])
        print('Set alpha ', alpha, ' is ', alpha_set)

    def maximinn_intersect(self, B):
        intersect_set = []
        for i in range(V + 1):
            intersect_set.append(min(self.set[i][1], B.set[i][1]))
        return intersect_set

    def maximinn_union(self, B):
        union_set = []
        for i in range(V + 1):
            union_set.append(max(self.set[i][1], B.set[i][1]))
        return union_set

    def addition(self):
        addition_set = []
        for i in range(V + 1):
            addition_set.append(round(1 - self.set[i][1], 2))
        return addition_set

    def print_set(self):
        print('Set :', self.set)

    def add_sect(self, B):
        add_s = []
        for i in range(V + 1):
            add_s.append(round(self.set[i][1] + B.set[i][1], 2))
        return add_s

    def substract_set(self, B):
        subs_s = []
        for i in range(V + 1):
            subs_s.append(round(self.set[i][1] - B.set[i][1], 2))
        return subs_s

    def multiply_set(self, B):
        mltpl_s = []
        for i in range(V + 1):
            mltpl_s.append(round(self.set[i][1] * B.set[i][1], 2))
        return mltpl_s

    def division_set(self, B):
        dvsn_s = []
        for i in range(V + 1):
            if self.set[i][1] and B.set[i][1]:
                dvsn_s.append(round(self.set[i][1] / B.set[i][1], 2))
            else:
                dvsn_s.append(0)
        return dvsn_s

#Create set A and B
A = unpresice_set_U(A_flag)
B = unpresice_set_U(B_flag)
#First point of the lab_1
print('Set A:')
A.print_set()
A.find_height_set()
A.find_mode_set()
A.find_carrier_set()
A.find_core_set()
A.find_alhpa_set(0.3)
print('Set B:')
B.print_set()
B.find_height_set()
B.find_mode_set()
B.find_carrier_set()
B.find_core_set()
B.find_alhpa_set(0.4)
########################

#Second point of the lab_1
print('Intersect and union operations')
print('Intersect set')
intersect_set = A.maximinn_intersect(B)
print(intersect_set)
print('Union set')
union_set = A.maximinn_union(B)
print(union_set)
addition_set = A.addition()
print('Addition A set')
print(addition_set)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Third point of the lab_1
print('Addition, Substraction, multiplication, division of A and B')
add_s = A.add_sect(B)
print(add_s)
sub_s = A.substract_set(B)
print(sub_s)
mltpl_s = A.multiply_set(B)
print(mltpl_s)
dvsn_s = A.division_set(B)
print(dvsn_s)