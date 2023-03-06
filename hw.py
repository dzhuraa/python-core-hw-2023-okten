# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
#
# 2) протипізувати перше завдання


# def notebook():
#     todo_list = []
#
#     def add_todo(todo: str):
#         nonlocal todo_list
#         todo_list.append(todo)
#
#     def get_all() -> print:
#         nonlocal todo_list
#         return print(todo_list)
#
#     return add_todo, get_all
#
#
# add_todo, get_all = notebook()
#
#
# add_todo("make a bed")
#
# get_all()
#
# add_todo("go shopping")
# add_todo("training")
# add_todo("homework")
# add_todo("eating")
# add_todo("sleeping")
#
# get_all()


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'


# def expanded_form(num: int) -> str:
#     num_str = str(num)[::-1]
#     nums = []
#
#     for i, digit in enumerate(num_str):
#         if digit == '0':
#             continue
#         nums.append(str(int(digit) * 10 ** i))
#
#     return ' + '.join(nums[::-1])
#
#
# print(expanded_form(12))


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій


# def decor(func):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         func()
#         print(count)
#
#     return inner
#
#
# @decor
# def func():
#     print("function called")
#
#
# func()
# func()
# func()
# func()
# func()
