s="Tiger, Heniken, 333, Sapporo"
beer_print=s.split(',')
print(beer_print)
# Duyệt ds
# C1: for ... in (duyệt qua tất cả các phần tử trong list)
for beer in beer_print:
     print(beer)

#C2: duyệt chỉ mục index (có thể thêm điều kiện để lọc ra những đối tượng cần)
for i in range (len(beer_print)):   #or __len__()
    print(beer_print[i])



print("-"*20)
print("VD2")
text="khoa he thong thong tin luon ..."
#h, o, n xuất hiện nhiều nhất với 4 lần
text1=text.replace(" ","")
count=text1.split()
for i in range (len(count)):
    print
