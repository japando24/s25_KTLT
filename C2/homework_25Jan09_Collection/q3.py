# Q3: Viết chương trình cho phép:
# • Khởi tạo và nhập vào ma trận MxN phần tử ngẫu nhiên.
# • Xuất dòng bất kỳ nhập từ bàn phím.
# • Xuất cột bất kỳ từ bàn phím.
# • Xuất số MAX trong ma trận.
import random

while True:
    print("Menu")
    print("1. Khởi tạo và nhập vào ma trận dòng x cột (rxc)")
    print("2. Xuất dòng")
    print("3. Xuất cột")
    print("4. Xuất số lớn nhất trong ma trận")
    print("0. THOÁT")
    print("-"*30)
    pick=int(input("Chọn chức năng: "))
    lst=[]
    if pick == 1:
        pvi=input("Nhập kích thước của ma trận (row x column): ")
        pvi_lst=pvi.replace(" ","").split("x")
        r=int(pvi_lst[0])
        c=int(pvi_lst[1])
        num_limit=int(input("Giới hạn phần tử (0 đến ...): "))
        matrix=[[random.randint(1, num_limit) for _ in range(c)] for _ in range(r)]
        print("Matrix")
        for r in matrix:
            print(r)
        print("*"*50)
    elif pick == 2:
        r_pick=int(input("Nhập chỉ số dòng muốn xuất: "))
        if 0 < r_pick <= len(matrix):
            print(f"Dòng {r_pick}: {matrix[r_pick]}")
        else:
            print("Chỉ số dòng không hợp lệ.")
    elif pick == 3:
        c_pick=int(input("Nhập chỉ số cột muốn xuất: "))
        print(f"Cột {c_pick}:")
        if 0 < c_pick <= len(matrix[0]):
            for row in matrix:
                column = [row[c_pick-1]]
                print(column)
    elif pick == 4:
        max_num=max(max(row) for row in matrix)
        print(f"Số lớn nhất trong ma trận: {max_num}")
    elif pick == 0:
        print("Cảm ơn đã sử dụng! LOVE LOVE")
        break
    else:
        print("Vui lòng chọn đúng số trong menu")
        print("*" * 50)



