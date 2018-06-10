#control flows

#while loop
# Fibonacci series:
# the sum of two elements defines the next
#non-zero integer value is true; zero is false
#anything with a non-zero length is true, empty sequences are false

#indentation is Python’s way of grouping statements

a, b = 0, 1 #multiple assignments
while b < 10:
    print(b, end='') #The keyword argument end can be used to avoid the newline after the output
    print(b, end=', ') #or end the output with a different string:
    a, b = b, a+b #the right hand expresions are evaluated from the left to the right

#the print function
i = 256*256
print('The value of i is', i) 

x = int(input('Please insert number'))

if x < 0:
    x = 0
    print("X is negative")
elif x == 0:
    print("X is Zero")
else:
    print("x is greater than zero")

#An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages

#for loop
#iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

#If you need to modify the sequence you are iterating over while inside the loop 
# (for example to duplicate selected items), 
# it is recommended that you first make a copy

for w in words[:]:#making a copy
    if len(w) > 6:
        words.insert(0, w)
print(words)

#range() Function
#iterates over a sequence of numbers
for i in range(6):#last number(given endpoint) is never part of the sequence
    print(i)

#let range start from another number
for n in range(-5, 2):#begins at -5
    print(n)

for m in range(0, 10, 2):#starts at 0 to 10(not included) in steps of 2
    print(m)

#To iterate over the indices of a sequence, you can combine range() and len()
for v in range(len(words)):
    print(v, words[v])

#In most such cases, however, it is convenient to use the enumerate()

for k, j in enumerate(words):
    print(k, j)

#The function list() it creates lists from iterables:

print(list(range(5)))
print(list(range(-1,10)))#from -1 to 9