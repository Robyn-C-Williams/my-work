# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# The first error is here. I added parenthesis to the print statements
print ("Welcome to the error program")

#This statement needed to be inline.
print ("\n")

    # Variables declaring the user's age, casting the str to an int, and printing the result

# Lines 15 - 26 need to be in line.
# age_Str - needs only 1 = assignment. age_Str also needs to only have a number.
age_Str = 24

# The variable age only typecasts the age_Str variable and may not be necessary long term.
age = int(age_Str) 

# This string needs to be an f string to concatenate the different data types.
print(f"I'm {age} years old.")

# Variables declaring additional years and printing the total years of age
# years_from_now doesn't need to be a string
years_from_now = 3
total_years = age + years_from_now

# This print statement needs parenthesis and also needs to be an f statement
# I replaced the + with a comma

# The string "answer_years" looks like it should be a variable however I am unable to know what it is meant to mean or do.
print (f"The total number of years: {total_years}", "answer_years")

# Variable to calculate the total amount of months from the total amount of years and printing the result
# The variable was written incorrectly
total_months = total_years * 12

# This print statement needs to be an f string - with parenthesis
print (f"In 3 years and 6 months, I'll be {total_months} months old")

#HINT, 330 months is the correct answer

