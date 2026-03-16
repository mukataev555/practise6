a = ["Python", "Java", "C++"]
for i, v in enumerate(a):
    print(i, v)

a = ["A", "B", "C"]
r = list(enumerate(a))
print(r)

d = {"a": 10, "b": 20}
for i, (k, v) in enumerate(d.items()):
    print(i, k, v)


a = [1, 2, 3]
b = ['a', 'b', 'c']

# No iterable are passed
res = zip()
print(list(res))

# One iterable is passed
res = zip(a)
print(list(res))

# Two iterables are passed
res = zip(a, b)
print(list(res))

a = [('Apple', 10), ('Banana', 20), ('Orange', 30)]
fruits, quantities = zip(*a)

print("Fruits:", fruits)
print("Quantities:", quantities)

d = {'name': 'Felix', 'age': 27, 'grade': 'A'}
keys = d.keys()
values = d.values()

res = zip(keys, values)
print(list(res))

