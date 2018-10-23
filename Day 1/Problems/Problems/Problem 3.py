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
