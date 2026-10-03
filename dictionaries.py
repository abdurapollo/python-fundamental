# Day 8: Python Dictionaries
# A dictionary stores data as key-value pairs. Each key identifies a value.




# student = {
#     "name": "Ajay",
#     "age": 25,
#     "course": "Python"
# }






student = {
    "name": "Ajay",
    "age": 25,
    "course": "Python"
    "isActive": True
}

# Example of a dictionary 




# Adding and updating values

# student["address"] = "Bangalore"

# student["age"]



# Safely reading a value
# Use .get() when a key may not exist:

# student.get("mobile", "Not Available")
# print(student.get("age", "Not Available"))

# # Looping through a dictionary

# for key, value in student.items(): 
#     print(key, ":", value)





# Practical example: Product inventory
inventory = {
    "laptop": 10,
    "mouse": 25,
    "keyboard": 15
}

product = "laptop"
if product in inventory:
    print(f"{product} is available with quantity: {inventory[product]}")
else:
    print("Product not available") 

inventory["mouse"] -= 1

print("Updated inventory:", inventory)







# Key takeaway

# Dictionaries are ideal for structured data such as user profiles, product details, API responses, settings, and inventory records. 
# Keys must be unique, while values can be of any data type.

