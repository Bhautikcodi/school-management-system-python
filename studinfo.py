import os
import subprocess
os.system('cls')
import pandas as pd
print('#'*75)
print('Student Portal'.center(70))
print('#'*75)
roll_no = int(input("Enter roll number (ID): "))
student_class = int(input("Enter class (1 to 12): "))


df = pd.read_csv("Students.CSV")


students_data = df[(df['ID'] == roll_no) & (df['Class'] ==student_class)]
print("\nStudent Details:")
for index, row in students_data.iterrows():
        print(f"ID: {row['ID']}")
        print(f"Full Name: {row['Full Name']}")
        print(f"Email: {row['Email']}")
        print(f"Phone Number: {row['Phone Number']}")
        print(f"Date of Birth: {row['Date of Birth']}")
        print(f"Class: {row['Class']}")
x = input('Do you want to exit ?(yes) :')
if x == 'yes' :
        print('Exiting.....')
        subprocess.run('python UserLogin.py')
