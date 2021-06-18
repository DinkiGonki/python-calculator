import math
try:
    x = float(input("Введите число 1"))
    y = float(input("Введите число 2"))
    z = input("""Выберите действие:
                        1-сложение 
                        2-вычитание 
                        3-умноэение 
                        4-дэление 
                        5-степень""")

    if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float) :
        if z == "1":
            if x+y % 1 == 0:
                print(int(x+y))
            else:
                print(x+y)
        elif z == "2":
            if x-y % 1 == 0:
                print(int(x-y))
            else:
                print(x-y)
        elif z == "3":
            if x*y % 1 == 0:
                print(int(x*y))
            else:
                print(x*y)  
        elif z == "4":
            if x/y % 1 == 0:
                print(int(x/y))
            else:
                print(x/y)
        elif z == "5":
            if pow(x , y) % 1 == 0:
                print(int(pow(x , y)))
            else:
                print(pow(x , y))
        else: 
            print("ты ебанат?")

    else:
        print('тебе 0 лет')

except:
    print("ошибка")
