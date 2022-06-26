from collections import OrderedDict
a = OrderedDict([('tony', '1'), ('sam', '2')])
b = OrderedDict([("chris", '4'), ("tom", '4')])
both = OrderedDict(list(b.items()) + list(a.items()))
print ("Resultant Dictionary :"+str(both))
