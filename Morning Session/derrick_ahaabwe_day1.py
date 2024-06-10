import os
import sys
print(os.getcwd())
name = input("Enter your name: ").strip().title()
print(f"Hello,", name)

S = 'shrubbery'
L = list(S)
"".join(L)
L[1]="c"
print(L)

# Type-Specific Methods
n = "Suppam"
print(n.find("pa"))
new_word = n.replace('pa', 'XYZ')
print(new_word)

line = '   aaa,bbb,ccccc,dd\n'
split = line.split(',')
print(split)

uppercase = line.upper()
alphabet = S.isalpha()

remove_white_space = line.rstrip()
both_ends = line.rstrip().split(',')
print(remove_white_space)
print(both_ends)


# string formatting
formatExp1 = '%s, eggs, and %s' % ('SPAM!','spam')
formatExp2 = '{1}, eggs, and {0}'.format('spam', 'SPAM!')

print(formatExp2)

# Accessing all string methods
stringMethods = dir(S)
print(stringMethods)
concat1 = S + 'NI!'
concat2 = S.__add__('NI!') #methods with _ for implementation pattern, while without the underscores in this list are the callable methods on string objects

whatMethodDoes = help(S.replace)
print(whatMethodDoes)

