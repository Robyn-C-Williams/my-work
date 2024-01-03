#In this task I will demonstrate how to replace characters in a string. 
# I will store the following data in a string variable.

string1 = ("The!quick!brown!fox!jumps!over!the!lazy!dog")

#I will create a new variable containg string1's value - however I will also use the replace method.
#I will use the replace method to replace the '!' with a blank space.

string1_replaced = string1.replace ("!", " ")

print (string1_replaced)

# With the string1_replaced variable - I will now use the upper method to capitalize all of the characters. 

string1_replaced_upper = string1_replaced.upper()

print (string1_replaced_upper)

#I will now printe string1_replaced_upper in reverse. To do this, I will use indexing. 
#I will create a new variable called string1_replaced_upper_reverse - and I will use box brackets to define the print parameters

string1_replaced_upper_reversed = string1_replaced_upper [::-1]

print (string1_replaced_upper_reversed)

