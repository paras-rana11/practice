# 1. Set Comprehensions
# Set comprehensions create sets in a concise way. A set is an unordered collection of unique elements.
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {x**2 for x in numbers if x % 2 == 0}  # Squares of even numbers only
print(even_squares)

# Syntax: {expression for item in iterable if condition}
# Parameters:
# - expression: The operation you want to apply to each item (e.g., `x**2`).
# - item: The current element from the iterable `numbers`.
# - iterable: The collection of elements to iterate over (`numbers` in this case).
# - condition: The optional condition that filters the items (e.g., `if x % 2 == 0`).

# 2. Dictionary Comprehensions
# Dictionary comprehensions allow you to create dictionaries in a single line.
numbers = [1, 2, 3, 4, 5]
squared_dict = {x: x**2 for x in numbers}  # Dictionary with numbers as keys and squares as values
print(squared_dict)

# Syntax: {key: value for item in iterable}
# Parameters:
# - key: The key for the dictionary (e.g., `x`).
# - value: The value associated with the key (e.g., `x**2`).
# - item: The current element from the iterable `numbers`.
# - iterable: The collection of elements to iterate over (`numbers` in this case).

# 3. Lambda Functions
# Lambda functions are anonymous, small functions that are defined in a single line.
add = lambda a, b: a + b  # Adds two numbers
print(add(3, 4))

# Syntax: lambda arguments: expression
# Parameters:
# - arguments: The parameters you pass to the function (e.g., `a` and `b`).
# - expression: The operation to be performed with those arguments (e.g., `a + b`).

# 4. map() Function
# The map() function applies a given function to all items in an iterable.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # Squares all numbers in the list
print(squared)

# Syntax: map(function, iterable, ...)
# Parameters:
# - function: The function you want to apply to each item (e.g., `lambda x: x**2`).
# - iterable: The collection of elements to which the function will be applied (`numbers` in this case).
# - additional iterables (optional): You can pass more than one iterable. The function should accept as many parameters as there are iterables.

a = [1, 2, 3]
result = map(lambda x: x * 2, a)  # Only one iterable (a), so the function takes one parameter.
print(list(result))  # Output: [2, 4, 6]

a = [1, 2, 3]
b = [4, 5, 6]
result = map(lambda x, y: x + y, a, b)  # Two iterables, so the function takes two parameters.
print(list(result))  # Output: [5, 7, 9]

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
result = map(lambda x, y, z: x + y + z, a, b, c)  # Three iterables, so the function takes three parameters.
print(list(result))

# 5. filter() Function
# filter() is used to filter elements from an iterable based on a condition.
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # Filters even numbers
print(evens)

# Syntax: filter(function, iterable)
# Parameters:
# - function: A function that returns a boolean value (`True` or `False`). It is applied to each item in the iterable (e.g., `lambda x: x % 2 == 0`).
# - iterable: The collection to filter based on the condition (e.g., `numbers`).

# 6. reduce() Function
# reduce() cumulatively applies a binary function to the items in an iterable.
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)  # Computes the product of all numbers
print(product)

# Syntax: reduce(function, iterable)
# Parameters:
# - function: A binary function that takes two arguments and returns a result (e.g., `lambda x, y: x * y`).
# - iterable: The collection to reduce based on the function (e.g., `numbers`).

# 7. zip() Function
# The zip() function combines elements from multiple iterables into tuples.
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 18]
zipped = list(zip(names, ages))  # Zips two lists into a list of tuples
print(zipped)

# Syntax: zip(iterable1, iterable2, ...)
# Parameters:
# - iterable1, iterable2, ...: The iterables to combine. The function pairs the elements at the same positions in each iterable.

# 8. Unpacking Iterables
# Unpacking allows breaking apart iterables into variables easily.
numbers = [1, 2, 3]
a, b, c = numbers  # Unpacks the list into three variables
print(a, b, c)

# Syntax: a, b, c = iterable
# Parameters:
# - iterable: The collection to unpack (e.g., `numbers`).
# - a, b, c: The variables that will receive the unpacked values.

# 9. Ternary Conditional Expression
# The ternary operator allows conditional expressions in a single line.
x = 10
result = "Even" if x % 2 == 0 else "Odd"  # Assign "Even" or "Odd" based on x
print(result)

# Syntax: value_if_true if condition else value_if_false
# Parameters:
# - condition: The condition to test (e.g., `x % 2 == 0`).
# - value_if_true: The value to return if the condition is `True` (e.g., `"Even"`).
# - value_if_false: The value to return if the condition is `False` (e.g., `"Odd"`).

# 10. any() and all() Functions
# any() checks if any element in an iterable is True, and all() checks if all are True.
numbers = [1, 2, 3, 4, 5]
print(any(x > 3 for x in numbers))  # True if any number is greater than 3
print(all(x > 0 for x in numbers))  # True if all numbers are greater than 0

# Syntax: any(iterable), all(iterable)
# Parameters:
# - iterable: The collection of elements to check. `any()` returns `True` if any element is `True`, while `all()` returns `True` if all elements are `True`.

# 11. enumerate() Function
# enumerate() adds a counter to an iterable and returns an enumerate object.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Syntax: enumerate(iterable, start=0)
# Parameters:
# - iterable: The collection to enumerate (e.g., `fruits`).
# - start: The starting index (default is 0). If you want to start from another number, provide it (e.g., `start=1`).

# 12. sorted() Function
# The sorted() function returns a sorted list from any iterable.
numbers = [3, 1, 4, 2, 5]
sorted_numbers = sorted(numbers, reverse=True)  # Sorts the list in descending order
print(sorted_numbers)

# Syntax: sorted(iterable, key=None, reverse=False)
# Parameters:
# - iterable: The collection to be sorted (e.g., `numbers`).
# - key: A function to extract a comparison key from each element (default is `None`).
# - reverse: If `True`, sorts in descending order (default is `False`).

# 13. defaultdict from collections
# defaultdict provides a default value if a key doesn’t exist.
from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)
d["b"].append(2)
print(d)

# Syntax: defaultdict(default_factory)
# Parameters:
# - default_factory: A function that provides the default value (e.g., `list` or `int`). 

count = defaultdict(int)
for item in ['apple', 'banana', 'apple', 'banana', 'orange', 'apple', 'mango', 'orange']:
    count[item] += 1
print(count)

# 14. Counter from collections
# Counter counts the occurrences of elements in an iterable.
from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(word_count)

# Syntax: Counter(iterable)
# Parameters:
# - iterable: The collection to count occurrences from (e.g., `words`).
# It returns a dictionary-like object with the count of each element.

# 15. itertools.chain
# itertools.chain is used to concatenate multiple iterables into one.
import itertools

list1 = {1, 2, 0}
list2 = [3, 4]
list3 = [5, 6]

concatenated = list(itertools.chain(list1, list2, list3))
print(concatenated)

# Syntax: itertools.chain(iterable1, iterable2, ...)
# Parameters:
# - iterable1, iterable2, ...: The iterables to concatenate (e.g., `list1`, `list2`, `list3`).
# It returns an iterator that produces items from all the provided iterables, one after the other.

