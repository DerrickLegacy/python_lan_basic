# age = 23

# if age<18:
#     print("You are an adult")

# elif age>63:
#     print("You are a Mzee")

# else:
#     print("You are a youth")  
    
#90> - Excellent
#80> - Very Good
#70 - Good
#Otherwise - Not Good 

grade = 88

if grade >= 90:
    print("Excellent")

elif grade >= 80:
    print("Very Good")
elif grade >= 70:
    print("Good")

else:
    print("Not Good ")  
    
    
    
# Exercise: 

full_price = 2000
age = int(input("Enter your age: "))

if age < 13:
    discount = 1000
    price = full_price - discount
    print("Child Price: ", price)
    
elif age >= 13 and age < 18:
    discount = 500
    price = full_price - discount
    print("Teenager Price: ", price)
    
elif age >= 18 and age < 45:
    price = full_price
    print("Youth Price: ", price)

else:
    price = 5000
    print("Senior Citizen: ", price)
    
# Loops
"""_summary_
    for loop - iterates over sequence(list, turple, dictionary, set, string)
    while loop - repeats as long as a condition is true
    """
    
cars = ["BMW", "Jeep", "Vitz"]
print(cars)
list_length = len(cars)

new_car_list = cars + ["Harrier","Ferraari"]

for car in new_car_list:
    print(car)

count = 1

while count<=5:
    print(count)
    count +=1

# Exercise 2:

colors = ["Red",  "Black", "White"]
derricks_fav_colors = []

for color in colors:
    derricks_fav_colors.append(color)    

print(derricks_fav_colors) 

# 1. reverse using reverse() method
colors.reverse()
print(colors)

# 2. reverse using [::-1] 
colors.reverse()
reversed_list = colors[::-1]
for color in reversed_list:
    print(color)

text = "12345" 
textLength = len(text)

while textLength > 0:
    print(text[textLength - 1]) 
    textLength -= 1

