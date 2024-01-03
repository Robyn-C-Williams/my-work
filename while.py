# I created a counter/control variable to store 0 as the base value to be added to all entries from the user.
total = 0

# I created an empty list variable to store all entries made by the user.
# This will allow me to divide the total variable by the value of user_num_list after using the len function - which, explicitly, outputs the amount of entries.
user_num_list = []

# I used a while loop with a boolean variable to iterate the loop.
while True:

    # I embedded a try-except box in order to mitigate any errors that may occur from the users entry.
    try:

        # I typecasted the users input to a float in order to be able to use math on the inputs (to find the average of the inputs)
        num = float(input("Please enter a number. (Entering -1 will terminate the program): "))
    except:
        (ValueError, NameError, TypeError)
        print("You have entered an incorrect value")

        # I used the continue function to continue the while loop's parameters once the input is accepted
        continue

    # I used the if condition to create a condition that will end the program once the user enters -1
    if num == -1:

        # The break function terminates the loop - only if the user enters -1
        break
    
    # I used the .append function to store all values of (num) entered into the user_num_list list.
    user_num_list.append(num)

    # I used variable total, within the loop - in order to update the value of the variable globally.
    total = total + num

# To find the average of all number entered I divided the total by the amount of enteries in user_num_list.
# To find the amount of enteries in user num list I used the len() function.
avg = total / len(user_num_list)

# I used the round() function - to round the inputs average to 2 decimal places.
round_avg = round(avg,2)

# I then used an f string to print the average of all numbers entered.
print (f"The average of all numbers entered is {round_avg}")
