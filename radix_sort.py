def countingSort(a, e1):
	n = len(a)
	output = [0] * (n)
	count = [0] * (10)
	for i in range(0, n):
		index = (a[i]/e1)
		count[int((index)%10)] += 1
	for i in range(1,10):
		count[i] += count[i-1]
	i = n-1
	while i>=0:
		index = (a[i]/e1)
		output[ count[ int((index)%10) ] - 1] = a[i]
		count[int((index)%10)] -= 1
		i -= 1
	i = 0
	for i in range(0,len(a)):
		a[i] = output[i]
def radixSort(a):
	max1 = max(a)
	exp = 1
	while max1/exp > 0:
		countingSort(a,exp)
		exp *= 10
a = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	a.append(ele) 
radixSort(a)
print("Sorted Elements are:")
for i in range(len(a)):
	print(a[i],end=" ")
