"""
NegativeNumberInStrings(str) xuất ra các số nguyên âm trong chuỗi
VD: Nếu nhập vào chuỗi "whdg-8bhl-68p8e--h" thì hàm phaải xuất ra được 2 số nguyên âm đó là -8 và -68
"""

def NegativeNumberInStrings(str):
    str="---8whdg-8bhl----68p8e--h-----0000hfhg---"
    sym=str.find("-")     #Nếu .find() không tìm thấy sẽ trả về -1
    res="-"
    while sym >= 0:
        i=sym+1
        while i< len(str) and str[i].isdigit():
            res += str[i]
            i +=1
        sym = str.find("-",sym+1)  # Nếu .find() không tìm
        res+= "\n" + "-"
        # thấy sẽ trả về -1
    return res

print(NegativeNumberInStrings(str))
