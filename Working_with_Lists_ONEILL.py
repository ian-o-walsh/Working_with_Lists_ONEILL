# Ian O'Neill
# IT 410
# Week 6 - Working with Lists Assignment
# Professor Charnesky

# List of all the courses I have taken at Walsh
courses_taken = ["com 405", "it 405", "it 407", "it 410"]

# Sort the list and print each course in uppercase
courses_taken.sort()
for course in courses_taken:
    print("I have taken " + course.upper() + " at Walsh College.")

# Add my courses planned for next term, resort, and print all
courses_taken.extend(["it 412", "it 461"])
courses_taken.sort()

print("\nThis is my course of study with upcoming courses added:")
for course in courses_taken:
    print(course.upper())

# Remove the courses I've already taken and print them
completed_courses = ["com 405", "it 405", "it 407", "it 410"]

print("\nI do not have to take these courses:")
for course in completed_courses:
    print(course.upper())
    courses_taken.remove(course)

# Print my courses left to take
print("\nI plan to take the following courses next term:")
for course in courses_taken:
    print(course.upper())
