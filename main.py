#hello

'''try:
    user_select = int(input("Введіть число від 1 до 7:"))
    match user_select:
        case 1:
            print("Понеділок")
        case 2:
            print("Вівторок")
        case 3:
            print("Середа")
        case 4:
            print("Четверг")
        case 5:
            print("П'ятниця")
        case 6:
            print("Субота")
        case 7:
            print("Неділя")
        case _:
            print("Введене число не входить в діапазон від 1 до 7.")
except ValueError:
    print("Введіть коректне число.")'''


'''
try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    if num1 == num2:
        print("Числа рівні.")
    else:
        smaller, larger = min(num1, num2), max(num1, num2)
        print(f"Числа не рівні. В порядку зростання:{smaller},{larger}")
except ValueError:
    print("Будь ласка, введіть коректні числа.")
'''



'''
try:
    num1 = float(input("Введіть перше число:"))
    num2 = float(input("Введіть друге число:"))
    operation = (input("Виберіть дію: +, -, /, *: "))
    match operation:
        case "+":
            print(num1 + num2)
        case "-":
            print(num2 - num1)
        case "*":
            print(num1 * num2)
        case "/":
            if num2 != 0:
                print(num1 / num2)
            else:
                print("На нуль ділити не можна")
        case _:
            print("Введене некоректне число")
except ValueError:
    print("Будь ласка, введіть коректні числа.")'''


