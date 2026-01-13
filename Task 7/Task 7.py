from datetime import date

attendance = {}

FILE_NAME = "attendance.txt"

# Load attendance from file
def load_from_file():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                date_key, data = line.strip().split(":", 1)
                students = {}
                for item in data.split(","):
                    name, status = item.split("-")
                    students[name] = status
                attendance[date_key] = students
    except FileNotFoundError:
        pass


# Save attendance to file
def save_to_file():
    with open(FILE_NAME, "w") as file:
        for date_key, students in attendance.items():
            student_data = ",".join(
                f"{name}-{status}" for name, status in students.items()
            )
            file.write(f"{date_key}:{student_data}\n")


# Mark attendance
def mark_attendance():
    today = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if today == "":
        today = str(date.today())

    attendance[today] = {}

    n = int(input("Enter number of students: "))

    for _ in range(n):
        name = input("Student name: ")
        status = input("Present / Absent: ").capitalize()
        attendance[today][name] = status

    save_to_file()
    print("Attendance marked successfully!")


# View attendance
def view_attendance():
    date_key = input("Enter date (YYYY-MM-DD): ")

    if date_key in attendance:
        print(f"\nAttendance for {date_key}:")
        for name, status in attendance[date_key].items():
            print(name, ":", status)
    else:
        print("No attendance found for this date.")


# Main menu
def main():
    load_from_file()

    while True:
        print("\n--- Date-wise Attendance Management System ---")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")


main()
