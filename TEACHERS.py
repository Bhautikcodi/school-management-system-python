import pandas as pd
import os
import subprocess
os.system('cls')
df = pd.read_csv("Teachers.CSV")

print('#'*75)
print("TEACHERS MANAGEMENT".center(75))
print('#'*75)

print(' '*15,'SELECT OPTION TO WORK')
print("1. View Teachers record")
print("2. Add new teachers record")
print('3. Update teachers record')
print("4. Exit")
choice = input("Select an option: ")
if choice == '1':
        print("Teacher Records:")
        tr = pd.read_csv("Teachers.CSV")
        print(tr)
        y= input('Exit ? (yes):')
        while y == 'yes' :
                 print("Exiting...")
                 subprocess.run('python TEACHERS.py')
elif choice == '2':
        print("Add new record :")
        id = input("Enter teacher ID: ")
        name = input("Enter teacher name: ")
        subject = input("Enter teacher subject: ")
        new_data = pd.DataFrame([[id,name,subject]],columns = ['ID','Name','Subject'])
        pd.concat([df, new_data], ignore_index=True)
        df.to_csv("Teachers.CSV",index = False)
        print("New records added successfully.")
        x = input('Do you want to add new record ? (yes/no) :')
        while x == 'yes' :
                id = input("Enter teacher ID: ")
                name = input("Enter teacher name: ")
                subject = input("Enter teacher subject: ")
                new_data = pd.DataFrame([[id,name,subject]],columns = ['ID','Name','Subject'])
                pd.concat([df, new_data], ignore_index=True)
                df.to_csv("Teachers.CSV",index = False)
                print("New records added successfully.")
        while x == 'no' :
                 print("Exiting...")
                 subprocess.run('python TEACHERS.py')
elif choice == '3':
        print('\n')
        print('Update teachers record')
        t_id = input('Enter Teacher ID :')
        if t_id in df['ID'].values:
                print("\nCurrent Record:")
                print(df[df['ID'] == t_id])
                print("\nEnter new details (leave blank to keep existing value):")
                full_name = input("Full Name: ")
                subject = input("Subject: ")
                df.loc[df['ID'] == t_id, 'Name'] = full_name if full_name else df.loc[df['ID'] == t_id, 'Full Name']
                df.loc[df['ID'] == t_id, 'Subject'] = subject if subject else df.loc[df['ID'] == t_id, 'Subject']
                df.to_csv("TEACHERS.CSV", index=False)
                print("\nStudent record updated successfully!")
elif choice == '4':
        print("Exiting...")
        subprocess.run('python AdminLogin.py')
else:
        print("Invalid option, please try again.")
        subprocess.run('python AdminLogin.py')
