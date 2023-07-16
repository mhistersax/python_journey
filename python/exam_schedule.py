exam_st_date = (11, 12, 2014)

# Print the examination schedule using string formatting
# The format string contains three placeholders for integers (%i)
print("The examination is scheduled for: %i/%i/%i" % exam_st_date)



# OR

exam_st_date = (11, 12, 2014)

# Extract the day, month, and year from the exam_st_date tuple
day, month, year = exam_st_date

# Create a date_string by formatting the day, month, and year as a string
# Using f-string to embed variables directly into the string
date_string = f"{day}/{month}/{year}"

print("The examination is scheduled for:", date_string)
