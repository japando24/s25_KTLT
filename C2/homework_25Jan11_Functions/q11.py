#Q11: Viết hàm giải phương trình bậc 2 (ax2 + bx + c = 0).
import math
def PTB2_dq(a, b, c, step=0, D=None):
    if step == 0:
        if b == 0 and c != 0:
            print(f"The equation {a}x**2 + {b}x + {c} = 0")
            print("NO SOLUTIONS!")

        elif b == 0 and c == 0:
            print(f"The equation {a}x**2 + {b}x + {c} = 0")
            print("INFINITE SOLUTIONS!")

        else:
            print(f"The equation {a}x**2 + {b}x + {c} = 0")
            print(f"x={-c/b}")
        return PTB2_dq(a, b, c, step + 1)

    elif step == 1:
        D = b ** 2 - 4 * a * c
        return PTB2_dq(a, b, c, step + 2, D)

    elif step == 2:
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            print(f"The equation {a}x**2 + {b}x + {c} = 0")
            print(f"Two distinct solutions: x1={x1}, x2={x2}")
        elif D == 0:
            x = -b / (2 * a)
            print(f"The equation {a}x**2 + {b}x + {c} = 0")
            print(f"Double solution: x1=x2={x}")
        else:
            print(f"The equation {a}x**2 + {b}x + {c} = 0")
            print("NO SOLUTIONS!")


# Ví dụ sử dụng
a = 1
b = -3
c = 2

result = PTB2_dq(a, b, c)
print(result)
