"""
#### Problem 4.1
Write a program that calculates the sum of a geometric sequence by using a while loop.
The variables *r* and *n* should be read from the user.

#### Problem 4.2
Rewrite the program from 4.1 such that the loop is finished when the difference between the sum and the limit is less than 0.001.
HINT: A while-loop in Python can be quit before the condition is false. Google how to do this.
Test your solution with *r* = 0.5.

#### Problem 4.3
Rewrite the program from 4.2 to print how many iterations the while-loop were executed before the difference between the sum and the limit were less than 0.001.
OPTIONAL: Print the real difference between the sum and the limit after the loop is broken.
"""

# Write your code here!

r = float(input("r: "))

limit = 1 / (1 - r)
print("Limit: " + str(limit))
i = 0
geometric_sum = 0

while True:
    geometric_sum += r ** i
    if abs(limit - geometric_sum) < 0.001:
        break
    i += 1

print("Actual sum:", geometric_sum)
print("The difference is:", abs(limit - geometric_sum))
print("The number of iterations it took to get there:", i + 1)