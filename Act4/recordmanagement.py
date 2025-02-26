import os

# File to store student records
FileName = "StudentRecords.txt"
Records = []

# Ensure file exists
with open(FileName, "a") as f:
    pass

# Load existing records from file
with open(FileName, "r") as f:
    for line in f:
        Records.append(tuple(line.strip().split("|")))
    print("File loaded successfully.")

while True:
    # Display menu options
    print("\n1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Show Student Record")
    print("6. Add Record")
    print("7. Edit Record")
    print("8. Delete Record")

    choice = input("Enter choice: ")

    if choice == "1":
        # Open the file in Notepad
        os.system(f'notepad "{FileName}"')
    
    elif choice == "2":
        # Save current records to file
        with open(FileName, "w") as f:
            f.write("STUDENT ID  |      FULL NAME      | CLASS STANDING GRADE | MAJOR EXAM GRADE | FINAL GRADE\n")
            f.write("-" * 80 + "\n")
            for record in Records:
                final_grade = 0.6 * float(record[2]) + 0.4 * float(record[3])
                f.write(f"{record[0]:^10} | {record[1]:^20} | {record[2]:^20} | {record[3]:^20} | {final_grade:^10.2f}\n")
        print("Records saved successfully.")

    elif choice == "3":
        # Save records under a new filename
        new_file = input("Enter new filename: ")
        if not new_file.endswith(".txt"):
            new_file += ".txt"
        with open(new_file, "w") as f:
            f.write("STUDENT ID  |      FULL NAME      | CLASS STANDING GRADE | MAJOR EXAM GRADE | FINAL GRADE\n")
            f.write("-" * 80 + "\n")
            for record in Records:
                final_grade = 0.6 * float(record[2]) + 0.4 * float(record[3])
                f.write(f"{record[0]:^10} | {record[1]:^20} | {record[2]:^20} | {record[3]:^20} | {final_grade:^10.2f}\n")
        print(f"New copy of student records saved as {new_file} successfully.")

    elif choice == "4":
        # Display all student records sorted by last name or grade
        print("1. Order by Last Name")
        print("2. Order by Grade")
        sort_choice = input("Choose sorting method: ")
        
        if sort_choice == "1":
            sorted_records = sorted(Records, key=lambda r: r[1].split()[-1])
        elif sort_choice == "2":
            sorted_records = sorted(Records, key=lambda r: 0.6 * float(r[2]) + 0.4 * float(r[3]), reverse=True)
        else:
            print("Invalid choice. Returning to menu.")
            continue
        
        print("\nSTUDENT ID  |      FULL NAME      | CLASS STANDING GRADE | MAJOR EXAM GRADE | FINAL GRADE")
        print("-" * 80)
        for record in sorted_records:
            final_grade = 0.6 * float(record[2]) + 0.4 * float(record[3])
            print(f"{record[0]:^10} | {record[1]:^20} | {record[2]:^20} | {record[3]:^20} | {final_grade:^10.2f}")
    
    elif choice == "5":
        # Search for a student record by ID
        student_id = input("Enter Student ID: ")
        found = False
        for record in Records:
            if record[0] == student_id:
                final_grade = 0.6 * float(record[2]) + 0.4 * float(record[3])
                print("\nSTUDENT ID  |      FULL NAME      | CLASS STANDING GRADE | MAJOR EXAM GRADE | FINAL GRADE")
                print("-" * 80)
                print(f"{record[0]:^10} | {record[1]:^20} | {record[2]:^20} | {record[3]:^20} | {final_grade:^10.2f}")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "6":
        # Add a new student record
        student_id = input("Enter Student ID (6-digit): ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        full_name = first_name + " " + last_name
        class_standing = input("Enter Class Standing Grade: ")
        major_exam = input("Enter Major Exam Grade: ")

        Records.append((student_id, full_name, class_standing, major_exam))
        print("Record added but NOT saved yet. Choose option 2 to save.")

    elif choice == "7":
        # Edit an existing student record
        student_id = input("Enter Student ID to edit: ")
        for i, record in enumerate(Records):
            if record[0] == student_id:
                first_name = input("Enter New First Name (leave blank to keep current): ") or record[1].split()[0]
                last_name = input("Enter New Last Name (leave blank to keep current): ") or record[1].split()[-1]
                full_name = first_name + " " + last_name
                class_standing = input("Enter New Class Standing Grade (leave blank to keep current): ") or record[2]
                major_exam = input("Enter New Major Exam Grade (leave blank to keep current): ") or record[3]
                Records[i] = (student_id, full_name, class_standing, major_exam)
                print("Record updated. Remember to save (Option 2)!")
                break
        else:
            print("Student not found.")

    elif choice == "8":
        # Delete a student record by ID
        student_id = input("Enter Student ID to delete: ")
        Records = [record for record in Records if record[0] != student_id]
        print("Record deleted. Remember to save (Option 2)!")
        
    else:
        print("Invalid choice, please try again.")
