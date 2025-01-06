from C1.homework_24Jan02.func import q4, q1, q2, q3

while True:
    print(
        "LIST FUNCTION \n"
        "1. Frequency of occurrence of characters (decreasing) \n"
        "2. Check relationship of 2-word \n"
        "3. Finding out the longest common substring \n"
        "4. Charactes adsent (English alphabet)"
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
            print("じゃあね（Jaane)! ~ ByeBye \n"
                  "Japan Do")
            break
    print("*"*40)

