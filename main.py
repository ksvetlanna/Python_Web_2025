# Декораторы
# Выводит большими буквами сообщение
def upper_case_print(old_func):
    def new_func(*args, **kwargs):
        args_up_case = [str(arg).upper() for arg in args]
        old_func(*args_up_case, **kwargs)
    return new_func
new_print = upper_case_print(print)
new_print('Привет, Пока')