# Применение is на практике
def print_array(array: list, start: int=None):
    if start is not None and start > len(array):
        return
    if start is None:
        start = 0
    for i in range(start, len(array)):
            print(array[i])



a = [1,2,3]
print_array(a)