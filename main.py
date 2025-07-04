# Встроенные библиотеки
# PyPI - Python Package Index (pypi.org)
import random as r

zara = ['\u2680','\u2680','\u2680','\u2680','\u2680','\u2680'] # \u2680 - код кубика

for _ in range(10):
    print(r.choice(zara),r.choice(zara))
#--------------------------------------------------------------------
"""import random as r

d = {'a': 1,
     'b': 2,
     'c': 3}
keys = list(d.keys())

key = r.choice(keys)
print(d[key])"""