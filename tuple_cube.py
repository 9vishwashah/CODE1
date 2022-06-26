l = []
num = int(input("number of elements you want to enter in list: "))
for i in range(1, num + 1):
	a= int(input("{0}st element: ".format(i)))
	l.append(a)
#list1 = [1, 2, 5, 6]
res = [(val, pow(val, 3)) for val in l]
print("The Cube of Given Tuple are:")
print(res)
