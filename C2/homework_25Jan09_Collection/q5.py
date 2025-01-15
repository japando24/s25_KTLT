#Q5: Viết chương trình nhập vào một dãy các số theo thứ tự tăng, nếu nhập sai quy cách thì yêu cầu nhập lại.
# In dãy số sau khi đã nhập xong.
#test case: 5 6 7 8 9 19 191 988 999
raw=input("Nhập dãy số theo thứ tự tăng dần: ")
lst=raw.split(" ")
l=len(lst)
c=0
for i in range (l-1):
    if int(lst[i]) > int(lst[i+1]):
        raw = input("Nhập lại dãy số theo thứ tự tăng dần: ")
    else:
        res=lst
print(f"Dãy số: {str(res).strip("[").strip("]")}")


