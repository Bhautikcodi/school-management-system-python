import pandas as pd
import matplotlib.pyplot as plt

file_path = "Students.CSV"

try:
    df = pd.read_csv(file_path)

    print("#" * 75)
    print("STUDENT MARKS VIEWER".center(75))
    print("#" * 75)

    student_class = input("Enter your class (e.g., 1-12): ").strip()
    student_id = input("Enter your student ID: ").strip()

    student_row = df[
        (df['ID'].astype(str) == student_id) &
        (df['Class'].astype(str) == student_class)
    ]

    if not student_row.empty:

        print("\nStudent Details:")
        print(f"Name: {student_row.iloc[0]['Full Name']}")
        print(f"Class: {student_class}")

        print("\nMarks Table:")
        print(f"Math: {student_row.iloc[0]['Math Marks']}")
        print(f"Science: {student_row.iloc[0]['Science Marks']}")
        print(f"English: {student_row.iloc[0]['English Marks']}")
        print(f"History: {student_row.iloc[0]['History Marks']}")
        print(f"Geography: {student_row.iloc[0]['Geography Marks']}")

        marks = {
            'Math': student_row.iloc[0]['Math Marks'],
            'Science': student_row.iloc[0]['Science Marks'],
            'English': student_row.iloc[0]['English Marks'],
            'History': student_row.iloc[0]['History Marks'],
            'Geography': student_row.iloc[0]['Geography Marks']
        }

        plt.bar(marks.keys(), marks.values())
        plt.ylim(0, 100)
        plt.title(f"Exam Marks for {student_row.iloc[0]['Full Name']}")
        plt.xlabel("Subjects")
        plt.ylabel("Marks (out of 100)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    else:
        print("\nNo student found with the given class and ID.")

except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")

except KeyError as e:
    print(f"Error: Missing expected column in the CSV file: {e}")

except Exception as e:
    print(f"An error occurred: {e}")