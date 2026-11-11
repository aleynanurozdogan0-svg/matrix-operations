# Matris okuma, gösterme, seyrek (sparse) forma çevirme ve devrik (transpose) alma
def readMatrix():
    rows = int(input("how many rows: "))
    columns = int(input("how many columns: "))


    matrix = [[0 for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            print("enter matrix element", i, j, ":", end="")
            matrix[i][j] = int(input())
    return matrix


def showMatrix(matrix):
    for row in matrix:  
        for element in row:
            print(element, end=" ")
        print()


def toSparseMatrix(matrix):
    sparseMatrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                sparseMatrix.append([i, j, matrix[i][j]])
    return sparseMatrix


def transposeMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    transpose = [[0 for _ in range(rows)] for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            transpose[j][i] = matrix[i][j]
    return transpose


# ---------------- Ana program ----------------

mtx = readMatrix()

print("\nnormal matris: ")
showMatrix(mtx)

print("\nsparse matris: ")
spsM = toSparseMatrix(mtx)
showMatrix(spsM)

print("\ntranspose matris: ")
transpose = transposeMatrix(mtx)
showMatrix(transpose)

print("\ntranspose sparse matris: ")
spsT = toSparseMatrix(transpose)
showMatrix(spsT)