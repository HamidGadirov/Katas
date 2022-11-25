# In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

def solution(matrix):
    minesweeper = []
    for i in range(len(matrix)):
        minesweeper.append([])
        for j in range(len(matrix[0])):
            l = -matrix[i][j] # for mines in itself
            print(l)
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0 <= i + x < len(matrix) and 0 <= j + y < len(matrix[0]):
                        l += matrix[i + x][j + y]
            minesweeper[i].append(l)
    return minesweeper


# import numpy as np
# def solution(matrix):
#     def neighboring(M, i, j):
#         x = len(matrix)
#         y = len(matrix[0])
#         if i == x - 1 and j == y - 1:
#             return int(M[i - 1][j] == 'true') + int(M[i][j - 1] == 'true') + \
#                     int(M[i - 1][j - 1] == 'true')
#         elif i == 0 and j == 0:
#             return int(M[i + 1][j] == 'true') + int(M[i][j + 1] == 'true') + \
#                     int(M[i + 1][j + 1] == 'true')
#         elif i == x - 1 and j == 0:
#             return int(M[i - 1][j] == 'true') + int(M[i][j + 1] == 'true') + \
#                     int(M[i - 1][j + 1] == 'true')
#         elif i == 0 and j == y - 1:
#             return int(M[i + 1][j] == 'true') + int(M[i][j - 1] == 'true') + \
#                     int(M[i + 1][j - 1] == 'true')
#         else:
#             print(i, j)
#             return int(M[i - 1][j - 1] == 'true') + int(M[i - 1][j] == 'true') + \
#                     int(M[i][j - 1] == 'true') + int(M[i][j] == 'true') + \
#                     int(M[i + 1][j - 1] == 'true') + int(M[i + 1][j] == 'true') + \
#                     int(M[i + 1][j + 1] == 'true')
    
#     x = len(matrix)
#     y = len(matrix[0])
#     minesweeper = []
#     for i in range(x):
#         for j in range(y):
#             if (matrix[i][j]):
#                 minesweeper.append(1)
#             else:
#                 minesweeper.append(neighboring(matrix, i, j))
#     print(minesweeper)
#     minesweeper = np.array(minesweeper).reshape(x, y)
#     print(minesweeper)
#     return minesweeper
    

