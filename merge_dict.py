def Merge(a, b):
	return(b.update(a))
a = {'a': 10, 'b': 8}
b = {'d': 6, 'c': 4}
print(Merge(a, b))
print(b)
