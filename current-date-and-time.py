import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the current date and time
formatted_datetime = current_datetime.strftime("%A, %B, %d, %Y %I:%M:%S %p")

# Display the current date and time
print("Current Date and Time:", formatted_datetime)
