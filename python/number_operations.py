# Prompt the user to input an integer
a = int(input("Input an integer: "))

# Concatenate 'a' with itself using formatted string literals
# and convert the concatenated strings to integers
n1 = int("%s" % a)  # n1 = a
n2 = int("%s%s" % (a, a))  # n2 = aa
n3 = int("%s%s%s" % (a, a, a))  # n3 = aaa

result = n1 + n2 + n3

# Print the result
print(result)
