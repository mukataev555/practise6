def double(n):
    return n * 2

n = [5, 6, 7, 8]
res = map(double, n)
print(list(res))

import functools

n = [1, 2, 3, 4]

prod = functools.reduce(lambda x, y: x * y, n)
print(prod)

def is_even(n):
    return n % 2 == 0

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

en = filter(is_even, n)
print(list(en))

from functools import reduce

n = [1, 2, 3, 4, 5, 6]

e = filter(lambda x: x % 2 == 0, n)
s = map(lambda x: x**2, e)
res = reduce(lambda x, y: x + y, s)

print(res)

from functools import reduce

n = [-3, -1, 2, 4, -2, 5]

res = reduce(lambda x, y: x * y,map(lambda x: x,filter(lambda x: x > 0, n)))

print(res)

from functools import reduce

w = ["sky", "apple", "tree", "gym", "orange"]

res = reduce(lambda a, b: a + b,map(lambda w: len(w),filter(lambda w: any(v in w for v in 'aeiou'), w)))

print(res)

