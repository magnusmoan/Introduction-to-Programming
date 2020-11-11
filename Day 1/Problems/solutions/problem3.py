"""
### Problem 3: Train Ticket Price Calculator
In the following problem you will create a train ticket price calculator. The problem is split into 3 sub-problems.

#### Problem 3.1: Price based on time until travel
Your program should have the following functionality:
1. Ask the user for the number of days until travel
2. Return the price for the ticket to the user based on the number of days entered

The pricing rules are as follows:
If it is more than 10 days until travel the price is 200 NOK (mini-price), otherwise the price is 450 NOK.

#### Problem 3.2: Price based on time until travel and age
Your program should have the same functionality as in problem 3.1, but should also include:
1. Ask the user for age
2. If the user is younger than 16 they are given a 50% discount,
   and if they are older than 59 they are given a 25% discount

#### Problem 3.3: Refundable ticket?
In some cases the user might want to pay full price, instead of mini-price,
since only full price tickets are refundable.
Your program should have the same functionality as in problem 3.2, but should also include:
1. Users eligible for mini-price should be asked if they really want mini-price
2. Mini-price can never be discounted, even if the user is eligible for a discount
3. OPTIONAL: Make the program ask for as little information as possible.
   If the user want mini-price and is eligible for it (more than 10 days until travel),
   she/he should not be asked about age.
"""

# Write your solution here!
mini_price = False
discount = 0
price = 450

days_until_travel = int(input("How many days until travel? "))
if days_until_travel > 10:
    wants_mini_price = input("You are eligible for mini price, however this ticket is not refundable. Do you want mini price (yes/no)? ").lower()
    if wants_mini_price == "yes":
        mini_price = True
        price = 200

if not mini_price:
    user_age = int(input("How old are you? "))
    if user_age < 16:
        discount = 0.5
    elif user_age > 59:
        discount = 0.25

price = price * (1 - discount)

print("The ticket will cost " + str(price) + " NOK")