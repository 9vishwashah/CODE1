import sys
def bubbleSort(a):
	n = len(a)
	s = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if a[j] > a[j + 1]:
				s = True
				a[j], a[j + 1] = a[j + 1], a[j]
		if not s:
			return
a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	a.append(ele) 
bubbleSort(a)
print("Sorted array is:")
for i in range(len(a)):
	print("% d" % a[i], end=" ")
