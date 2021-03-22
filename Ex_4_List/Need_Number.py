"""
A crazy trainer returns my grade into sigle string and I need to know the total and the average.
"""

test = "English=68 Logic=75 Uml=87 Code=80"
courses = test.split(" ")
count = 0
note = 0

for course in courses:
    note = note + int(course.split("=")[1])
    count = count + 1

average = note / count

print(average)
