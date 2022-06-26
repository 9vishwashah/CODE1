def partition(l, r, n):
	pivot, ptr = n[r], l
	for i in range(l, r):
		if n[i] <= pivot:
			n[i], n[ptr] = n[ptr], n[i]
			ptr += 1
	n[ptr], n[r] = n[r], n[ptr]
	return ptr
def quicksort(l, r, n):
	if len(n) == 1: 
		return n
	if l < r:
		pi = partition(l, r, n)
		quicksort(l, pi-1, n) 
		quicksort(pi+1, r, n) 
	return n
a = []
num = int(input("Enter number of elements : "))
for i in range(0, num):
	ele = int(input())
	a.append(ele) 
print(quicksort(0, len(a)-1, a))
