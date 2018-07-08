import module1

print(module1.__name__) #will be "module1" since its the name of the module we are importing

#A module is a file containing Python definitions and statements
#The file name is the module name with the suffix .py appended.
#Within a module, the module’s name (as a string) is available as the value of the global variable __name__

print(__name__)# will give the value "__main__" since this is the actual file we are running

#If you intend to use a function often you can assign it to a local name:

#import fibo will import module name
# from fibo import fib, fib2 : imports names from a module directly into the importing module’s symbol table
# a variant to import all names that a module defines:
#from fibo import *
#If the module name is followed by as, then the name following as is bound directly to the imported module.
#import fibo as fib
#fib.fib(500)

print(dir())
#It can also be used when utilising from with similar effects: