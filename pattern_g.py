def Pattern(l):
	pat=""
	for i in range(0,l):
		for j in range(0,l):	
			if ((j == 1 and i != 0 and i != l-1) or ((i == 0 or
				i == l-1) and j > 1 and j < l-2) or (i == ((l-1)/2)
				and j > l-5 and j < l-1) or (j == l-2 and
				i != 0 and i != l-1 and i >=((l-1)/2))):
				pat=pat+"*"
			else:	
				pat=pat+" "
		pat=pat+"\n"
	return pat
line = 7
print(Pattern(line))
