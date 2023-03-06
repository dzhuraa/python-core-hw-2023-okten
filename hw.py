#1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
# 2) протипізувати перше завдання


def notebook():
    todo_list = []

    def add_todo(todo: str):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all():
        nonlocal todo_list
        return print(todo_list)

    return add_todo, get_all


add_todo, get_all = notebook()


add_todo("make a bed")

get_all()

add_todo("go shopping")
add_todo("training")
add_todo("homework")
add_todo("eating")
add_todo("sleeping")

get_all()
