"""
### Problem 5: For-loops & Fibonacci
The Fibonacci sequence is a sequence of integers. The sequence is defined as:
$$f(0) = 0\\f(1) = 1\\f(n) = f(n-1) + f(n-2)$$
Tasks:
1. Implement a program which calculates the *n*th Fibonacci number. _n_ should be an input from the user.
2. The program should calculate the sum of all Fibonacci up to and including the *n*th number.
3. The list of all the Fibonacci numbers up to the *n*th number should be printed to the screen.
"""

# Write your code here!


def fib(n):
    fibonacci_seq = [0, 1]

    for i in range(1, n+1):
        fibonacci_seq.append(fibonacci_seq[i-1] + fibonacci_seq[i])

    return fibonacci_seq

"""
seq = fib(int(input("n: ")))
print("The n-th Fibonacci number is:", seq[-1])
print("The sum of all Fibonacci numbers up to and including the n-th number is", sum(seq))
print("The Fibonacci numbers up to and including the n-th number are", seq)
"""