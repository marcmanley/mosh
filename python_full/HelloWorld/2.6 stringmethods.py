# functions
# i.e., len() where the () designate a function

# functions that are related to str
course = "python programming"

# here we have a kind of function called a "method" which
# comes after a str and designated by a "."
# in Py all everything is an object
# and objects have "functions"
# and "functions" have "methods"

print(course.upper())
print(course)
print(course.capitalize())
print(course.istitle())
print(course.title())

# you can make a new var/str based off of a method applied to another str/var

upper_course = course.upper()
print(upper_course)
lower_course = upper_course.lower()
print(lower_course)

# striping white space

unstriped_course = "   The unstriped Python Course"
print(unstriped_course)
striped_course = unstriped_course.strip()
print(striped_course)
