# The program allows the user to calculate their investment interest (either simple or compound)
# OR to calculate a home loan repayment plan. 

import math

options ='''
Investment - to calculate the amount of interest you'll earn on your investment
Bond       - to calculate the amount you'll have to pay on a loan
'''

print(options)

investment = "investment"
bond = "bond"

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

simple_interest = "simple"
compound_interest = "compound"
