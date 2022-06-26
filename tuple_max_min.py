a = (5, 20, 3, 7, 6, 8,100,1,25,85,70,60)
print("The original tuple is : " + str(a))
n = int(input("Enter the digit:\n"))
res = []
a = list(sorted(a))
for idx, val in enumerate(a):
	if idx < n or idx >= len(a) - n:
		res.append(val)
res = tuple(res)
print("The extracted values : " + str(res))
