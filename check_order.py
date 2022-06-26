from collections import OrderedDict
def checkOrder(a, b):
	dict = OrderedDict.fromkeys(a)
	n = 0
	for key,value in dict.items():
		if (key == b[n]):
			n = n + 1
		if (n == (len(b))):
			return 'true'
	return 'false'
if __name__ == "__main__":
	a = 'Vishwa Shah'
	b = 'wh'
	print (checkOrder(a,b))
