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
