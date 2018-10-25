from Problems.solutions.problem5 import fib

"""
### Problem 7: File handling, importing, dictionaries and functions
This problem is divided into 3 parts, and each part could potentially be its own function, but that's up to you:
1. Store the *n* first Fibonacci numbers to a file called *fibonacci.txt*. Make sure to re-use the Fibonacci function
   implemented earlier.
2. Read the file your wrote to in the previous step and store the number of occurences of each individual character in
   that file to a dictionary
3. Print the key in the dictionary from the previous step that has the highest value, i.e. print the character that
   appeared most times in the file.
"""

# Write your code here!


def write():
    with open("fibonacci.txt", "w") as fibonacci_file:
        fib_sequence = fib(100)

        for fib_number in fib_sequence:
            string_for_file = str(fib_number) + "\n"
            fibonacci_file.write(string_for_file)


def read():
    with open("fibonacci.txt", "r") as fibonacci_file:
        return fibonacci_file.readlines()


def get_occurrence_dictionary(lines):
    occurrence_dict = {key: value for key, value in [(i,0) for i in range(10)]}

    for line in lines:
        for char in line:
            if char.isdigit():
                occurrence_dict[int(char)] += 1

    return occurrence_dict


def get_highest_occurrence(occurrence_dict):
    key_list = list(occurrence_dict.keys())
    curr_best = (key_list[0], occurrence_dict[key_list[0]])
    for key in key_list[1:]:
        if occurrence_dict[key] > curr_best[1]:
            curr_best = (key, occurrence_dict[key])

    return curr_best


print(get_highest_occurrence(get_occurrence_dictionary(read())))
