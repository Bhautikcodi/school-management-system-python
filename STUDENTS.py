import os
import subprocess
os.system('cls')
import pandas as pd

print('#'*75)
print("STUDENTS Management ".center(70))
print('#'*75)

print("1. View Student Data")
print("2. Add New Student")
print("3. Update  Student Record")
print("4. Exit") 
choice = input("Enter your choice (1-4): ")

if choice == '1':
        print('\n')
        print('View Student Data')
        roll_no = int(input("Enter roll number (ID): "))
        student_class = int(input("Enter class (1 to 12): "))
        df = pd.read_csv("Student.CSV")
        students_data = df[(df['ID'] == roll_no) & (df['Class'] ==student_class)]
        print("\nStudent Details:")
        for index, row in students_data.iterrows():
                print(f"ID: {row['ID']}")
                print(f"Full Name: {row['Full Name']}")
                print(f"Email: {row['Email']}")
                print(f"Phone Number: {row['Phone Number']}")
                print(f"Date of Birth: {row['Date of Birth']}")
                print(f"Class: {row['Class']}")

if choice == '2':
        print('\n')
        print('Add New Student')
        t_id = input("Enter student ID: ")
        full_name = input("Enter full name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")
        dob = input("Enter date of birth (YYYY-MM-DD): ")
        student_class = input("Enter class (1 to 12): ")
        new_data = pd.DataFrame([[t_id,full_name,email,phone,dob,student_class]],columns = ['ID','Full Name','Email','Phone Number','Date of Birth','Class'])
        df = pd.read_csv("Students.CSV")
        pd.concat([df, new_data], ignore_index=True)
        df.to_csv("Student.CSV", index=False)
        print(f"Student {full_name} added successfully!")

if choice =='3' :
        print('\n')
        print('Update Student record')
        df = pd.read_csv("C:\\Users\\BHAUTIK\\Desktop\\GROUP PROJECT\\Students1.CSV")
        t_id = int(input("Enter Student ID to update: "))
        if t_id in df['ID'].values:
                print("\nCurrent Record:")
                print(df[df['ID'] == t_id])
                print("\nEnter new details (leave blank to keep existing value):")
                full_name = input("Full Name: ")
                email = input("Email: ")
                phone = int(input("Phone Number: "))
                dob = input("Date of Birth (YYYY-MM-DD): ")
                student_class = int(input("Class (1-12): "))
                df.loc[df['ID'] == t_id, 'Full Name'] = full_name if full_name else df.loc[df['ID'] == t_id, 'Full Name']
                df.loc[df['ID'] == t_id, 'Email'] = email if email else df.loc[df['ID'] == t_id, 'Email']
                df.loc[df['ID'] == t_id, 'Phone Number'] = phone if phone else df.loc[df['ID'] == t_id, 'Phone Number']
                df.loc[df['ID'] == t_id, 'Date of Birth'] = dob if dob else df.loc[df['ID'] == t_id, 'Date of Birth']
                df.loc[df['ID'] == t_id, 'Class'] = student_class if student_class else df.loc[df['ID'] == t_id, 'Class']
                df.to_csv("Students.CSV", index=False)
                print("\nStudent record updated successfully!")

elif choice == '4':
        print("Exiting the system.")
        subprocess.run('python AdminLogin.py')
