# @Author Oluwapelumi
# Getting user values from the user
user_values = input("Enter Series of Value Use Comma to separate them: ")
print("Printing your value in list ")
list = user_values.split(",")
tuple = tuple(user_values)
print("Printing in List and tuple")
print(list, tuple)

# print(user_values.split(","))