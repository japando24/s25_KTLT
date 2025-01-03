org_s= ("Khoa  he   Thong   thong tin   luon")
org_s=org_s.lower() #đổi lại thành chữ thường
out_s=""
#TỐI ƯU HÓA HÀM
count_max=0
res_s=""
for c in org_s:
    if c != " " and c not in out_s:
        out_s+=c
for c in out_s:
    count=org_s.count(c)
    if count > count_max:
        count_max=count
        res_s = c+","
    elif count == count_max:
        res_s +=c+","
print(f'{res_s.rstrip(",")} xuất hiện nhiều nhất {count_max} lần')