from random import randint


def createMatrix(n: int) -> list[list]:
    matrix = []

    for i in range(n):
        line = []
        for j in range(n):
            line.append(randint(0, 10))
        matrix.append(line)

    return matrix


def sumMatrix(
        A: list[list[int | float]],
        B: list[list[int | float]]) -> list[list[int | float]] | None:

    is_matrix = isMatrix(A)
    is_matrix = isMatrix(B)
    is_same_size = isSameSize(A, B)
    if len(A) == len(B) and is_matrix and is_same_size:
        matrix = []
        for i in range(len(A)):
            line = []
            for j in range(len(A[i])):
                line.append(A[i][j] + B[i][j])
            matrix.append(line)
        return matrix
    return None


def subtractMatrix(
        A: list[list[int | float]],
        B: list[list[int | float]]) -> list[list[int | float]] | None:

    is_matrix = isMatrix(A)
    is_matrix = isMatrix(B)
    is_same_size = isSameSize(A, B)
    if len(A) == len(B) and is_matrix and is_same_size:
        matrix = []
        for i in range(len(A)):
            line = []
            for j in range(len(A[i])):
                line.append(A[i][j] - B[i][j])
            matrix.append(line)
        return matrix
    return None


def isMatrix(matrix: list[list]) -> bool:
    col_size: list[int] = []
    for i in range(len(matrix)):
        col_size.append(len(matrix[i]))
    for i in range(len(matrix)-1):
        if col_size[i] != col_size[i+1]:
            return False
    return True


def isSameSize(
        A: list[list[int | float]],
        B: list[list[int | float]]) -> bool:

    if len(A) == len(B):
        for i in range(len(A)):
            if len(A[i]) != len(B[i]):
                return False
    else:
        return False
    return True


n = 2

matrix = createMatrix(n)
A = createMatrix(n)
B = createMatrix(n)
print(isSameSize(A, B))
C = sumMatrix(A, B)
print(matrix)
print(A)
print(B)
print(C)
