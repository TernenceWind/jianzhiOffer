# coding = utf-8
# 二维数组中的查找
matrix = [[1, 2, 8, 9],
          [2, 4, 9, 12],
          [4, 7, 10, 13],
          [6, 8, 11, 15]]
key1 = 12
mm = [1,2,3,4,5,6]
# 1
def Find(matrix,key):
    if not matrix:
        print('False')
        return 
    if type(matrix[0]) != list:
        matrix = [matrix]
    for i in range(len(matrix[0])):
        if matrix[0][i] == key:
            print('True')
            return
        elif matrix[0][i] < key:
            for j in range(len(matrix)-1):
                if matrix[j+1][i] == key:
                    print('True')
                    return
                elif matrix[j+1][i] > key:
                    pass
    print('False')
Find(matrix,key1)

# 2
def Find2(matrix,key):
    if not matrix:
        print('False')
        return 
    if type(matrix[0]) != list:
        matrix = [matrix]
    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = cols - 1
    while row < rows and col >= 0:
        if matrix[row][col] == key:
            print('True')
            return
        elif matrix[row][col] > key:
            col -= 1
        elif matrix[row][col] < key:
            row += 1
    print("False")
    return
Find2([],key1)
