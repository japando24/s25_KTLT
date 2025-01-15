#Q4: Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU
import random

unique_list=set()
print("Giới hạn các số từ 0 - 1000")
N = int(input("Nhập số lượng phần tử (N):"))
while len(unique_list) < N:
    random_list=int(random.randint(0,1000)) #Tạm thời giới hạn lại trong khoảng 1000
    unique_list.add(random_list)
print(unique_list)

