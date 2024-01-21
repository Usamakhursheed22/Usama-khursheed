# 1). age criteria

age = int(input("enter your age:"))

#Determine the age group.

if age < 13:
    print("child")
elif age < 20:
    print("teenager")
elif age < 60:
    print("adult")
else:
    print("senior")

# 2). Definig a complex number veriable.

comp_num = 7 + 8j 
real_part = comp_num.real
imaginary_part = comp_num.imag

print("Real part:", real_part)
print("Imaginary part:", imaginary_part)

#3). Sum of numbers.

num1 = 24
num2 = 6
add = (num1+num2)
print("Answer of sum:",(add))

#4). Append Function.

message = "hello "
message += "world!"
print(message) 

#5). Bool function.

is_python_fun = False
if is_python_fun:
    print("python is fun")
else:
    print("python is not fun for those who are not intrested in it!")

#6). Creating a list of fruits.
    
Fruits = ['kewi', 'mango', 'apple']
print("list of fruits:", Fruits)
new_fruit = 'orange'
Fruits.append(new_fruit)
print("updated list of fruits:", Fruits)

#7). Conversion of Float into Integer.

price = 26.5
print("price in float form:", price)
integer_price = int(price)
print("price in integer form:", integer_price)

#8). creating dictionary.

student_info = {
    'name' : 'Usama',
    'age' : '20',
    'grade' : '13th'
    }
print(student_info) 

#9). combine two strings using concatenation.

string1 = "here we go "
string2 = "again"
combined_string = string1 + string2
print(f"the combine string is: {combined_string} and its length is {len(combined_string)}")

#10). #Create a tuple named days of week wwith the name of the day.

days_of_week = ("monday ","tuesday ","wednesday ","thursday ","friday ","saturday ","sunday")
print(days_of_week[3])

