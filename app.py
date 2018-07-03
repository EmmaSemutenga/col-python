#lists
squares = [1, 4, 9, 16, 25]

#Like strings (and all other built-in sequence type), lists can be indexed and sliced:

#All slice operations return a new list containing the requested elements

squares[:] #returns shallow copy of list in question list.copy() does the same job

#Lists also support operations like concatenation:

newlst = squares + [7,9,5,4]

print(newlst)

#lists are a mutable type, i.e. it is possible to change their content:

squares[0] = 6

print(squares)

#add new items at the end of the list, by using the append() method

squares.append([8])

print(squares)

# replace some values
squares[2:5] = ['C', 'D', 'E']

print(squares)

#removing elements I have just added
squares[2:5] = []

print(squares)


#removing all elements
squares[:] = [] #list.clear() does the same job

print(squares)

#built-in function len() also applies to lists:

print(len(squares))

#It is possible to nest lists (create lists containing other lists)