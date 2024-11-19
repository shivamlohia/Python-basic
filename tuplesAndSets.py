tpl = (1,2,3,4,5)
#tuples act as a list/array; objects are immutable, i.e., tpl[0] = x will throw an error; we can add new items to the tuple
print(tpl)
print(tpl[1:3])

tpl2 = (5,6,7,8)
tpl += tpl2
print("tpl after new elements", tpl)
print("tpl count of 5", tpl.count(5))
print("Index of first 5", tpl.index(5))


#Sets - only unique elements can be added
setA = {1,2,3,4,5}
setB = set([4,5,5,6,7,7])
print("A", setA)
print("B", setB)
print("Union", setA | setB)

print("Intersection", setA & setB)

print("Difference", setA - setB)

print("Symmetric difference", setA ^ setB)

#add - to add; remove/discard - same purpose, remove element;clear - empty set
setA.add(6)
setA.add(7)
print(setA)
setA.remove(6)
print(setA)
setA.discard(7)
print(setA)
setC = {1,2,3,4,5}
setA.clear()
print(setA)

#Check element in set
print(setC)
print(2 in setC)
print(7 in setC)