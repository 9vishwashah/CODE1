a = ((4, 'vishwa', 10), (3, 'is', 8), (6, 'Best', 10))
print("The original tuple : " + str(a))
res = [{'key': sub[0], 'value': sub[1], 'id': sub[2]}for sub in a]
print("The converted dictionary : " + str(res))
