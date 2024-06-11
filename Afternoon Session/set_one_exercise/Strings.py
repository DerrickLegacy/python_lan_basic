# number one
age = 22
name="Hairat"
print(name,age)
# number two
txt = "     Hello,       Uganda!       "
# Remove spaces at the beginning and end
txt = txt.strip()
# Remove spaces in the middle
txt = ' '.join(txt.split())
print (txt)

#question 3
#  Convert the string to uppercase
a = txt.upper()
# Print the result
print(a)
# question 4
# Replace 'U' with 'V'
replacing = txt.replace('U', 'V')

# Print the result
print(replacing)
# question 5
# Given string
y = "I am proudly Ugandan"

# Get the range of characters in the 2nd, 3rd, and 4th positions
substring = y[1:4]

# Print the result
print(substring)
# question 6
#x = “All “Data Scientists” are cool!” 
# The correct one is
#x = "All Data Scientists are cool"
x = 'All "Data Scientists" are cool!'
print(x)

