#Q6: Viết chương trình nhập vào một danh sách n số thực, sắp xếp và xuất dãy số theo thứ tự giảm dần
#test case: 6.6 8.9 5.5 1.4 1.0 10.8
raw=input("Nhập dãy số thực: ")
lst=raw.split(" ")
while '' in lst:
    lst.remove('')
num_lst=[]
for i in lst:
    i=float(i)
    num_lst.append(i)
sorted_lst=sorted(num_lst, reverse=True)
print(f"Dãy số thực sắp xếp giảm dần: {str(sorted_lst).strip("[").strip("]")}")
