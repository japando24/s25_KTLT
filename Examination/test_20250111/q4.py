#Câu 4: Viết phương thức nhận đối số đầu vào là một danh sách với các phần tử có giá trị bất kỳ (bao gồm số nguyên dương và chuỗi), phương thức xử lý trả về kết quả là các phần tử có tần suất xuất hiện nhiều nhất trong danh sách (không phân biệt chữ hoa chữ thường, không xét khoảng trắng đối với phần tử có giá trị kiểu chuỗi). Ví dụ: Với danh sách cho trước là [‘Hello ’, 4, 8, 6, 4, 6, ‘he   ll o’, 9, ‘Welcome’ ] --> kết quả xử lý trả về là “Phần tử ‘Hello’, 4, ‘he  ll o’, 6 xuất hiện nhiều nhất trong danh sách với số lần xuất hiện là 2.”
from collections import Counter

def normal_string(s):
    return ''.join(c.lower() for c in s if not c.isspace())

def find(input_list):
    # Dictionary để lưu giá trị chuẩn hóa và số lần xuất hiện
    counter = Counter()
    original_map = {}

    for item in input_list:
        if isinstance(item, str):
            v = normal_string(item)
        else:
            v = str(item)

        counter[v] += 1
        original_map[v] = item

    # Tìm tần suất xuất hiện lớn nhất
    max_frequency = max(counter.values())

    # Lấy các phần tử có tần suất xuất hiện bằng tần suất lớn nhất
    most_frequent_elements = [original_map[key] for key, count in counter.items() if count == max_frequency]

    # In kết quả
    print(f"Phần tử {', '.join(map(str, most_frequent_elements))} xuất hiện nhiều nhất trong danh sách với số lần xuất hiện là {max_frequency}.")

# Ví dụ danh sách đầu vào
input_list = ['Hello ', 4, 8, 6, 4, 6, 'he   ll o', 9, 'Welcome']
find(input_list)
