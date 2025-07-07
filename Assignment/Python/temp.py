# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦

# l1 = [1, [2, 3, 4], 5, 6, [7, 88, 9], 0, 33, 44, 55, [66, 777, 88]]
# l2 = [1, 5, 8, 6, 3, 2, 5, (7, 88, 9)]
# l3 = [2, 3, [1, 9, 0], 9, {6, 7, 4}, 4, 1, 8]

# l4 = l1+l2+l3

# def flatten_list(lst):
#     return []


# ♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.__name}.")

    def introduce(self):
        print(f"I am {self.age} years old.")

    def age_info(self):
        print(f"{self.__name} is {self.age} years old.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.__name}! You are now {self.age} years old.")

# Create a list of Person objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Charlie", 35)

# Store the Person objects in a list
people = [person1, person2, person3]

# Loop through each Person object and call different methods
for person in people:
    print(person._Person__name)          # Print person's name
    person.greet()              # Calls greet method
    person.introduce()          # Calls introduce method
    person.age_info()           # Calls age_info method
    person.celebrate_birthday() # Calls celebrate_birthday method
    print('---')          