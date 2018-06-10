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

#Default Argument Values

name = "semutenga"
print(name.replace("se", "mi"))#doesn't change the actual name string(immutable) but creates a new string 
print(name)