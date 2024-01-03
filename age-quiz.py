#This program will use conditional programming to output input responsive outputs. 

#I will create an input variable followed by multiple conditional outputs.

#Firstly I have created an input variable. This variable will allow the user to input data.
#I have typecast the age variable to only accept integer variables.

age = int(input("Please input your age: (Your age must be a whole number) "))

#Below I have created string variables for my output messages - to be used within my conditional algorithm.
# I have chosen string variables instead of print statements to allow flexibilty to my code and a better UI for coders using and editing my code.

forty_and_some = ("You're over the hill")
over_a_hundred = ("Sorry you're dead.")
retired = ("Enjoy your retirement")
kids_discount = ("You qualify for the kiddie discount.")
twenty_first = ("Congrats on your 21st!")
age_is_a_number = ("Age is but a number.")

#I have created an algorithm that is age sensitive. The conditional algorithm runs from the highest to the lowest age.
#This is to ensure that the outputs are formatted correctly - and only one output is sent per input.


#I have used the >= (larger than or equal to) operator to output a condition.
if age >= 100:
    print (over_a_hundred)

#I have used the >= (larger than or equal to) operator to output a condition.
elif age >= 65: 
    print (retired)

#I have used the >= (larger than or equal to) operator to output a condition.
elif age >= 40:
    print (forty_and_some)

#I have used the == (equal to) operator to output a condition.
elif age == 21: 
    print (twenty_first)

#I have used the <= (smaller than or equal to) operator to output a condition.
elif age <= 13:
    print (kids_discount)
        
#I have used an else condition for all other inputted data.
else:
    print (age_is_a_number)

