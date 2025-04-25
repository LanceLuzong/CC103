
file_path = r"C:\Users\luzon\Documents\2ND SEM\CODES\ACT6.txt"

try:
    with open(file_path, "w") as file:
        student_records = int(input("Enter number of students: "))
    
    for i in range (student_records):
        with open(file_path, "a") as file:
            print ("Student records")
            name= input("Enter student name: ")
            Number = int(input("Enter student ID: "))
            Course = input("Enter student course: ")
            
           
            file.write(f"{name}\n")
            file.write(f"{Number}\n")
            file.write(f"{Course}\n")
            file.write("- " * 20)
            file.write("\n")
            print("Student records written successfully\n")
            
            
except PermissionError as e:
    print(" Error {e} - Ypu do not have permission to write to this file")  
except ValueError as e:
    print("Error {e} - Invlid input, Please enter a valid number")
except IOError as e:
    print(" Error {e} - An I/O error occurred ")

    
    
            

        
        

    
