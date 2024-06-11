"""
#LISTS :    Are positionally ordered collections of arbitrarily typed objects.
            -They have no fixed size
            -Mutable
            -Store different objects of different types(Strings, Integers, float)
"""

mylist = ["Paul", "Juma", "Joe", "Deo", "Joseph", 100]
print("Original list is :", mylist)
print(mylist[1])
print(type(mylist))

# change the value of the first element using index


def change_first_item(lst, new_value):
    if lst:
        lst[0] = new_value
        return lst


mylist = change_first_item(mylist, "John")
print("Update list:", mylist)


"""
Available Methods
    1. append()	-Adds an element at the end of the list
    2. clear()	-Removes all the elements from the list
    3. copy()	-Returns a copy of the list
    4. count()	-Returns the number of elements with the specified value
    5. extend()	-Add the elements of a list (or any iterable), to the end of the current list
    6. index()	-Returns the index of the first element with the specified value
    7. insert()	-Adds an element at the specified position
    8. pop()	-Removes the element at the specified position
    9. remove()	-Removes the first item with the specified value
    10. reverse()	-Reverses the order of the list
    11. sort()	-Sorts the list
    12. remove()

"""
print(dir(mylist))
# Append an element at the end of list

mylist.append("Francis")
mylist.insert(2, "Bathel")
mylist.insert(3, "Amon")

# Deleting Item at specifiend index e,g 4
del mylist[3]

# new list and print a given range of elements
new_list = ["book", "pen", "chair", "table", "ruler", "bag", "belt"]

# Printing ranges using [:]
print("the last item is: ", mylist[-1])
print("the 3rd, 4th and 5th items are: ", mylist[2:5])

country_list = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]
x = country_list.copy()

for x in country_list:
    print(x)

# list of animal names and sort them in both descending and ascending order.
animal_list = ["dog", "goat", "sheep", "cow", "monkey", "zebra"]

# ascending sort
ascending_sort = sorted(animal_list)
print("This list is sorted in assending order: ", ascending_sort)

# descending sort
desceding_sort = sorted(animal_list, reverse=True)
print("this list is sorted in descending order: ", desceding_sort)

# Filter animal names with the letter 'a' in them
animal_names_with_a = [name for name in animal_list if 'a' in name.lower()]
print("Animal names with the letter 'a':", animal_names_with_a)

# list of my name
first_name = ["Paul"]
second_name = ["Akol"]

second_name.extend(first_name)
print(second_name)
