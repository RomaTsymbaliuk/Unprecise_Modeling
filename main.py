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

    def print_set(self):
        print('Set :', self.set)


#Create set A and B
A = unpresice_set_U(A_flag)
B = unpresice_set_U(B_flag)
#First point of the lab1
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
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
