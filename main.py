# Декораторы
# Выводит большими буквами сообщение
def upper_case_print(old_func):
    def new_func(*args, **kwargs):
        case = kwargs.pop('case', None)
        if case == 'U':
            args = [str(arg).upper() for arg in args]
        if case == 'L':
            args = [str(arg).lower() for arg in args]
        return old_func(*args, **kwargs)
    return new_func
new_print = upper_case_print(print)
new_print('Привет, Пока')
new_print('Привет, Пока', case='U')