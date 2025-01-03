org_s= ("Khoa  he   Thong   thong tin   luon")
org_s=org_s.lower() #đổi lại thành chữ thường

#1. Tính tần số xuất hiện nhiều nhất của ký tự
    #Input: khoa  he   hong   thong tin   luon  => khoaetngilu
out_s=""
for c in org_s:
    if c != " " and c not in out_s:
        out_s+=c
print(out_s) # => khoaetngilu

count_max=0
for c in out_s:
    count=org_s.count(c)
    if count > count_max:
        count_max = count
print(count_max)

#2. Liệt kê các ký tự có tần số xuất hiện == tần suất nhiều nhất
result_s=""
for c in out_s:
    if org_s.count(c) == count_max:
        result_s += c + ","
print(f'{result_s.rstrip(", ")} xuất hiện nhiều nhất {count_max} lần') # CÝ use dấu khác nhau để ko bị lỗi