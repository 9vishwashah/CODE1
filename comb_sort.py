from array import array
def getNextGap(g):
	g = (g * 10)/13
	if g < 1:
		return 1
	return g
def combSort(a):
	n = len(a)
	g = n
	s = True
	while g !=1 or s == 1:
		g = getNextGap(g)
		s = False
		for i in range(0, n-g):
			if a[i] > a[i + g]:
				a[i], a[i + g]=a[i + g], a[i]
				s = True
a= []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	e = int(input())
	a.append(e) 
combSort(a)
print ("Sorted array:")
for i in range(len(a)):
	print (a[i]),