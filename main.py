# Встроенные библиотеки
# PyPI - Python Package Index (pypi.org)

# import math as m
#print('Число Пи:', m.pi, 'Квадратный корень: ', m.sqrt(4))

from math import (pi,
                  sqrt,
                  sin,
                  radians, hypot
                  )

print('Число Пи:', round(pi,2), 'Квадратный корень: ', sqrt(4))
print('Синус 30',chr(176),':', round(sin(radians(30)),2))
print('Гипотенуза для 3 и 2:', hypot(3,2))

#print(help(m.cos)) посмотреть информацию о функции