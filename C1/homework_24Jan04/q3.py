#Q3: Viết hàm với tên NegativeNumberInStrings(str) xuất ra các số nguyên âm trong chuỗi.
#Vd: Nếu nhập vào chuỗi “akg-6bhl-79p8e--h” thì hàm phải xuất ra được 2 số nguyên âm đó là -6 và -79.
#Demo
s="---------5wh-------000006akg-6bhl-79p8e--h-0--9"
def q3():
    res=""
    l=len(s)
    i=0
    while i<l-1:
        if s[i] == "-" and s[i+1].isdigit():
            j=i+2
            while j<l:
                if not s[j].isdigit():
                    break
                j +=1
            if j >= i+2:
                if s[i:j] not in res:
                    res += str(int(s[i:j])) + ","
                i=j
        else:
            i +=1
    print(res.rstrip(", "))



