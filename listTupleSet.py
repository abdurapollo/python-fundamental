# Day 5: Python Lists

# A list is an ordered collection used to store multiple values in one variable. 
# Lists can contain strings, numbers, or mixed data types, and they are mutable, 
# which means you can change them after creation.


fruits = ["apple", "banana", "mango"]




# Common list operations
# fruits.append("orange")
# fruits.insert(1, "grape")
fruits.remove("mango")
# print(fruits)


# You can find the number of items with len():
# print(len(fruits))



# Practical example: Shopping cart
cart = ["Laptop", "Mouse", "Keyboard"]

cart.append("Headphone")

# print("Items in cart:")

# for item in cart:
#     print("-", item)
# print("Total Items:", len(cart))



# List slicing
# numbers = [10, 20, 30, 40, 50]
# print(numbers[1: 4: 2])


# Key takeaway

# Lists are useful for storing collections such as products, user names, marks, tasks, or orders. 
# You will frequently combine lists with loops and conditions in real applications.

# Practice task: Create a list of five programming languages, add one more language, 
# remove one language, and print every item using a loop.











# Day 6: Python Tuples

# A tuple is an ordered collection of values, similar to a list. 
# The main difference is that tuples are immutable, which means their values cannot be changed after creation.

# Tuples are useful for fixed collections of related values, such as coordinates, dates, or configuration settings.




# colors = ("red", "green", "blue")

# colors[0] = "yellow"
# print(colors)


# Tuple immutability




# Tuple unpacking
person = ("Sonu", 30, "Software Engineer")

name, age, profession = person
print(name, age, profession)


# Practical example: Coordinates
# location = (25.5941, 85.1376)






# A tuple is a good choice here because the coordinate pair should remain unchanged.





# Useful tuple methods
# numbers = (1, 2, 3, 4, 5, 2, 3, 2)
# print(numbers.index(5))







# Key takeaway

# Use a list when your collection may change. 
# Use a tuple when the values should remain fixed and protected from accidental modification.

# Practice task: Create a tuple containing a product name, price, and quantity. Unpack the tuple into variables and calculate the total cost.







# Day 7: Python Sets

# A set is an unordered collection of unique values. 
# Sets are useful when you want to remove duplicates or quickly check whether an item exists.



# numbers = {1, 2, 3, 3, 4, 4}
# print(numbers)

# Duplicate values are automatically removed.



# Common set operations

# python_topics = {"variables", "loops", "lists"}
# new_topics = {"tuples", "sets", "loops"}

# print(python_topics - new_topics)





# Adding and removing items
# skills = {"Python", "SQL"}
# skills.add("Java")
# skills.remove("PHP")
# print(skills)





# Use discard() when you want to remove an item without getting an error if it does not exist:


# Practical example: Remove duplicate email addresses

emails = [
    "alice@example.com", 
    "bob@example.com",
    "alice@example.com",
    "charlie@example.com",
    "bob@example.com"
]

unique_emails = set(emails)
print(unique_emails)






# Key takeaway

# Use a set when:

# You need only unique values.
# The order does not matter.
# You want fast membership checks, such as item in my_set.

# Unlike lists and tuples, sets do not support indexing because they are unordered.