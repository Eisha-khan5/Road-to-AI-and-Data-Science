# Conditional statements

x = 10
if x > 5:
    print("x is greater than 5")    
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# for loop
menu = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
for food in menu:
    print(food)

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# break statement
for letter in "codanics":
    if letter == "a":
        break
    print(letter)

# continue statement
for letter in "codanics":
    if letter == "a":
        continue
    print(letter)

# pass statement
for letter in "codanics":
    if letter == "a":
        pass
    print(letter)

# nested for loop
colors = ["red", "green", "blue"]
items = ["chair", "table", "sofa"]

for color in colors:
    for item in items:
        print(color, item)

# nested while loop
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(i, j)
        j += 1
    i += 1

# for loop inside while loop
i = 1
while i <= 5:
    for j in range(3):
        print(i, j)
    i += 1


# while loop inside for loop
for i in range(3):
    j = 1
    while j <= 5:
        print(i, j)
        j += 1  