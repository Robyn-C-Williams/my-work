# I will ask the user to enter three different numbers.
# In order to make sure the input will be numerical values - I have typecast the variables to be floats. 
# I chose floats instead of integers in order to have more complex numbers.
# I made sure each input was

num1 = float (input("Please enter a whole number: "))
num2 = float (input("Please enter a second whole number: "))
num3 = float (input("Please enter a third whole number: "))

print (f"{num1},{num2},{num3}")

# I have created an equation that will add all of the inputs together and to print the sum.
sum_of_all = (num1 + num2 + num3)
print (sum_of_all)

# I have created an equation that will deduct the second number from the first number. 

negative_sum = (num1 - num2)
print (negative_sum)

# I have created an equation that will multiply the third number by the first number

multiply_sum = (num3 * num1)
print (multiply_sum)

# I have created an eqution that will divide the sum of all numbers by the third number

print (sum_of_all / num3)

