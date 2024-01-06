#hello

try:
    user_select = int(input("Введіть число від 1 до 7:"))
    if user_select == 1:
        print("Понеділок")
    elif user_select == 2:
        print("Вівторок")
    elif user_select == 3:
        print("Середа")
    elif user_select == 4:
        print("Четверг")
    elif user_select == 5:
        print("П'ятниця")
    elif user_select == 6:
        print("Субота")
    elif user_select == 7:
        print("Неділя")
    else:
        print("Введене число не входить в діапазон від 1 до 7.")
except ValueError:
    print("Введіть коректне число.")
