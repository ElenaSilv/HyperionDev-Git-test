'''The program allows the user to calculate their investment interest (either simple or compound)
   OR to calculate a home loan repayment plan.'''

import math

options ='''
Investment - to calculate the amount of interest you'll earn on your investment
Bond       - to calculate the amount you'll have to pay on a loan
'''

print(options)

investment = "investment"
simple_interest = "simple"
compound_interest = "compound"

bond = "bond"

# Requesting input from the user 
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()


# Investment calculator 
if user_choice == investment:
    deposit = int(input("How much money do you want to deposit? ")) 
    interest_percentage = int(input("Please tell us the percentage of the interest rate (no symbols): "))/100
    years = int(input("How many years do you plan on investing? "))
    interest = input("Do you want a simple or compound interest? ").lower()
    
    # choosing btw simple or compund interest
    if interest == simple_interest:
        print(deposit *(1+interest_percentage*years))
    elif interest == compound_interest:
        print(deposit * math.pow((1+interest_percentage),years))
    else:
        print("Please start again and choose either 'simple' or 'compound.")



# home loan repayment calculator 
elif user_choice == bond:
    house_value = int(input("Please tell us the present value of your house: "))
    interest_percentage = int(input("Please tell us the percentage of the interest rate (no symbols): "))/100
    months = int(input("How many months will you need to repay the bond? "))
    
    print((interest_percentage/12 * house_value)/(1 - (1 + interest_percentage/12)**(-months)))

else:
    print("Please start again and choose either 'investment' or 'bond.")