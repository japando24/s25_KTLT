#Q1: Viết hàm kiểm tra Chuỗi có đối xứng hay không?
# Vd: với chuỗi “madam”,“radar”, “mom” à True, chuỗi “hello” à False.
#Demo

#Test case
#odd_word="madam"
#even_word="noon" #deed, peep, anna, otto
def q1():
    word=input("Enter your word: ")
    list0=list(word)
    l=len(list0)
    c=0
    if l%2 != 0:
        odd=int((l-1)/2)
        for i in range (odd):
            if list0[i]==list0[l-i-1]:
                c=c+1
            else:
                continue
        if c == odd:
            print("This odd word is symmetrical.")
        elif c != odd:
            print("This odd word is NOT symmetrical.")
    else:
        even=int(l/2)
        for i in range(even):
            if list0[i] == list0[l-i-1]:
                c = c + 1
            else:
                continue
        if c == even:
            print("This even word is symmetrical.")
        elif c != even:
            print("This even word is NOT symmetrical.")

while True:
    q1()