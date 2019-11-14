# How to print multiple non-consecutive values from a list with Python

from operator import itemgetter
animals = ['bear', 'python', 'peacock',
           'kangaroo', 'whale', 'dog', 'cat', 'cardinal']
print(itemgetter(0, 3, 4, 1, 5)(animals))
print(animals)
print(type(animals))

# Slicing indexes

course_name = "Python Programming"

print(len(course_name))
print(course_name[0])
print(course_name[-1])

# Note here that the slicing ends at "t" and not at "h" because the indexing starts at [0]

print(course_name[0:3])

# if you leave off the opening number, Python will automotically assume it to be [0]

print(course_name[:3])

# This returns a copy of the original string

print(course_name[:])

# ESC character

new_course = "\"Intermediate\" Programming"
print(new_course)

# How to use backslash in a str

new__new_course = "Python\\Programming"
print(new__new_course)

# Breaks on a new line

new_new_new_course = "Python\nProgramming"
print(new_new_new_course)
