#Q1: 1. Viết chương trình cho phép: khởi tạo list; thêm phần tử vào list; nhập k, kiểm tra k xuất hiện bao nhiêu lần trong list;
# tính tổng các số nguyên tố trong list; sắp xếp; xóa list
from math import sqrt
#  2 2 4 5 6 7 7 7 8 99 88 66 55 67
def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range (2,int(sqrt(num))+1):  #Một số ko thể có ước số > căn bậc hai của nó, ngoại trừ chính nó.
            if num % i ==0:
                return False
        return True

n_lst=[]
while True:
    print("Menu")
    print("1. Tạo list mới (list rỗng)")
    print("2. Thêm phần tử vào list đã tạo")
    print("3. Kiểm tra số lần xuất hiện của phần tử trong list")
    print("4. Tính tổng các số nguyên tố trong list")
    print("5. Sắp xếp list")
    print("6. Xóa list")
    print("0. THOÁT")
    print("-"*30)
    pick=int(input("Chọn chức năng: "))
    if pick == 1:
        name_lst=input("Nhập tên list: ")
        print(f"Đã tạo list '{name_lst}' thành công!")
        print("*"*50)
        continue
    elif pick == 2:
        element=input("Nhập phần tử muốn thêm (chỉ nhập số nguyên): ")
        try:
            element = int(element)
        except ValueError:
            pass  # Giữ nguyên nếu là chuỗi
        n_lst += element.split(" ")
        while '' in n_lst:
            n_lst.remove('')
        #n_lst=n_lst.split(" ")
        print(f"Danh sách hiện tại: {n_lst}")
        print("*" * 50)
    elif pick == 3:
        print(f"Các phần tử trong list {set(n_lst)}")
        check=input("Nhập phần tử muốn kiểm tra:")
        c=n_lst.count(check)
        print(f"Phần tử {check} xuất hiện {c} lần trong list.")
        print("*" * 50)
    elif pick == 4:
        su=0
        for i in n_lst:
            if i == " " or i == "":
                continue
            else:
                i = int(i)
                if is_prime(i):
                    su += i
                else:
                    continue
        print(f"Tổng các số nguyên tố trong list = {su}")
        print("*" * 50)
    elif pick == 5:
        if not n_lst:
            print("Danh sách rỗng.")
        else:
            sort_lst=sorted(n_lst)
            print(f"Danh sách đã được sắp xếp: {sort_lst}")
            print("*" * 50)
    elif pick == 6:
        n_lst.clear()
        print(f"Danh sách đã được xóa thành công!")
        print("*" * 50)
    elif pick == 0:
        print("Cảm ơn đã sử dụng! LOVE LOVE")
        break
    else:
        print("Vui lòng chọn đúng số trong menu")
        print("*" * 50)








