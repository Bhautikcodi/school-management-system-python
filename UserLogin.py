import subprocess
import os
import getpass
os.system('cls')
print('#'*74)
print('#'*20,"WELCOME TO LOGIN SCREEN FOR USER",'#'*20)
print('#'*74)
uname=input('Enter your user name :')
pwd=getpass.getpass()
uname=='User' 
pwd=='user@123'

if uname !='User' and pwd !='user@123' :
        print('!!!!Please check your user name and password!!!!')
        subprocess.run('python UserLogin.py')

print('SELECT OPTION TO WORK'.center(75))
print("1. Student Portal")
print("2. Timetable or Schedule of Week")
print("3. Academic Report")
print('4. Exit')
ch=int(input('Enter your choice :'))
if ch==1:
        subprocess.run('python studinfo.py')
elif ch==2:
        subprocess.run('python timetable.py')
elif ch==3:
        subprocess.run('python Viewmark.py')
elif ch == 4 :
        subprocess.run('python main.py')
else :
        print('Invalid option')
