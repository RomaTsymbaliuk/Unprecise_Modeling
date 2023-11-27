a1 = [20, 40, 60, 80]
a2 = [10, 30, 50, 70]
b1 = [20000, 30000, 40000, 50000]
b2 = [10, 30, 50]
b3 = [10, 30, 50]

a11_interval = [0, a1[0]]
def a11(x):
    return 1

a12_interval = [a1[0], a1[1]]
def a12(x):
    return 1

a13_interval = [a1[1], a1[2]]
def a13(x):
    return 1

a14_interval = [a1[2], a1[3]]
def a14(x):
    return 1

a15_interval = [a1[3], 100]
def a15(x):
    return 1

a21_interval = [0, a2[0]]
def a21(x):
    return 1

a22_interval = [a2[0], a2[1]]
def a22(x):
    return 1

a23_interval = [a2[1], a2[2]]
def a23(x):
    return 1

a24_interval = [a2[2], a2[3]]
def a24(x):
    return 1

a25_interval = [a2[3], 100]
def a25(x):
    return 1

b11_interval = [0, b1[0]]
def b11(x):
    return 1

b12_interval = [b1[0], b1[1]]
def b12(x):
    return 1

b13_interval = [b1[1], b1[2]]
def b13(x):
    return 1

b21_interval = [0, b2[0]]
def b21(x):
    return 1

b22_interval = [b2[0], b2[1]]
def b22(x):
    return 1

b23_interval = [b2[1], b2[2]]
def b23(x):
    return 1

b31_interval = [0, b3[0]]
def b31(x):
    return 1

b32_interval = [b3[0], b3[1]]
def b32(x):
    return 1

b33_interval = [b3[1], b3[2]]
def b33(x):
    return 1

c1_interval = [100000, 200000]
def c1(x):
    return 1

c2_interval = [200000, 300000]
def c2(x):
    return 1

c3_interval = [300000, 400000]
def c3(x):
    return 1