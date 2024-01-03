# I created a string to explain the function of the program.

print ("Use this calculator to find out your future age! Input your current age, and the amount of years in the future you wish to add to your age to find your future age!")

# I have created two variables where the user will enter two numerical inputs.
age = float(input("Please input your age: "))
in_time_age = float(input("Please the amount of years you want to add to your age: "))

# Instead of adding the two entries together - I have multiplies them. Therefore, the code is executed but the wrong age is shown.
future_age = age * in_time_age 

# I print the variable future_age however it does not show the correct age.
print (future_age)


