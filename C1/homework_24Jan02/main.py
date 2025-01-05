from C1.homework_24Jan02.func import q4

print(
    "LIST FUNCTION \n"
    "1. Frequency of occurrence of characters \n"
    "4. Charactes adsent"
)

print("-"*30)
pick=input("Please choose the function you want to use: ")
match pick:
    case "1":
        q1()
    case "2":
        q2()
    case "3":
        q3()
    case "4":
        q4()
    case _:
        print("じゃあね（Jaane)!")

