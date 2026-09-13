#lab1......
# 1. Comments......
print("Hello, Python!")
#This line of code prints Hello, Python! on screen.



 # 2. Input/ Output
name = input("Enter your name:")
print("Your name is:", name)

# 3. Multiple statements on a single line.
x = 10; y = 20
print("x = ", x); print("y = ", y)


# 4. Identation
age = 20
if age >=18 :
    print("You are an adult.")


#5. Data Types
integer=25
print(type(integer))
floating= 10.3
print(type(floating))
string= "PYTHON"
print(type(string))
boolean= True
print(type(boolean))
complex_no = 2 + 3j
print(type(complex_no))


# 7. TYPE CASTING
no = 50

integer_number = int(no)
float_number = float(no)

print(integer_number)
print(float_number)

# 8. NUMBERS
integer_number = 100
float_number = 25.5
complex_number = 4 + 3j

print("Integer:", integer_number)
print("Float:", float_number)
print("Complex:", complex_number)


# 9. BOOLEAN
is_student = True
is_teacher = False

print("Is student:", is_student)
print("Is teacher:", is_teacher)


# 10. STRINGS
message = "Hello Python"

print(message)
print("Length:", len(message))


# 11. SPECIAL CHARACTERS IN STRINGS
print("Hello\nPython")
print("Hello\tPython")
print("This is a backslash: \\")
print("She said, \"Hello!\"")
print("It's a Python class.")


# 12. STRING INDEXING
text = "PYTHON"

print(text[0])
print(text[1])
print(text[-1])
print(text[-2])



# 13. STRING SLICING
text = "PYTHON TUTORIAL"

print(text[0:6])
print(text[7:15])
print(text[:6])
print(text[7:])


# 14. LISTS
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)


# 15. CREATING LISTS
empty_list = []

student = ["Sehrish", 20, 3.67, True]

print(empty_list)
print(student)


# 16. LIST INDEXING
colors = ["Red", "Blue", "Green", "Black"]

print(colors[0])
print(colors[1])
print(colors[-1])
print(colors[-2])


# 17. LIST SLICING
colors = ["Red", "Blue", "Green", "Black"]

print(colors[0:2])
print(colors[1:3])
print(colors[:3])
print(colors[1:])


# 18. CONDITIONAL STATEMENTS
marks = 75

if marks >= 50:
    print("Pass")
else:
    print("Fail")


# Another conditional statement
number = 10

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")