# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Question 1:
# Write a function that takes a nested list and returns a flattened version of it.

# # Input: [1, [2, [3, 4], 5], 6]
# # Output: [1, 2, 3, 4, 5, 6]

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# Recursion
from collections.abc import Iterable


def flatten_nested_list(li):
    result = []

    for item in li:
        if isinstance(item, (list, tuple, set)):
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)
    return result


# li1 = [1, [2, [3, 4], 5], 6]
# li2 = flatten_nested_list(li1)
# print(li2)

# li3 = [1, [2, [3, (5, [54, {1, 2, 3}, 5], 4), 4], 5], 6]
# li4 = flatten_nested_list(li3)
# print(li4)


l1 = [1, [2, 3, 4], 5, 6, [7, 88, 9], 0, 33, 44, 55, [66, 777, 88]]
l2 = [1, 5, 8, 6, 3, 2, 5, (7, 88, 9)]
l3 = [2, 3, [1, 9, 0], 9, {6, 7, 4}, 4, 1, 8]

l4 = l1+l2+l3

l5 = [x
      for item in l4
      for x in (item if isinstance(item, (list, tuple, set)) else [item])]
print(l5)


l6 = [ele for li in l4 for ele in (li if isinstance(li, Iterable) else [li])]
print(l6)

# l7 = flatten_nested_list(l4)
# print(l7)


# Just Slicing
# items = [1, 4, 6, 10]
# last_item = items[-1:3]
# print(last_item)


# import time

# start_time = time.time()
# result = []
# for x in range(1000000):
#     result.append(x * 2)
# end_time = time.time()

# print(f"For loop took: {end_time - start_time} seconds")


# start_time = time.time()
# result = [x * 2 for x in range(1000000)]
# end_time = time.time()

# print(f"List comprehension took: {end_time - start_time} seconds")

# List comprehensions are optimized internally by Python. When you use a list comprehension, Python doesn't need to call the append() function multiple times in a loop. Instead, it handles the entire process of creating the list in one go, which makes it faster.





l1 = [1, [2, 3, 4], 5, 6, [7, [5, 7, 3], 88, 9], 0, 33, 44, 55, [66, 777, 88]]
l2 = [1, 5, 8, 6, 3, 2, 5, (7, 88, 9)]
l3 = [2, 3, [1, 9, 0], 9, {6, 7, 4}, 4, 1, 8]


l4 = l1+l2+l3
from _collections_abc import Iterable
def flatten_list(lst):
    return [x 
            for item in lst
            for item2 in (item if isinstance(item, Iterable) else [item])
            for x in (item2 if isinstance(item2, Iterable) else [item2])]

l5 = flatten_list(l4)

print(l5)     



 
l1 = [1, [2, 3, 4], 5, 6, [7, [5, 7,['hello', 'world'], 3], 88, 9], 0, 33, 44, 55, [66, 777, 88]]
l2 = [1, 5, 8, 6, 3, 2, 5, (7, 88, 9)]
l3 = [2, 3, [1, 9, 0], 9, {6, 7, 4}, 4, 1, 8]


def recursive_flatten_list(item):
    if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
        return [x 
                for subitem in item
                for x in recursive_flatten_list(subitem)]
    else:
        return [item]

l6 = l1+l2+l3

l7 = recursive_flatten_list(l6)

print("l7:", l7)




names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]

# Using zip in list comprehension to pair names with scores
paired_list = [(name, score) for name, score in zip(names, scores)]
print(paired_list)

names = ["Alice", "Bob", "Charlie"]
scores = [90, 45, 92]

# Using zip with list comprehension and adding a condition (selecting only scores > 80)
high_scores = [name for name, score in zip(names, scores) if score > 80]
print(high_scores)


numbers = [1, 2, 3, 4, 5]

# Using map in list comprehension to square each number
squared_numbers = [x ** 2 for x in map(lambda x: x, numbers)]
print(squared_numbers)


numbers = [1, 2, 3, 4, 5]

# Using map and list comprehension to multiply each number by 2, but only if it's odd
doubled_odds = [x * 2 for x in map(lambda x: x, numbers) if x % 2 != 0]
print(doubled_odds)

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce with a list comprehension to calculate the sum of numbers
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)


from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce to find the maximum value
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)


numbers = [5, 10, 15, 20, 25]

# Using filter in list comprehension to get only numbers greater than 10
filtered_numbers = [x for x in filter(lambda x: x > 10, numbers)]
print(filtered_numbers)




numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Using filter in list comprehension to keep only even numbers
even_numbers = [x for x in filter(lambda x: x % 2 == 0, numbers)]
print(even_numbers)
