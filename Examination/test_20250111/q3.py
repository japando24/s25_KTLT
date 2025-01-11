#Câu 3: Viết phương thức nhận đối số đầu vào là một chuỗi và trả về kết quả xử lý là các ký tự nguyên âm (theo tiếng Anh) có tần suất xuất hiện nhiều nhất trong chuỗi không phân biệt chữ hoa chữ thường, không xét khoảng trắng.
# Ví dụ: Với chuỗi cho trước là “Faculty   of   Information    Systems  ” --> kết quả xử lý trả về là “Ký tự nguyên âm ‘o’ xuất hiện nhiều nhất trong chuỗi với số lần xuất hiện là 3.”
input_parameter = str(input("Enter your string input: "))

# no different about UPPER and lower and join
# trả về nguyên âm aeiou

parameter = input_parameter.lower().strip().replace(" ", "")
print(parameter)
list_vowel = []
for i in parameter:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        list_vowel.append(i)
print(f"So the list of vowels from input parameter string is: {list_vowel}")
print(f"The len of that vowels is {len(list_vowel)}")

vowels = "aeiou"

for vowel in vowels:
    print(f"The count of '{vowel}' is {list_vowel.count(vowel)}")

max_vowel = max(vowels, key=list_vowel.count)
max_count = list_vowel.count(max_vowel)
print(
    f"Ký tự vowels nguyên âm '{max_vowel}' xuấn hiện nhiều nhất với số lần xuất hiện là {max_count} lần."
)