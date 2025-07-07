# 1. Set Comprehensions
# Set comprehensions create sets in a concise way. A set is an unordered collection of unique elements.
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {x**2 for x in numbers if x % 2 == 0}  # Squares of even numbers only
print(even_squares)

# Explanation:
# - This comprehension iterates over the list `numbers` and calculates the square of each even number.
# - A set is created with the squares of even numbers, so the result will only contain unique elements.
# Parameters:
# - x: The current element from the iterable `numbers`.
# - numbers: The iterable (list) we are iterating over.
# - if x % 2 == 0: A condition to select only even numbers.

# 2. Dictionary Comprehensions
# Dictionary comprehensions allow you to create dictionaries in a single line.
numbers = [1, 2, 3, 4, 5]
squared_dict = {x: x**2 for x in numbers}  # Dictionary with numbers as keys and squares as values
print(squared_dict)

# Explanation:
# - The comprehension iterates over `numbers`, and for each element `x`, a dictionary is created with `x` as the key and `x**2` as the value.
# Parameters:
# - x: The current element from the iterable `numbers`.
# - numbers: The iterable (list) we are iterating over.

# 3. Lambda Functions
# Lambda functions are anonymous, small functions that are defined in a single line.
add = lambda a, b: a + b  # Adds two numbers
print(add(3, 4))

# Explanation:
# - A lambda function is defined as `lambda a, b: a + b`. It accepts two parameters `a` and `b` and returns their sum.
# Parameters:
# - a: First argument.
# - b: Second argument.

# 4. map() Function
# The map() function applies a given function to all items in an iterable.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # Squares all numbers in the list
print(squared)

# Explanation:
# - `map()` applies the lambda function `lambda x: x**2` to every element of the iterable `numbers`. 
# - It returns an iterator, so we use `list()` to convert the result into a list.
# Parameters:
# - lambda x: x**2: A function that squares each element.
# - numbers: The iterable (list) that map() will iterate over.
# 
# * If you pass **one iterable**, the function should take **one argument**.
# * If you pass **two iterables**, the function should take **two arguments**.
# * If you pass **three iterables**, the function should take **three arguments**, and so on.

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

# Explanation:
# - `filter()` filters out the numbers that do not meet the condition (in this case, even numbers).
# - The lambda function checks if `x % 2 == 0` (if the number is even), and keeps only the even numbers.
# Parameters:
# - lambda x: x % 2 == 0: A function that checks if a number is even.
# - numbers: The iterable (list) that filter() will iterate over.


# 6. reduce() Function
# reduce() cumulatively applies a binary function to the items in an iterable.
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)  # Computes the product of all numbers
print(product)

# Explanation:
# - `reduce()` applies the lambda function `lambda x, y: x * y` cumulatively to the list `numbers`.
# - It starts with the first two elements, applies the operation, then uses the result with the next element, and so on.
# Parameters:
# - lambda x, y: x * y: A binary function that multiplies two numbers.
# - numbers: The iterable (list) to reduce.


# 7. zip() Function
# The zip() function combines elements from multiple iterables into tuples.
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 18]
zipped = list(zip(names, ages))  # Zips two lists into a list of tuples
print(zipped)

# Explanation:
# - `zip()` combines the elements from the iterables `names` and `ages` into tuples, each containing one element from each list.
# - The result is a list of tuples, where each tuple holds the corresponding elements from both iterables.
# Parameters:
# - names: The first iterable to zip.
# - ages: The second iterable to zip.


# 8. Unpacking Iterables
# Unpacking allows breaking apart iterables into variables easily.
numbers = [1, 2, 3]
a, b, c = numbers  # Unpacks the list into three variables
print(a, b, c)

# Explanation:
# - Unpacking breaks the iterable (in this case, the list `numbers`) into individual elements, assigning each element to a variable.
# Parameters:
# - numbers: The iterable to unpack into variables.
# - a, b, c: The variables that will hold the unpacked elements.


# 9. Ternary Conditional Expression
# The ternary operator allows conditional expressions in a single line.
x = 10
result = "Even" if x % 2 == 0 else "Odd"  # Assign "Even" or "Odd" based on x
print(result)

# Explanation:
# - This is a shorthand way of writing an if-else statement. If the condition `x % 2 == 0` is true, "Even" is returned, otherwise "Odd".
# Parameters:
# - x: The number to check.
# - condition: The condition to test.


# 10. any() and all() Functions
# any() checks if any element in an iterable is True, and all() checks if all are True.
numbers = [1, 2, 3, 4, 5]
print(any(x > 3 for x in numbers))  # True if any number is greater than 3
print(all(x > 0 for x in numbers))  # True if all numbers are greater than 0

# Explanation:
# - `any()` returns `True` if any element in the iterable satisfies the condition (`x > 3`), otherwise it returns `False`.
# - `all()` returns `True` if all elements in the iterable satisfy the condition (`x > 0`), otherwise it returns `False`.
# Parameters:
# - x: The current element in the iterable.


# 11. enumerate() Function
# enumerate() adds a counter to an iterable and returns an enumerate object.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# Explanation:
# - `enumerate()` adds an index counter to each element of the iterable `fruits` and returns a tuple `(index, fruit)`.
# Parameters:
# - fruits: The iterable to enumerate.
# - index: The counter that starts at 0 by default.


# 12. sorted() Function
# The sorted() function returns a sorted list from any iterable.
numbers = [3, 1, 4, 2, 5]
sorted_numbers = sorted(numbers, reverse=True)  # Sorts the list in descending order
print(sorted_numbers)

# Explanation:
# - `sorted()` returns a new list containing all the elements from `numbers`, sorted in the specified order (in this case, descending).
# Parameters:
# - numbers: The iterable (list) to be sorted.


# 13. defaultdict from collections
# defaultdict provides a default value if a key doesn’t exist.
from collections import defaultdict

d = defaultdict(list)
d["a"].append(1)
d["b"].append(2)
print(d)

# Explanation:
# - `defaultdict` automatically creates a new value for a key if it doesn't exist. In this case, it creates an empty list for missing keys.
# Parameters:
# - list: The default value type to create empty lists for keys that don’t exist.

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

# Explanation:
# - `Counter` counts how many times each item appears in the iterable `words`.
# Parameters:
# - words: The iterable (list) to count elements.


# 15. itertools.chain
# itertools.chain is used to concatenate multiple iterables into one.
import itertools

list1 = {1, 2, 0}
list2 = [3, 4]
list3 = [5, 6]

concatenated = list(itertools.chain(list1, list2, list3))
print(concatenated)

# Explanation:
# - `itertools.chain()` takes multiple iterables as arguments and returns a single iterable that contains all elements from the input iterables, one after the other.
# Parameters:
# - list1, list2, list3: The iterables to be chained together.



