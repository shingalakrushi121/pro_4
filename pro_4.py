
# Student Marks Analysis Program

# Input total number of students
n = int(input("Enter total number of students: "))

marks = []

# Input marks for each student
for i in range(n):
    mark = float(input(f"Enter marks for student {i + 1}: "))
    marks.append(mark)

# Calculate statistics
total_students = len(marks)
highest_marks = max(marks)
lowest_marks = min(marks)
average_marks = sum(marks) / total_students

# Pass mark is 35
passed = sum(1 for mark in marks if mark >= 35)
failed = total_students - passed
pass_percentage = (passed / total_students) * 100

# Sort marks
sorted_marks = sorted(marks)

# Calculate grades
grade_a = sum(1 for mark in marks if mark >= 90)
grade_b = sum(1 for mark in marks if 80 <= mark < 90)
grade_c = sum(1 for mark in marks if 70 <= mark < 80)
grade_d = sum(1 for mark in marks if 60 <= mark < 70)
grade_f = sum(1 for mark in marks if mark < 60)

# Display results
print("\n----- Student Marks Report -----")
print("Total Students:", total_students)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Marks:", round(average_marks, 1))
print("Passed:", passed)
print("Failed:", failed)
print(f"Pass Percentage: {pass_percentage:.1f}%")
print("Sorted Marks:", sorted_marks)
print("Grade A:", grade_a, "Students")
print("Grade B:", grade_b, "Students")
print("Grade C:", grade_c, "Students")
print("Grade D:", grade_d, "Students")
print("Grade F:", grade_f, "Students")
