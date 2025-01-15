# Q2: Viết chương trình cho phép:
# • Khởi tạo ngẫu nhiên n phần tử cho list.
# • Với k là một số nhập từ bàn phím, hãy xóa tất cả các phần tử có giá trị k tồn tại trong list.
# • Kiểm tra list có đối xứng hay không.
import random

while True:
    print("Menu")
    print("1. Khởi tạo ngẫu nhiên N phần tử")
    print("2. Xóa phần tử k trong list")
    print("3. Kiểm tra tính đối xứng")
    print("0. THOÁT")
    print("-"*30)
    pick=int(input("Chọn chức năng: "))

    if pick == 1:
        lst=[]
        num_start=int(input("Nhập số bắt đầu: "))
        num_end=int(input("Nhập số bắt đầu: "))
        N = int(input("Nhập số lượng phần tử (N):"))
        while len(lst) < N:
            random_list=int(random.randint(num_start,num_end)) #Tạm thời giới hạn lại trong khoảng 100
            lst.append(random_list)
        print(f"Dãy số: {str(lst).strip("[").strip("]")}")
        print("*"*50)
    elif pick == 2:
        delete=int(input("Nhập phần tử muốn xóa: "))
        if lst == "":
            print("Danh sách rỗng")
        else:
            while delete in lst:
                lst.remove(delete)
            print(f"Đã xóa phần tử {delete} thành công.")
            print(f"Dãy số cập nhật: {str(lst).strip("[").strip("]")}")
    elif pick == 3:
        if lst == "":
            print("Danh sách rỗng")
        else:
            if lst == lst[::-1]:
                print("Dãy số có tính đối xứng")
            else:
                print("Dãy số KHÔNG có tính đối xứng")

    elif pick == 0:
        print("Cảm ơn đã sử dụng! LOVE LOVE")
        break
    else:
        print("Vui lòng chọn đúng số trong menu")
        print("*" * 50)





