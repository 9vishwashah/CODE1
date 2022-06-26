def binarySearch(a, item, low, high):
	while (low <= high):
		mid = low + (high - low) // 2
		if (item == a[mid]):
			return mid + 1
		elif (item > a[mid]):
			low = mid + 1
		else:
			high = mid - 1
	return low
def insertionSort(a, n):
	for i in range (n):
		j = i - 1
		selected = a[i]
		loc = binarySearch(a, selected, 0, j)
		while (j >= loc):
			a[j + 1] = a[j]
			j-=1
		a[j + 1] = selected
a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	a.append(ele) 
n = len(a)
insertionSort(a, n)
print("Sorted array: ")
for i in range (n):
	print(a[i], end=" ")
