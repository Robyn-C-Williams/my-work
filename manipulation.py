#In this task I will firstly promopt the user to input a sentence. 
#I will store the input data into a variable called str_manip 

str_manip = input ("Please enter a sentence ")
print (str_manip)

# I will now create an operation to do the following: 
# 1: Calulate and display the length of the inputted data. To do this I will use the len() method.
#To do this, I have created a new variable which will display str_manip as an integer character length.


str_manip_length = len(str_manip)
print(str_manip_length)

#2: Replace the last letter of the inputted data with an @ symbol. 
# To do this I will create a new variable to store the last character's value. I will do this using indexing. 

str_manip_last_letter = str_manip[-1]
print (str_manip_last_letter)

# I will then use the replace method to replace the last characters value with an "@" symbol at every occurence.

str_manip_replace = str_manip.replace(str_manip_last_letter, "@")
print(str_manip_replace)

#I will now demonstrate printing the last 3 characters of the str_manip input backwards.
#I will do this by creating 2 variables. One will be the last 3 characters of the str_manip input. I will do this using indexing.
# The second variable will be the indexed str_manip - that will be sub-indexed, to print backwards.

#I have created a new variable which will print the last 3 characters of the inputted sentence. 
str_manip_3char =(str_manip[-3::])
print (str_manip_3char)

#I have created a new variable which will print the str_manip_3char backwards

str_manip_3char_reversed = str_manip_3char [::-1]
print (str_manip_3char_reversed)

#Using the first 3 characters and the last 2 characters of the input, I will create 3 new variables. 
# I will create a variable to store the first 3 characters of the input.

str_manip_first_three_chars = str_manip[:3]
print (str_manip_first_three_chars)

# I will create a variable to store the last 2 characters of the input.

str_manip_last_two_chars = str_manip [-2::]
print (str_manip_last_two_chars)

#As the data is stored as a variable, I am able to concatonate the values together with the '+' operator

concat_first3_and_last2 = (str_manip_first_three_chars) + (str_manip_last_two_chars)
print (concat_first3_and_last2)