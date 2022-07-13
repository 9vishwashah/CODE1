from collections import OrderedDict
def checkOrder(a, b):
	dict = OrderedDict.fromkeys(a)
	n = 0
	for key,value in dict.items():
		if (key == b[n]):
			n = n + 1
		if (n == (len(b))):
			return 'true the entered char is in order'
	return 'false entered char is not in order'
if __name__ == "__main__":
	a = input("Enter the String\n")
	b = input("Enter letter you want to check in order\n")
	print (checkOrder(a,b))
