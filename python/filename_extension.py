# Get the filename from the user
filename = input("Enter a filename: ")

# Split the filename into its name and extension
extension = filename.split(".")

# Print the file extension
print("File extension:", extension[-1])


# OR


# Get the filename from the user
filename = input("Enter a filename: ")

# Split the filename into its name and extension
name, extension = filename.split(".")

# Print the file extension
print("File extension:", extension)
