import numpy as np

rowsA, colsA = 1000, 1000
matrixA = np.random.randint(0, 10, size=(rowsA, colsA))

rowsB, colsB = 1000, 1000
matrixB = np.random.randint(0, 10, size=(rowsB, colsB))

if colsA != rowsB:
    print("columns of matrix A is not equal rows of Matrix B, you can't multiply")
    exit

with open("matrixA.txt", "w") as file:
    np.savetxt(file, matrixA, fmt="%d", delimiter=" ")

with open("matrixB.txt", "w") as file:
    np.savetxt(file, matrixB, fmt="%d", delimiter=" ")