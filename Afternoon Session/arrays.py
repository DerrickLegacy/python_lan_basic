import array as arr

# array(data_type, value_list)
# arrayName = array(typecode, [initializer])
# is used to create array in Python with data type and value list specified in its arguments.

students_marks = arr.array('i', [2, 4, 5, 6, 56, 65])
print(type(students_marks))
print(students_marks)

# Joining two arrays together
a = arr.array('d', [1.6, 3.7, 4.4, 5.3, 6.2, 7.4])

b = arr.array('d', [1.2, 3.4, 5.6, 7.8])

c = arr.array('d')

c = a + b
print(c)
print(" ")

# to access/searching for an individual elements of the array
print('the first element is ', c[0])
print('the second element is ', c[1])
print('the last element is ', c[-1])
print('the second last element is ', c[-2])

# deleting elements from an array
del c[3]
print(c)

numbers = arr.array('i', [1, 4, 23, 3, 4, 56, 54, 4, 4, 4, 4])
# modifying elements in the array
print("Before updating", numbers)
numbers[3] = 7
print("After updating", numbers)

# METHODS FOR PERFORMING ARRAY OPERATIONS
"""
    -append() - add one value 
    -extend() - add more than one value
    -insert() - adds item after specified position
    -remove() - remove first occurences of value from array
    -pop()    - value from an array at specified index
    -reverse()
    -__contains__
    -_copy_

"""

# counting number of occurrences of an element in the array
count = numbers.count(4)
print("the number occurs", count, "number of times")

# adding elements in array
numbers.append(89)
numbers.append(1)
numbers.append(96)
print(numbers)
print(".......................work............................")
print(students_marks[2:3])

# extend()
numbers.extend([70, 88, 29])
# remove()
numbers.remove(70)
# reverse
numbers.reverse()
# _contains_
print(numbers.__contains__(88))
# _copy_
copied_numbers = arr.array('i', [])
print(copied_numbers)


copied_numbers = numbers.__copy__()
print(copied_numbers)

# printing methods for an array object
print(dir(numbers))

# insert()
numbers.insert(3, 10000)
print(numbers)


numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5])  # 3rd to 5th
print(numbers_array[:-5])  # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])   #
