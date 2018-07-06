#Write a program that checks if a word supplied as the argument is an Isogram. 
# An Isogram is a word in which no letter occurs more than once.

def isogram(word):
    print(word.count("z"))
    for w in word:
        if word.count(w) == 0:#is not every usefull
            print("letter doesn't exist")
            return
        elif word.count(w) == 1:
            print("Yess, this is an isogram")
            return (word, False)
        else:
            print("No it is not an isogram")
            return
        #print(list(word).count("z"))
        #print(w, end=" ,")

print(type(isogram("semuteeenga")))

def is_isogram(word):
    if type(word) != str:
        raise TypeError('Argument should be a string')

    elif (len(word) < 1):
         return ("argument", False)
    else:
       
        for char in word:
            if word.count(char) > 1 or not word.isalpha():
                return (word, False)
            else:
                return (word, True)

print(is_isogram("semutenga"))

print("semutenga".count("e"))

def nu_isogram(item):
    nuword = list(item)
    if len(nuword) < 1:
        return "please enter string"
    else:
        for n in nuword:
            if nuword.count(n) > 1:
                return "It aint an iso"
            else:
                return True

print(nu_isogram("semutenga"))