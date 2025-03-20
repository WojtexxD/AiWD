import numpy as np

# zad1=====================================================================
arr = np.array(["python", "NumPy", "data science", "machine learning"])
zad01 = np.strings.upper(arr)

# zad2=====================================================================
arr = np.array(["PYTHON", "NUMPY", "DATA SCIENCE"])
zad02a = np.strings.lower(arr)
zad02b = np.strings.title(arr)
zad02c = np.strings.capitalize(arr)

# zad3=====================================================================
arr1 = np.array(["machine", "deep"])
arr2 = np.array(["learning", "networks"])
zad03a = np.strings.add(arr1, arr2)
zad03b = np.strings.replace(zad03a, ["el", "pn"], ["e l", "p n"])
print(zad03b)

# zad4=====================================================================
arr = np.array(["python.data.science", "machine.learning"])
zad04 = np.char.split(arr, sep=".")
print(zad04)

# zad5=====================================================================
arr = np.array([" python ", " numpy ", " pandas "])
zad05 = np.strings.strip(arr)
print(zad05)

# zad6=====================================================================
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])
zad06a = np.dot(a, b)
zad06b = a @ b

# zad7=====================================================================
A = np.array([[2, 3], [1, 4]])
B = np.array([[5, 1], [2, 6]])
zad07 = np.matmul(A, B)
print(zad07)
print(A @ B)

# zad8=====================================================================
A = np.array([[4, 2], [3, 5]])
b = np.array([8, 7])
zad08 = np.linalg.solve(A, b)

# zad9=====================================================================
M = np.array([[6, 2], [3, 9]])
zad09a = np.linalg.det(M)
zad09b = np.linalg.inv(M)
print(M @ zad09b)

# zad10=====================================================================
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
zad10a = np.outer(v1, v2)
zad10b, zad10c = np.linalg.eig(zad10a)
print(zad10b)
print(zad10c)

# zad11=====================================================================
arr = np.array([[0, 5, 0], [2, 0, 3], [0, 0, 7]])
zad11 = np.nonzero(arr)
print(zad11)
print(arr[zad11])

# zad12=====================================================================
data = np.array([-3, 4, -1, 6, -8, 2])
zad12 = np.where(data < 0, -99, data)
print(zad12)

# zad13=====================================================================
indices = np.array([2, 0, 1, 2, 0])
options = [np.array([10, 20, 30, 40, 50]),
           np.array([60, 70, 80, 90, 100]),
           np.array([110, 120, 130, 140, 150])]
zad13 = np.choose(indices, options)
print(zad13)

# zad14=====================================================================
matrix = np.array([[5, 12, 8], [3, 7, 9], [15, 4, 2]])
# warunki = [matrix < 5, matrix <= 10 , matrix > 10]
warunki = [matrix < 5, (matrix >= 5) & (matrix <= 10), matrix > 10]
opcje = [0, 50, 100]
zad14 = np.select(warunki, opcje)
print(zad14)

# zad15=====================================================================
values = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
np.putmask(values, values % 2 == 0, 0)
print(values)
np.put(values, [0, 4, 8], [100, 200, 300])
print(values)