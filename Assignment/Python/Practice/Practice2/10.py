# Takes the above list as input.

# Returns a dictionary mapping each student's name to their average marks.


students = [
    {"name": "Ali", "marks": [75, 80, 65]},
    {"name": "Sara", "marks": [90, 85, 88]},
    {"name": "John", "marks": [60, 70, 72]}
]

averages = {}

for student in students:
    name = student["name"]
    marks = student["marks"]
    avg = sum(marks) / len(marks)
    averages[name] = avg

print(averages)