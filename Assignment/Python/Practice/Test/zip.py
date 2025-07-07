names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 95]

paired1 = zip(names, scores)


paired_list1 = list(paired1)
print(paired_list1)


l1 = ["Alice", "Bob", "Sara", "Charlie"]
l2 = [90, 85, 95, 70, 90, 88]
l3 = ['M', 'M', 'F', 'M']

paired2 = zip(l1, l2, l3)

paired_list2 = list(paired2)
print(paired_list2)

names, marks, gender = zip(*paired_list2)

print("names: ", names)
print(marks)
print(gender)


# Key Points to Remember:
# Zip function tuples create karta hai, jisme har tuple ka ek element har input iterable se hota hai, based on their positions.

# Unequal Lengths: Agar iterables ki lengths different hain, toh zip() sirf minimum length tak combine karega.

# Unzip: Aap zip(*iterable) ka use karke tuples ko unpack kar sakte hain aur separate lists ya values mein convert kar sakte hain.


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(zip(*matrix))
print(transposed)




products = ["Apple", "Banana", "Cherry"]
prices = [0.99, 0.5, 1.5]

# Pair products with prices
product_price_pairs = list(zip(products, prices))
print(product_price_pairs)


products = ["Apple", "Banana", "Cherry"]
prices = [0.99, 0.5, 1.5]

# Pair products with prices using zip() and convert to dictionary
product_price_dict = dict(zip(products, prices))

print(product_price_dict)


names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 92]

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
