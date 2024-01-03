# This program will determine the award a triathelete will achieve. 
# The time will be based in minutes. 
# The total time taken across 3 events will be added together.

# I created my variables outside of my coding algorithim in order to be able to access the variable values without error.

swimming_input = float(input("Please enter the amount of time it took to complete the swimming event: (please enter in minutes only)  "))
cycling_input = float(input("Please enter the amount of time it took to complete the cycling event: (please enter in minutes only) "))
running_input = float(input("Please enter the amount of time it took to complete the running event: (please enter in minutes only) "))
total_time = swimming_input + cycling_input + running_input

# I used print (" ") to create an easy to read format, in terms of the text (string) output.

print (" ")

# I created a simple chart to outline the relevant qualifying criteria.

print ("Well done for completing the triatholon. Please find the qualifiying criteria below.\
       \nTime range: 0 - 100 minutes        Award: Provincial Colours \nTime range: 101 - 105 minutes      Award: Provincial Half Colours \nTime range: 106 - 110 minutes      Award: Provincial Scroll \nTime range: 111+ minutes           Award: No award ")

print (" ")

# I used an f string to concatonate the float data within a string.

print (f"The time taken to complete all events was: {total_time} Minutes.")

print (" ")

# I used if, elif and else conditional functions to create an algorithm that will use the inputted data to output the correct award.
# I made sure to create the algorithm following the correct order (the highest value 1st) followed by incrementaly lower values.

if total_time >= 111:
    print ("Unfortunately you did not finish the triatholon within the qualifiying times. Please try again next next time!")

elif total_time >= 106:
    print ("Congratualtions! You qualified for the Provinical Scroll Award!")

elif total_time >= 101:
    print ("Congratualtions! You qualified for the Provinical Half Colours award!")

else:
    print ("Well done! You finished the triatholon in record time. You have been awarded Provincial Colours.")






