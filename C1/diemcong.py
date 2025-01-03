org_s= ("Khoa  he   Thong   thong tin   luon")
org_s=org_s.lower()
out_s=""
count_max=0
result=""
for c in org_s:
    if c != " " and c not in out_s:
        out_s+=c
        if org_s.count(c) > count_max:
            count_max = org_s.count(c)
            result = c
        elif org_s.count(c) == count_max:
            result +=c

print(",".join(result), f'xuất hiện nhiều nhất {count_max} lần')


