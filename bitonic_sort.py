def compAndSwap(a, i, j, dire):
	if (dire==1 and a[i] > a[j]) or (dire==0 and a[i] > a[j]):
		a[i],a[j] = a[j],a[i]
def bitonicMerge(a, low, cnt, dire):
	if cnt > 1:
		k = cnt//2
		for i in range(low , low+k):
			compAndSwap(a, i, i+k, dire)
		bitonicMerge(a, low, k, dire)
		bitonicMerge(a, low+k, k, dire)
def bitonicSort(a, low, cnt,dire):
	if cnt > 1:
		k = cnt//2
		bitonicSort(a, low, k, 1)
		bitonicSort(a, low+k, k, 0)
		bitonicMerge(a, low, cnt, dire)
def sort(a,N, up):
	bitonicSort(a,0, N, up)
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
	ele = +int(input())
	a.append(ele) 
bubbleSort(a)
("Sorted array is:")
for i in range(len(a)):
	print("% d" % a[i], end=" ")
n = len(a)
up = 1
