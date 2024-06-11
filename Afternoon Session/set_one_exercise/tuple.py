x = ("samsung", "iphone", "tecno", "redmi")
favorite_phone = "iphone" 
print('....................favourite phone..............................')
print(f"My favorite phone brand is: {favorite_phone}")
print('')

# the second last item
print('..............................second last item...............................')
x = ("samsung", "iphone", "tecno", "redmi")
second_last_item = x[-2]
print(f"The second last item in the tuple is: {second_last_item}")
print("")

# update iphone” to “itel”
print('...................update.............................................')
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print(x)
print("")

#add huwei to the tuple
print("....................................addition...........................................")
x = ("samsung", "iphone", "tecno", "redmi")
x_list = list(x)
x_list.append("Huawei")
x = tuple(x_list)
print(x)
print("")

print(".......................................loop....................................")
# loop throug the tuple
x = ("samsung", "iphone", "tecno", "redmi")
for phone in x:
    print(phone)
print("")
    
print("...................................deletion..........................................")
# delete the first item in the tuple
x = ("samsung", "iphone", "tecno", "redmi")
x_list = list(x)
del x_list[0]
x = tuple(x_list)
print(x)


print("..............................................constructor................................")
#7.	Using the tuple() constructor, create a tuple of the cities in Uganda
cities_in_uganda = tuple(["Kampala", "Entebbe", "Jinja", "Gulu", "Mbarara"])
print(cities_in_uganda)
print("")

print(".........................unpack...........................................................")
#8.	Write a python program to unpack your tuple.
cities_in_uganda = ("Kampala", "Entebbe", "Jinja", "Gulu", "Mbarara")
city1, city2, city3, city4, city5 = cities_in_uganda
print(city1)
print(city2)
print(city3)
print(city4)
print(city5)
print("")
#9.	Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above
print(".......................................use of range.......................................")
cities_in_uganda = ("Kampala", "Entebbe", "Jinja", "Gulu", "Mbarara")
print(cities_in_uganda[1:4])
print("")

print("..........................two tuples..........................................")
#10.	Write two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("musiimenta", )
second_names = ("cissylyn", )
full_names = first_names + second_names
print(full_names)
print("")
 
print("..........................multiply..........................................")
#11.	Create a tuple of colors and multiply it by 3.
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors)
print("")

print("..........................number of times..........................................")
#Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print(count_8)



