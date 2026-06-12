import os
import subprocess
import pandas as pd

os.system('cls' if os.name == 'nt' else 'clear')

print('#' * 70)
print('CLASS TIMETABLE'.center(70))
print('#' * 70)

timetable_df = pd.read_csv("timetable.csv")

class_name = int(input("Enter class (1-12) to view timetable: "))

if class_name in timetable_df['Class'].values:

    print(f"\nTimetable for Class {class_name}")
    print("-" * 90)
    print(f"{'Day':<10} | {'Period 1':<10} | {'Period 2':<10} | {'Period 3':<10} | {'Period 4':<10} | {'Period 5':<10}")
    print("-" * 90)

    class_row = timetable_df[timetable_df['Class'] == class_name].iloc[0]

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    for day in range(5):
        start = 1 + day * 5
        end = start + 5

        periods = class_row[start:end].values

        print(
            f"{days[day]:<10} | "
            f"{periods[0]:<10} | "
            f"{periods[1]:<10} | "
            f"{periods[2]:<10} | "
            f"{periods[3]:<10} | "
            f"{periods[4]:<10}"
        )

    choice = input("\nDo you want to exit? (yes/no): ").strip().lower()

    if choice == "yes":
        print("Exiting...")
        subprocess.run(["python", "UserLogin.py"])
        exit()

else:
    print(f"Class {class_name} not found in the timetable.")
    subprocess.run(["python", "UserLogin.py"])