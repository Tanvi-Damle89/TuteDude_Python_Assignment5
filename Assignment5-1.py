# Task 1: Create a Dictionary of Student Marks

# Step 1: Create the dictionary
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 74,
    "Eva": 88
}

# Step 2: Ask user to input the student's name
name = input("Enter the student's name: ")

# Step 3: Retrieve and display marks
if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print(f"Student '{name}' does not exist in the records.")
