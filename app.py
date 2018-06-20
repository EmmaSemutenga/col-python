#functions
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        #print(a, end=' ')
        a, b = b, a+b
    #print()

# Now call the function we just defined:
print(fib(2000))#will return None

#even functions without a return statement do return a value called None

#The return statement returns with a value from a function. return without an expression 
#argument returns None. Falling off the end of a function also returns None.



name = "semutenga"
print(name.replace("se", "mi"))#doesn't change the actual name string(immutable) but creates a new string 
print(name)

#Default Argument Values

def ask_me(name, age=18, trys=4):
    while True:
        elinya = input(name)
        if elinya in ('emz', 'mimi', 'baibe'):
            return "You are the one"
        elif elinya in ('naa', 'n', 'nope'):
            return "You are not the one"
        trys -=1
        if trys < 1:
            #return
            #raise ValueError('invalid user response')
            return

ask_me("please Insert name : ")

#metasplot
#harvester
#The default value is evaluated only once. This makes a difference 
# when the default is a mutable object such as a list, dictionary, or instances of most classes, the default to be shared between subsequent calls

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#If you don’t want the default to be shared between subsequent calls,
#you can write the function like this instead:
def f2(a, L=None):
    L=[]
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3))

def emz():
    name = "Jane"
print(emz())#no return value but it will return None

#function key arguments

def keyargs(firstName, secondName, joiner = "and"):
    print("Your firstname is: ", firstName, joiner, secondName)

keyargs("semutenga", "emmanuel", "nnn")

#In a function call, keyword arguments must follow positional arguments.
#keyargs(joiner = "and", "semutenga", "emmanuel" ) SyntaxError: positional argument follows keyword argument
keyargs("semutenga", "emmanuel", joiner = "and")
keyargs(joiner = "and", secondName = "emmanuel", firstName = "semutenga")