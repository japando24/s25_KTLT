#Câu 4: Viết phương thức nhận đối số đầu vào là một danh sách với các phần tử có giá trị bất kỳ (bao gồm số nguyên dương và chuỗi), phương thức xử lý trả về kết quả là các phần tử có tần suất xuất hiện nhiều nhất trong danh sách (không phân biệt chữ hoa chữ thường, không xét khoảng trắng đối với phần tử có giá trị kiểu chuỗi).
# Ví dụ: Với danh sách cho trước là [‘Hello ’, 4, 8, 6, 4, 6, ‘he   ll o’, 9, ‘Welcome’ ] --> kết quả xử lý trả về là “Phần tử ‘Hello’, 4, ‘he  ll o’, 6 xuất hiện nhiều nhất trong danh sách với số lần xuất hiện là 2.”

from C2.L6.func import standardize

l= ["Hello ", 4, 8, 6, 4, 6, "he   ll o", 9, "Welcome"]
#1. Chuẩn hóa các phần tử có kiểu chuỗi trong list
length=len(l)
for i in range (length):
    if type(l[i]) is str:
        l[i] = standardize(l[i])
#2. Đếm tần suất xuất hiện của các phần tử
#3. In ra các phần tử có tần xuất nhiều nhất
c_max=0
res=[]
lst=list(set(l))
for i in lst:
    c=l.count(i)
    if c > c_max:
        c_max=c
        res = [i]
    elif c==c_max:
        res.append(i)

