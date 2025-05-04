
# printing strings

print('codanics')
print("we are learning python with codanics")
print('''we are learning python with codanics''')

# printing numbers
print(10+20)


#list of integers 
a= [1,2,3]
b= [4,5,6]

# concatenation of lists
print(a)
print(b)
print(a+b)

#use of variables and tips to use them
# 1. to perform calculations
# 2. to import the data and name the data

# rules
# 1. variables should not start with numbers
# 2. variables should not contain any special characters
# 3. variables should not be same as func names
# 4. dont use spaces in variable names instead use _
# 5. dont use capital letters in variable names
# 6. use short and descriptive variable names

# more operators
a = 'codanics'
b = 'we are learning python with codanics'
print(a+b)

# data types
# 1. x = 5  int 
# 2. y= 5.5 float
# 3. z = 'hello' string
# 4. a = [1,2,3] list
# 5. b= (1,2,3) tuple
# 6. c= {'name':'codanics', 'course':'python', 'fees':500} dict 
# dictionary is made up of keys and values 
# 7. d= {1 , 2, 3} set

# identation
a = 10
b = 20

if a > b:
    print('a is greater')
else:
    print('b is greater')

#
person_1_name = input("enter your name :")
person_1_age = input("enter your age :")
person_2 = input("enter your name :")
person_2_age = input("enter your age :")

if person_1_age > person_2_age:
    print(person_1_name , 'is older than ', person_2) 
else:
    print(person_2 , 'is older than ', person_1_name)

