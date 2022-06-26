def partition(a,l,h):
	i = ( l - 1 )
	x = a[h]
	for j in range(l , h):
		if a[j] <= x:
			i = i+1
			a[i],a[j] = a[j],a[i]
	a[i+1],a[h] = a[h],a[i+1]
	return (i+1)
def quickSortIterative(a,l,h):
	s = h - l + 1
	st = [0] * (s)
	t = -1
	t = t + 1
	st[t] = l
	t = t + 1
	st[t] = h
	while t >= 0:
		h = st[t]
		t = t - 1
		l = st[t]
		t = t - 1
		p = partition( a, l, h )
		if p-1 > l:
			t = t + 1
			st[t] = l
			t = t + 1
			st[t] = p - 1
		if p+1 < h:
			t = t + 1
			st[t] = p + 1
			t = t + 1
			st[t] = h
a = []
num = int(input("Enter number of elements : "))
for i in range(0, num):
	ele = int(input())
	a.append(ele) 
n = len(a)
quickSortIterative(a, 0, n-1)
print ("Sorted array is:")
for i in range(n):
	print ("%d" %a[i]),
