import random

def initMatrix(size):
    """Initialize matrix."""
    matr = []
    for i in range(size):
        matr.append([])
        for j in range(size):
            matr[i].append(random.randint(10, 99))
    return matr

def printMatrix(matr,size):
    """Print matrix ordinarily."""
    for i in range(size):
        print(matr[i])

def spiralPrintMatrix(matr,size):
    """Print matrix spiral"""
    center =int((size)/2)
    i = j = center
    l = 1
    matrStr = ''
    while l <= center:
        while j >= center - l:  # left
            matrStr = matrStr + str(matr[i][j]) + ' '
            j -= 1
        j += 1
        i += 1
        while i <= center + l:  # down
            matrStr = matrStr + str(matr[i][j]) + ' '
            i += 1
        i -= 1
        j += 1
        while j <= center + l:  # right
            matrStr = matrStr + str(matr[i][j]) + ' '
            j += 1
        j -= 1
        i -= 1
        while i >= center - l:  # up
            matrStr = matrStr + str(matr[i][j]) + ' '
            i -= 1
        i += 1
        j -= 1
        l += 1
    for item in reversed(matr[i][:j+1]):
        matrStr = matrStr + str(item) + ' '
    print(matrStr)


n = int(input("Введите n:"))
matrix=initMatrix(2*n-1)
printMatrix(matrix, 2*n-1)
spiralPrintMatrix(matrix, 2*n-1)
