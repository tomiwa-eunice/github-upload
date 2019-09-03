addressbook = {}
kate = ["0506717171", "Hengelosestraat99"]
clara = ["Langestraat 25", "clara@itc.nl"]
amy = ["0347252525", "amy@itc.nl"]
addressbook["Kate"] = kate
addressbook["Clara"] = clara
addressbook["Amy"] = amy
addressbook["Kate"] = ["0506717171", "Hengelosestraat99", "kate@itc.nl"]
addressbook["Clara"] = ["Langestraat 25", "clara@itc.nl", "0628363636"]
addressbook["Amy"] = ["0347252525", "amy@itc.nl", "Walstraat 90"]

print(addressbook)

#
#
# from functools import reduce
# even = lambda n:n%2 ==0
#
# x = filter_even(1, 2, 3, 4, 5)
# print(x)

import numpy as np

arrA = np.arange(8, 1, -1)
print(arrA)
print(arrA[np.array([2,3,2,4])])

yourTwoDimArray = np.arange(30).reshape(5,6)
print(yourTwoDimArray)
print(yourTwoDimArray[ np.array([0,2,3]), np.array([1,1,1]) ])