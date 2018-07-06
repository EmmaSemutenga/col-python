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

if fib(2000) == None:
    print("indeed, it actually returns nothing")

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
            return #will cause function to exit with None return type

ask_me("please Insert name : ")

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

#order is not important
#No argument may receive a value more than once
#When a final formal parameter of the form **name is present, it receives a dictionary
#When a formal parameter of the form *name is present, it receives a turple
#*name must occur before **name

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print(type(arguments))
    for arg in arguments:
        print(arg)
    print("-" * 40)
    print(type(keywords))
    for kw in keywords:
        print(kw, ":" ,keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.", "It's really very, VERY runny, sir.", shopkeeper="Michael Palin", client="John Cleese", sketch="Cheese Shop Sketch")

#Arbitrary Argument Lists¶
#a function can be called with an arbitrary(random) number of arguments. These arguments will be wrapped up in a tuple

def write_multiple_items(file, separator, *args, elinya):
    for a in args:
        print("hey ", file, " am just here testing ", separator, elinya, " and its ",a )

write_multiple_items("file one", ":)", "Limburger", "It's very runny, sir.", "It's really very, VERY runny, sir.", elinya="sema")

#Before the variable number of arguments, zero or more normal arguments may occur.
#Normally, these variadic arguments will be last in the list of formal parameters, because they scoop up all remaining input arguments
#  that are passed to the function. Any formal parameters which occur after the *args parameter are
#  ‘keyword-only’ arguments, meaning that they can only be used as keywords rather than positional arguments

#Unpacking Argument Lists¶
#The reverse situation occurs when the arguments are already in a list or tuple but need 
# to be unpacked for a function call requiring separate positional arguments.
#  For instance, the built-in range() function expects separate start and stop arguments. 
# If they are not available separately, write the function call with the *-operator to 
# unpack the arguments out of a list or tuple:

list(range(3, 6))            # normal call with separate arguments

args = [3, 6]
print(list(range(*args)))            # call with arguments unpacked from a list

def kokya(ages):
    for i, age in enumerate(ages):
        print(f"student {i} is {age} years")

choices = [2,8]
kokya(list(range(*choices)))

#In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

#Lambda Expressions
#Small anonymous functions can be created with the lambda keyword. 

#Documentation Strings
#The first line should always be a short, concise summary of the object’s purpose.
#This line should begin with a capital letter and end with a period.
#If there are more lines in the documentation string, the second line should be blank, 
#visually separating the summary from the rest of the description. The following lines
#should be one or more paragraphs describing the object’s calling conventions, its side effects, etc
#multiline doc string

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

#Function Annotations¶
