myList = [2,4,7,5]

print(myList.append(67))#will append 67 to the end of the list
print(myList)
#You will notice that methods like insert, remove or sort 
# that only modify the list have no return value printed – 
# they return the default None. [1] This is a design principle for all mutable data structures in Python.

#Extend the list by appending all the items from the iterable(anything that can be looped)
#for a string
myList.extend("emz")
print(myList)

#for a list
myList.extend(["sksk","ksksks","ssosos"])
print(myList)

#for a turple
myList.extend((993,34343,3434,343))
print(myList)

#for a dictionary
myList.extend({"name":"Sema", "last":"Emma"})#only adds keys of the dict
print(myList)

#just trying out
def listo(items):
    myList = []
    myList.extend(items)
    for name in myList:
        print(name)
listo("semutenga")

#list.insert(i,x)
#Insert an item at a given position. The first argument is the index of the element before 
#which to insert, so a.insert(0, x) 
#inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
    
myList.insert(0,"Nakasoma")
print(myList)

#list.remove(x)
#Remove the first item from the list whose value is x. It is an error if there is no such item.
myList.remove(67)

print(myList)

#list.pop([i])
#Remove the item at the given position in the list, and return it. If no index is specified,
#  a.pop() removes and returns the last item in the list. (The square brackets around 
# the i in the method signature denote that the parameter is optional, not that you 
# should type square brackets at that position. You will see this notation frequently 
# in the Python Library Reference.
#also returns the value that has been removed

myList.pop() #will remove and return the last item since position has not been specified

print(myList)

print(myList.pop(3)) #will remove and return the item at position specified

print(myList)

#list.clear()
#Remove all items from the list. Equivalent to del a[:].

#myList.clear()

#list.index(x[, start[, end]])
#Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.

print(myList.index(993, 0, len(myList)))
print(myList)

#Return the number of times x appears in the list.
print(myList.count(5))

#Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
#myList.sort(key=None, reverse=False)

#list.reverse()
#list.copy()

#using lists as stacks (last in first out by using .appen() and .pop() respectively)

#using Lists as queues (first in first out), lists are not efficient for this purpose i.e doing inserts and pops at the begining is slow


#To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves
queue.pop()

print(list(queue))                           # Remaining queue in order of arrival, also coverted it into a list

#List comprehensions
