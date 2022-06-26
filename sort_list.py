a = [{ "name" : "sam", "age" : 45},
{ "name" : "chris", "age" : 30 },
{ "name" : "tony" , "age" : 15 }]
print ("The list printed sorting by age: ")
print (sorted(a, key = lambda i: i['age']))
print ("\r")
print ("The list printed sorting by age and name: ")
print (sorted(a, key = lambda i: (i['age'], i['name'])))
print ("\r")
print ("The list printed sorting by age in descending order: ")
print (sorted(a, key = lambda i: i['age'],reverse=True))
