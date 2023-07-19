#first Method
File_Name = input("Please Give Your File Name: ")
File_Extension = input("Please Give your File Extension: ")
File_Name_With_Extension = File_Name + "." + File_Extension
print(File_Name_With_Extension)

#Second method
Extensive_Name = input("Enter Your File Name: ")
dot_index = Extensive_Name.find(".")
if dot_index != -1:
    print("You've Inputted  a ."+Extensive_Name[dot_index + 1:] + " File")
else:
    print("No dot (.) found in the file name.")

#Third Method
def print_value_after_dot(string):
  """Prints any value after the "." sign.

  Args:
    string: The string to print the value from.
  """

  index = string.find(".")
  if index == -1:
    print("The string does not contain a '.'")
  else:
    print(string[index + 1:])


if __name__ == "__main__":
  string = input("Enter Your File Name: ")
  print_value_after_dot(string)
