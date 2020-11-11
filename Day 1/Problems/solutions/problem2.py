'''
Problem 2: Lists
 1. Create a list containing the names of all the people in this room (up to 5)
 2. Sort the list in ascending order. HINT: The built in function sort might be useful
 3. Print out the name of the last person in the list
 4. Print the first half of the list
'''

# 1. List names
my_list = ["Viktoria", "Julia", "Jo", "Alexander"]
print(my_list)

# 2. Sort the list
my_list.sort()
print(my_list)

# 3. Print last name in list
print(my_list[-1])

# 4. Print first half of the list
print(my_list[:len(my_list)//2])



my_list.append("Magnus")
