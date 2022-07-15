from itertools import product
a = {'num' : [1, 2, 3],
     'month' : ['Jan', 'Feb', 'March']}
print("The original dictionary is : " + str(a))
res = dict(zip(a['num'], a['month']))
print("Flattened dictionary : " + str(res))
