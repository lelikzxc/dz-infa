def fill_spiral_matrix(n, m):
    matrix = [[0 for j in range(m)] for i in range(n)]
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1
    direction = 0
    value = 1
    while top <= bottom and left <= right:
        if direction == 0:
            for j in range(left, right + 1):
                matrix[top][j] = value
                value += 1
            top += 1
            direction = 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                matrix[i][right] = value
                value += 1
            right -= 1
            direction = 2
        elif direction == 2:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = value
                value += 1
            bottom -= 1
            direction = 3
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = value
                value += 1
            left += 1
            direction = 0
        else:
            break
    return matrix



def multiply_row_by_index(matrix):
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    for i in range(n):
        for j in range(m):
            matrix[i][j] *= (i)

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
matrix = fill_spiral_matrix(n, m)
print("Матрица по спирали:")
for row in matrix:
    print(row)
multiply_row_by_index(matrix)
print("Матрица после умножения:")
for row in matrix: 
    print(row)