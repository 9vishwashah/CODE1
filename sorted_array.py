def insertionSort(a):
	for i in range(1, len(a)):
		key = a[i]
		j = i-1
		while j >=0 and key < a[j] :
				a[j+1] = a[j]
				j -= 1
		a[j+1] = key
a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	a.append(ele) 
insertionSort(a)
print ("Sorted array is:")
for i in range(len(a)):
	print ("%d" %a[i])
