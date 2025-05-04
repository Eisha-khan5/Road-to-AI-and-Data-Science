# Data Structures in Python
# 1. list

food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
print(food)
print(food[2])
print(food[-1])
food[0] = "sushi"
print(food)
food.append("ice cream")
print(food)
food.remove("hamburger")
print(food)


# 2.Tuples

coordinates = (4, 5)
print(coordinates[0])   

# 3. set
fruit_set = {"apple", "banana", "orange"}
print(fruit_set)
fruit_set.add("grapes")
print(fruit_set)

# 4. dictionary
car = { 
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car)
car["year"] = 2020
print(car["year"])