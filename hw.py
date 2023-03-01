


# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому.



# input_string = input("Enter letters and numbers: ")
#
# num = []
#
# for i in input_string:
#     if i.isdigit():
#         num.append(i)
#
# print(','.join(num))



# list comprehension 1



# greeting = 'Hello, world'
#
# new_greeting = greeting.upper()
#
# print(list(new_greeting))



# list comprehension 2


# num = []
#
# i = 0
#
# while i < 50:
#     new_num = i
#     if (new_num % 2) != 0:
#         new_num **= 2
#         num.append(new_num)
#     i += 1
#
# print(num)



#створити функцію яка виводить ліст


# def func(*args):
#     print(args)
#
#
# func(1,2,3,4,5,6,7,8)



#створити функцію яка приймає три числа та виводить та повертає найбільше.



# def func(a, b, c):
#     arr = [a, b, c]
#     max_num = max(arr)
#     print(max_num)
#
#
# func(100, 15, 249)



#створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.


# def func(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#
#
# func(3, 8, 10)


#Дан list:
#  list = [22, 3,5,2,8,2,-23, 8,23,5]
#  - знайти мін число
#  - видалити усі дублікати
#  - замінити кожне 4-те значення на 'X'

# list = [22, 3,5,2,8,2,-23, 8,23,5]
#
# print('min: ', min(list))
#
# print(set(list))



#квадрат



def square(size):
    for a in range(size):
        for b in range(size):
            if a == 0 or a == size-1 or b == 0 or b == size-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()



#таблиця множення



def multiplication_table():
    a = 1
    while a <= 9:
        b = 1
        while b <= 9:
            print(a*b, end="\t")
            b += 1
        print()
        a += 1

#меню



def menu():
    print('1. Вивести таблицю множення ')
    print()
    print('2. Намалювати квадрат')
    print()

    action = int(input('Виберіть завдання: '))

    if action == 1 or action == 2:
        if action == 1:
            multiplication_table()
        elif action == 2:
            size = int(input('Напишіть довжину сторони квадрату: '))
            square(size)
    else:
        print('Такого завдання не існує! Виберіть завдання 1 або 2.')


menu()
