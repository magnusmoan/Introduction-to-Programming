"""
Problem 1: Printing, strings and mathematical operations
In the following problem you will be asked to combine knowledge about strings and mathematical operators.
Remember that everything within a pair of " or ' are considered string, even though they are mathematical expression.
An example of this is "1+2".

When grouping longer expressions in Python we use () to group sub-expressions.
"""

# Example of grouping
a = 3 - 2 * 4
b = (3 - 2) * 4
print(a)
print(b)

# Finally: A print statement can take an arbitrary number of arguments separated by commas
a = 3
b = 4
print(a, b)

# Replace None with the correct mathematical expression
print('1+2(−3) =', 1+2*(-3))
print('[(3+5·2) + 1] : 2 =', ((3+5*2) + 1) / 2)
print('-3^2+5*3-7 =', -3**2 + 5*3 - 7)

# 1.
print('5:2-4 =', None)

# 2.
print('5·12+6-1 =', None)

# 3.
print('3(5+2) =', None)

# 4.
print('4[(5+3):2 +7] =', None)

# 5.
print('(−4)^(-3)+5·(3−7:2) =', None)
