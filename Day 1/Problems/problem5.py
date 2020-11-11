"""
### Problem 5: For-loops & Fibonacci
The Fibonacci sequence is a sequence of integers. The sequence is defined as:
$$f(0) = 0\\f(1) = 1\\f(n) = f(n-1) + f(n-2)$$
Tasks:
1. Implement a program which calculates the *n*th Fibonacci number. _n_ should be an input from the user.
2. The program should calculate the sum of all Fibonacci up to and including the *n*th number.
3. The list of all the Fibonacci numbers up to the *n*th number should be printed to the screen.
"""

n = int(input("n: "))

f0 = 0
f1 = 1

fib_numbers = [f0, f1]

for i in range(2, n+1):
    result = fib_numbers[i-1] + fib_numbers[i-2]
    fib_numbers.append(result)

print(fib_numbers[-1])

