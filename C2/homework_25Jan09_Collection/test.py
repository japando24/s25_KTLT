def add_matrix(matrix1, matrix2):
    l1=len(matrix1[0])
    l2=len(matrix2[0])
    res=[]
    if len(matrix1) != len(matrix2) or l1 != l2:
        print("Muốn cộng hai ma trận phải cùng kích thước.")
    else:
        for i in range (len(matrix1)):
            row=[]
            for j in range (l2):
                row.append(matrix1[i][j] + matrix2[i][j])
            res.append(row)
        return res

def print_matrix(matrix):
    for i in matrix:
        print(i)

matrix1=[[2,3,4],[4,5,6]]
matrix2=[[7,8,9],[10,11,12]]
print_matrix(add_matrix(matrix1,matrix2))