from functools import reduce
square = lambda x: x*x
l = [1,2,3,4, 5]
c = map(square, l)
print(list(c))
greater = lambda x: x>4
a = [1, 2, 3, 4, 54,67, 81, 8, 89 ]
d = filter(greater, a)
print(list(d))
sum = lambda x, y: x+y
a = [1, 2, 3, 7]
d = reduce(sum, a)
print(d)
