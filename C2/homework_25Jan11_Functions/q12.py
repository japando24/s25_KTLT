#Q12: Viết hàm tính chỉ số BMI của một người khi biết chiều cao và cân nặng.
# Biếtrằng: BMI = Weight / (Height*Height).
# Cho biết tình trạng cân nặng của người này dựa trên tiêu chuẩn quốc tế như sau:
def calculate_bmi(w, h):
    if h <= 0 or w <= 0:
        raise ValueError("Your height and weight must greater than 0.")
    return w / (h ** 2)

def classify_bmi(bmi, categories=None):
    if categories is None:
        categories = [
            (18.5, "Gầy"),
            (25, "Bình thường"),
            (30, "Mập"),
            (float('inf'), "Béo phì"),
        ]

    if not categories:  # Nếu danh sách rỗng
        return "Không xác định"

    upper_limit, status = categories[0]  # Lấy giới hạn trên và trạng thái đầu tiên
    if bmi < upper_limit:
        return status
    return classify_bmi(bmi, categories[1:])  # Gọi đệ quy với phần còn lại


def bmi_status(w, h):
    bmi = calculate_bmi(w,h)
    status = classify_bmi(bmi)
    return bmi, status



w= 77
h= 1.73
bmi, status = bmi_status(w, h)
print(f"BMI: {bmi:.2f}, Tình trạng cân nặng: {status}")