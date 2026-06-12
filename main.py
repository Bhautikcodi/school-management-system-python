import os
os.system('cls')
print('#'*75)
print("WELCOME TO SCHOOL MANAGEMENT SYSTEM".center(75))
print('#'*75)
print('SELECT THE INTERFACE IN WHICH YOU WANT TO WORK'.center(75))
print('1. Admin Interface')
print('2. User Interface')
ch= int(input('Enter your choice :'))
if ch==1:
    subprocess.run('python AdminLogin.py')
elif ch==2:
    subprocess.run('python UserLogin.py')
else:
    print('Invalid option')
    subprocess.run('python p1.py')

