from itertools import chain
test_dict = {'vishwa' : [5, 6, 7, 8],
			'alpesh' : [10, 11, 7, 5],
			'shah' : [6, 12, 10, 8],
			'vishu' : [1, 2, 5]}
print("The original dictionary is : " + str(test_dict))
res = list(sorted(set(chain(*test_dict.values()))))
print("The unique values list is : " + str(res))
