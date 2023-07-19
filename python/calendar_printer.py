import calendar

# Accept input for month and year
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

# Print the calendar for the specified month and year
print(calendar.month(year, month))
