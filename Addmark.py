import pandas as pd

# Load the existing student data
df = pd.read_csv("Student.CSV")
print("#" * 75)
print("ADD STUDENT SUBJECT MARKS".center(75))
print("#" * 75)

# Input class and student ID
student_class = input("Enter the student's class (e.g., 1-12): ")
student_id = input("Enter the student's ID: ")
student_row = df[(df['ID'] == student_id) & (df['Class'] == student_class)]
subjects = ['Math', 'Science', 'English', 'History', 'Geography'] # Example subjects
marks = {}
for subject in subjects:
        marks[subject] = float(input(f"Enter marks for {subject}: "))
# Update the student's record in the DataFrame
for subject, mark in marks.items():
        column_name = f"{subject} Marks"
        if column_name not in df.columns:
                df[column_name] = None # Add new column if it doesn't exist
                df.loc[(df['ID'] == student_id) & (df['Class'] ==student_class), column_name] = mark
df.to_csv("Students.CSV", index=False)
print("Marks have been added successfully!")

