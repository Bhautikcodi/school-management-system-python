import subprocess
import os
import getpass
os.system('cls')
print('#'*75)
print("WELCOME TO LOGIN SCREEN FOR ADMIN".center(75))
print('#'*75)
uname=input('Enter your user name :')
pwd=getpass.getpass()
uname=='Admin'  
pwd=='admin@123' 
if uname !='Admin' and pwd !='admin@123' :
        print('!!!!Please check your user name and password!!!!')
        print("Exiting...")
        subprocess.run('python AdminLogin.py')
        
print(' '*15,'SELECT OPTION TO WORK')
print('1. TEACHERS MANAGEMENT')
print('2. STUDENT MANAGEMENT')
print('3. Add Students Mark')
print('4. Exit')
ch=int(input('Enter your choice :'))
if ch==1:
        subprocess.run('python TEACHERS.py')
elif ch==2:
        subprocess.run('python STUDENTS.py')
elif ch==3:
        subprocess.run('python Addmark.py')
elif ch==4:
        print("Exiting...")
        subprocess.run('python main.py')
else:
        print('Invalid option')
