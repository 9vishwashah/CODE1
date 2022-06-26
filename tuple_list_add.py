l = []
num = int(input("number of elements you want to enter in tuple list: "))
for i in range(1, num + 1):
	a= int(input("{0}st element: ".format(i)))
	l.append(a)
t = []
num = int(input("number of elements you want to enter in test tuple: "))
for i in range(1, num + 1):
	a= int(input("{0}st element: ".format(i)))
	t.append(a)
res = tuple(list(t) + l)
print("The container after addition : " + str(res))
