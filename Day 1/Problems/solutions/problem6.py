"""
#### Problem 6: Functions
In this problem you have to program the following 4 functions:
1. A function which takes two arguments, x and y, and returns the product of them
2. A function which takes one argument, and prints it to the screen
3. A function which takes zero arguments and return 42
4. A function which takes two arguments. The function shall add 42 to the product of the two numbers and then print the result.

HINT: The 4th function should reuse the other 3.
"""

# Write your code here!


def product(x, y):
    return x * y


def print_variable(variable):
    print(variable)


def function42():
    return 42


def final_function(x, y):
    product_result = product(x, y)
    sum_42 = product_result + function42()
    print_variable(sum_42)


final_function(2, 3)