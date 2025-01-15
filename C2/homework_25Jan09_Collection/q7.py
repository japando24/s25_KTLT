# Q7: Xử lý ma trận:
# • Viết hàm nhập matrix.
# • Viết hàm cộng 2 matrix.
# • Viết hàm tính matrix hoán vị
def create_matrix(rs, cs):
    matrix=[]
    for i in range (rs):
        row = list(map(int, input(f"Nhập dòng {i+1} (CÝ: Các số cách nhau bằng khoảng trắng): ").split()))
        while len(row) != cs:
            print(f"Vui lòng nhập đúng {cs} phần tử")
            row=list(map(int,input(f"Nhập lại dòng {i+1}: ").split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for i in matrix:
        print(i)

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
def transposr_matrix(matrix):
    res=[]
    lc=len(matrix[0])
    lr=len(matrix)
    for i in range (lc):
        new_r=[]
        for j in range (lr):
            new_r.append(matrix[j][i])
        res.append(new_r)
    return res

#Tạo ma trận 1
size1=input("Nhập kích thước ma trận 1 (dòng x cột): ")
size1_lst=size1.replace(" ","").split("x")
r1=int(size1_lst[0])
c1=int(size1_lst[1])
matrix1=create_matrix(r1,c1)
print_matrix(matrix1)

#Tạo ma trận 2
size2=input("Nhập kích thước ma trận 2 (dòng x cột): ")
size2_lst=size2.replace(" ","").split("x")
r2=int(size2_lst[0])
c2=int(size2_lst[1])
matrix2=create_matrix(r2,c2)
print_matrix(matrix2)

print("Chọn chức năng:")
print("1. Cộng hai ma trận")
print("2. Chuyển đổi thành ma trận hoán vị")
print("0. THOÁT")
pick=int(input("Chọn chức năng: "))

while True:
    if pick == 1:
        print("Kết quả cộng hai ma trận:")
        print_matrix(add_matrix(matrix1,matrix2))
        break
    if pick == 2:
        flag=False
        while not flag:
            print("MA TRẬN")
            print("0. Đổi chức năng")
            print("1. Ma trận 1")
            print("2. Ma trận 2")
            m = int(input("Chọn ma trận muốn hoán vị:"))
            if m == 1:
                tra_ma1 = transposr_matrix(matrix1)
                print_matrix(transposr_matrix(matrix1))
                print("-"*30)
            elif m == 2:
                tra_ma2 = transposr_matrix(matrix2)
                print_matrix(tra_ma2)
                print("-"*30)
            elif m==0:
                flag=True
            else:
                print("Vui lòng chọn đúng số trong menu")
                print("*" * 50)
    elif pick == 0:
        print("Cảm ơn đã sử dụng! LOVE LOVE")
        break
    else:
        print("Vui lòng chọn đúng số trong menu")
        print("*" * 50)

