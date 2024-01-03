# To have access to the math module - I have imported math
import math

# I created the function end_or_continue to display a function that will enable the user to restart the program or end it.
def end_or_continue():

    # The user is prompted to type 'y' to return to the home screen, or 'n' to end the program
    yes_or_no = (input ("Would you like to return to the home screen?\nPlease enter:'y' to return to the homescreen or 'n' to end the session: "))

    # I typecasted the input to be lowercase to mitigate case sensitive faults.
    yes_or_no_lower = yes_or_no.lower()

    # I utilised if & elif conditions to use the input to pass the user to the correct calculator function.
    if yes_or_no_lower == "y":
        print ("You are being redirected to the home screen.")
        finance_calculator()

    elif yes_or_no_lower == "n":
        print ("Thank you for using our calculator. Have a great day!")

    # I used the != operator to prompt the user to enter the correct value by triggering the end_or_continue function again - if they did not enter the correct value.
    elif yes_or_no_lower != "n" or "y":
        print ("\nYou have entered an incorrect value.")
        end_or_continue()


# I created the function home_loan_calculation_function to easily use and call upon the calculator at any point during the program, without re-scripting the code.
def home_loan_calculation_function():

    # I used the try & except method to ensure the user enters the correct input.
    while True:
        try:
            house_value = float(input ("Please input the value of the house: £ "))
            break
        except ValueError:
            print("Please enter a numerical value.")

    while True:
        try:
            house_loan_interest_rate = float(input ("Please input the interest rate you want: "))
            break
        except ValueError:
            print("Please enter a numerical value.")

    # I created a variable for the house's repayment interest - which turns the users inputted whole number into a decimal.
    house_interest_decimal = house_loan_interest_rate / 100

    while True:
        try:
            months_investing = float(input ("Please input the amount of months you would like to pay the loan back over: "))
            break
        except ValueError:
            print("Please enter a numerical value.")

    # I created variables that represent the data inputted by the user. These variables are single characters which makes it easier to use them within the home repayment calculation.
    i = house_interest_decimal / 12
    n = months_investing
    p = house_value

    # I created an embedded function called loan_repayment_formula in order to access and use the code (the formula) without having to re-script. 
    def loan_repayment_formula():
        repayment = (i * p) / (1 - (1 + i) ** (-n))
        rounded_repayment = format(repayment, ".2f")
        print(f"You will need to pay £{rounded_repayment} a month.")
    loan_repayment_formula()
    
    # To make my code more readable, I added an empty string to create an empty line.
    print (" ")

    # I called end_or_continue after the user finished their calculator process in order to allow them to do another calculation or end the session.
    end_or_continue()

# I created the function investment_calculation_function to easily use and call upon the calculator at any point during the program, without re-scripting the code.
def investment_calculation_function():

    # I used try & except blocks for user inputs in order to mitigate faults and errors arising from incorrect inputs. 
    while True:
        try:
            money_investing = float(input ("Please input the amount of money you would like to invest: £ "))
            break
        except ValueError:
            print("Please enter a numerical value.")

    while True:
        try:
            invest_interest_rate = float(input ("Please input the interest rate you want: "))
            break
        except ValueError:
            print("Please enter a numerical value.")

    # I created a variable to turn the users inputted whole number into a decimal number.
    interest_decimal = invest_interest_rate / 100

    while True:
        try:
            years_investing = float(input ("Please input the amount of years you would like to invest: "))
            break
        except ValueError:
            print("Please enter a numerical value.")

    while True:
        try:
            simple_or_compound = (input ("Please input the type of interest you would like by entering 'simple' or 'compound': "))
            break
        except ValueError:
            print("")
            
    # I created single character variables to store the users inputs in order to easily assemble the formula used within the calculator.
    # These variables are stored outside of and before the calculators so that they can be accessed globally.           
    r = interest_decimal
    P = money_investing
    t = years_investing
    

    def simple_interest_calculator():
        simple_total = P *(1 + r*t)
        rounded_simple_total = format(simple_total, ".2f")
        print(f"You will recieve £{rounded_simple_total} total, from your investment.")
        return simple_total

    def compound_interest_calculator():
        compound_total = P * math.pow((1+r), t)
        rounded_compound_total = format(compound_total, ".2f")
        print (f"You will recieve £{rounded_compound_total} total, from your investment.")
        return compound_total

    simple_or_compound = (input ("Please input the type of interest you would like by entering 'simple' or 'compound': "))

    simple_or_compound_lower = simple_or_compound.lower()
    interest = simple_or_compound_lower

    if interest == "simple":
        simple_interest_calculator()

    elif interest == "compound":
        compound_interest_calculator()


        

    print (" ")

    end_or_continue()

    print (" ")

# I created the function finance_calculator to separate the inital greetings and relevant triaging process which will pass the user to the correct calculators.
def finance_calculator():

    # The customer will input their preference of calculator (investment or bond)
    customer_first_input = (input ("\nHi there.\nTo calculate the amount of interest you'll earn of your investment please type 'investment'.\nTo calculate the amount you'll have to pay on a home loan please type 'bond': "))

    # The input is typecasted to be lowercase in order to mitigate case sensitive faults.
    customer_first_input_lower = customer_first_input.lower()

    # I then used if and elif conditions to categorise the users input.
    # If the user typed investment - the investment_calculation_function() will be called.
    if customer_first_input_lower == "investment":
        print ("You have chosen 'investment'.")
        investment_calculation_function()
        
    # If the user typed bond - the home_loan_calculation() will be called.
    elif customer_first_input_lower == "bond":
        print ("You have chosen 'bond'.")
        home_loan_calculation_function()

    # If the user did not enter the correct value - the finance_calculator() function will be called and the user will need to re-enter the calculator they wish to use.
    elif customer_first_input_lower != "investment" or "bond":

        print (" ") 
        
        print ("You have inputted an incorrect answer. Please try again.")

        print (" ") 

        finance_calculator() 
  
# To begin the program - the finance_calculator is called.
finance_calculator()  