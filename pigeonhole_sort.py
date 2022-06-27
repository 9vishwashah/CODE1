def pigeonhole_sort(a):
	my_min = min(a)
	my_max = max(a)
	s = my_max - my_min + 1
	h = [0] * s
	for x in a:
		assert type(x) is int, "integers only please"
		h[x - my_min] += 1
	i = 0
	for c in range(s):
		while h[c] > 0:
			h[c] -= 1
			a[i] = c + my_min
			i += 1
a = []
num = int(input("Enter number of elements : "))
for i in range(0, num):
	ele = int(input())
	a.append(ele) 
print("Sorted order is :")
pigeonhole_sort(a)
for i in range(0, len(a)):
	#print(a[i], end =" ")
    print ("%d" %a[i])