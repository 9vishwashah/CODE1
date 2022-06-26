from itertools import chain
a = ([5, 6, 4, 6, 3, 1], [6, 7, 8, 9], [3])
print("The original tuple : " + str(a))
res = tuple(chain.from_iterable(a))
print("The flattened tuple : " + str(res))
