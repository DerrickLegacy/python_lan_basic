#SETS

#Creating using a set constructor
thisset = set(("fourCousins", "CokeZero", "RedBull")) 

#Adding the two beverages
thisset.add("Nile")
thisset.add("Johnwalker")
print(thisset)

#check if item present
mySet = {"Oven", "Kettle", "microwave", "refrigerator"}
print("microwave" in mySet)

#Removing item
mySet = {"Oven", "Kettle", "microwave", "refrigerator"}
mySet.remove("Kettle")
print(mySet)

#looping through the set
mySet = {"Oven", "Kettle", "microwave", "refrigerator"}
for x in mySet:
  print(x)

# Create a set with 4 items
my_set = {"apple", "banana", "cherry", "date"}

# Create a list with 2 items
my_list = ["elderberry", "fig"]

# Add elements from the list to the set
z = my_set.union(my_list)
print(z)

#Joining two sets
ages = {33, 20, 23, 25, 24}
first_name = {"Gertrude", "Shadia", "Paul", "Cissy", "Alvin"}
myset = ages | first_name 
print(myset)
