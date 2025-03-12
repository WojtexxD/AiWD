from locale import normalize

import numpy as np
from numpy import broadcast
from numpy.ma.extras import average

# zad1====================================
zad1 = np.arange(21, step=2)

# zad2====================================
# zad2 = np.array(np.arange(1,5),np.arange(5,9),np.arange(9,13),np.arange(13,17))
zad2_1 = np.arange(1, 17).reshape(4, 4)

# zad3====================================
zad3 = np.arange(1, 26).reshape(5, 5)
print(np.min(zad3), np.max(zad3))

# zad4====================================
zad4 = np.linspace(0, 1, 10)

# zad5====================================
zad5 = np.eye(3)  # to samo co np.identity(3)

# zad6====================================
zad6 = np.arange(1, 13).reshape(3, 4).reshape(2, 6)

# zad7====================================
zad7_1 = np.arange(1, 6)
zad7_2 = np.arange(6, 11)
zad7 = np.concatenate((zad7_1, zad7_2))

# zad8====================================
zad8 = np.zeros(9).reshape(3, 3)
np.fill_diagonal(zad8, 1)

# zad9====================================
zad9 = np.arange(0, 100).reshape(10, 10)
zad9 = zad9[3:8, 3:8]

# zad10====================================
zad10 = np.array([5, 2, 8, 1, 9, 3, 7, 4, 6, 0])
zad10 = (zad10 - zad10.min()) / (zad10.max() - zad10.min())

# zad11====================================
zad11a = np.array([1, 2, 3, 4, 5])
zad11b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
zad11 = zad11a + zad11b

# zad12====================================
zad12 = np.arange(1, 17).reshape(4, 4).T

# zad13====================================
zad13a = np.arange(1, 7).reshape(2, 3)
zad13b = np.arange(1, 13).reshape(3, 4)
zad13 = zad13a @ zad13b
# np.matmul(zad13a,zad13b)

# zad14====================================
zad14 = np.arange(1, 101).reshape(10, 10)
sumaa = zad14.sum(axis=1)
sumab = zad14.sum(axis=0)

# zad15====================================
zad15 = np.array([3, 8, 2, 5, 1, 4, 9, 7, 6, 0])
zad15[(zad15 < zad15.mean())] = 0

# zad16====================================
wektor = np.array([10, 20, 30])
macierz = np.array([[1], [2], [3], [4]])
wynik = wektor + macierz

# zad17====================================
zad17 = np.array([8, 3, 9, 5, 1, 7, 2, 0, 6, 4, 15, 13, 19, 12,
                11, 17, 14, 10, 16, 18, 25, 21, 23, 20, 22]).reshape(5,5)
zad17.sort()

# zad18====================================
zad18 = np.zeros((2,3,4))
print(f"liczba wymiarów: {zad18.ndim}")
print(f"liczba elementów: {zad18.size}")

# zad19====================================
zad19a = np.array([[2], [4], [6]])
zad19b = np.array([[1, 3, 5, 7]])
zad19 = zad19a*zad19b

# zad20====================================
zad20 = np.arange(1,37).reshape(6,6).reshape((3,4,3))
print(zad20[0].mean())
print(zad20[1].mean())
print(zad20[2].mean())