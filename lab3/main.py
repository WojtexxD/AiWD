import numpy as np

# zad1=============================
A = np.array([3, 5, 7, 9])
B = np.array([2, 4, 6, 8])
zad01 = A / B

# zad2=============================
X = np.array([[1, 2, 3], [4, 5, 6]])
skalar = 3
zad02 = X + skalar

# zad3=============================
C = np.array([10, 20, 30, 40])
D = np.array([1, 2, 3])
# zad03 = D-C
# ponieważ obydwie tablice są różnej wielkości

# zad4=============================
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([10, 20, 30])
zad04 = M + v

# zad5=============================
Z = np.zeros((3, 4))
ones = np.ones(4)
zad05 = Z + ones

# zad6=============================
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20])
zad06 = A*B[:,np.newaxis]

# zad7=============================
temps = np.array([0, 10, 20, 30, 40])
zad07 = temps * (9 / 5) + 32

# zad8=============================
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
zad08 = np.sqrt(data)

# zad9=============================
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
zad09a = np.sin(angles)
zad09b = np.cos(angles)
zad09c = np.tan(angles)

# zad10=============================
A = np.array([[5, 6], [7, 8]])
B = np.array([2, 3])
zad10 = A%B

# zad11=============================
X = np.array([[2, 1, 4], [1, 3, 7], [7, 8, 9]])
Y = np.array([5, 2, 6])
zad11min = np.minimum(X,Y)
zad11max = np.maximum(X,Y)

# zad12=============================
values = np.array([-3, -2, -1, 0, 1, 2, 3])
zad12 = np.abs(values)

# zad13=============================
A = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.uint64)
B = np.array([[10, 20, 30], [40, 50, 60]], dtype=np.uint64)
zad13 = A**B

# zad14=============================
probabilities = np.array([0.1, 0.01, 0.001, 0.0001])
zad14a = np.log(probabilities)
zad14b = np.log10(probabilities)

# zad15=============================
M = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([[10], [20]])
zad15 = M+v