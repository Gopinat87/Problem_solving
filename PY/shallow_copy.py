import copy

a = [[1, 2], [3, 4]]
b = a.copy()
c = copy.deepcopy(a)

a[0][0] = 99

print(a)
print(b)
print(c)