#strings

name = 'Semutenga' # single quotes

name2 = "Semutenga Emmanuel" # double quotes

phrase = 'Semutenga\'s world' #escaping string using the back slash

phrase2 = 'Semutenga\'s world' #escaping string using double quotes

s = 'First line.\nSecond line.'  # \n add a new line

print(phrase)

print(s)

print(r'C:\some\name')  # using r before helps ignore the \ slash

#for strings that span for more than one line use """___ """ or '''___'''

print("""hey brother, the 
is an endless road to \
discover""")

#forward slash will remove the new line when put at end of line

#string concatenation and repeation

print(3 * 'un' + 'ium')

#Two or more string literals next to each other are automatically concatenated, only works with two literals, used to break long strings

print('Py' 'thon')

#Strings can be indexed with the first character having index 0

word = 'Python'
print(word[0])  # character in position 0

print(word[-1])  # last character

#obtaining substrings by slicing
print(word[0:2])  # characters from position 0 (included) to 2 (excluded) 
print(word)
print(word[2:len(word)])  # characters from position 2 (included) to 5 (excluded)

print(word[:2] + word[2:]) # is equal to Python

#Python strings cannot be changed — they are immutable

#built-in function len() returns the length of a string