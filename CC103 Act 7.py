file_path = r"C:\Users\luzon\Documents\2ND SEM\CODES\Act7.txt"

def save_records(records):
    try:
        with open(file_path, "w") as file:
            for record in records:
                file.write(f"{record}['ID'], {record['Name']}, {record['Course']}\n")
    except Exception as e:
        print(f"Error saving student records {e}")
def load_records():
    records = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                student_id, name, course = line.strip().split(", ")
                records.append({"ID": student_id, "Name": name, "Course": course})
    except FileNotFoundError as e:
        print(f"Error No Record Found {e}")
    except Exception as e:
        print(f"Error loading student records {e}")
    return records
def add_student(records):
    try:
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        course = input("Enter student course: ")
        records.append({"ID": student_id, "Name": name, "Course": course})
        save_records(records)
        print("Student record added successfully")
    except Exception as e:
        print(f"Error adding student record {e}")
        
def display_records(records):
    print("--" * 20)
    if not records:
        print("No records found")
        return
    print("--" * 20)
    print("\nStudent records:\n")
    for record in records:
        print(f"ID: {record['ID']}, Name: {record['Name']}, Course: {record['Course']}")
    print("--" * 20)
def main_menu():
    records = load_records()
    while True:
        print("\nStudent Record Management System")
        print("1. Add Student Record")
        print("2. Display Student Records")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student(records)
        elif choice == "2":
            display_records(records)
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again")
    print("Exiting program")

main_menu()