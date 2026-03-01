# initialising dictionary

student_grades = {}   # empty dictionary

# Add new students

def add_student(name,grade):
    
    if name in student_grades:
        print(f" student '{name}' already exist.")
    else:    
        student_grades[name] = grade
        print(f"Added {name} with grade {grade}")



# update student grade

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name}'s grade updated to {grade}")

    else:
        print(f"Student '{name}' not found !")  


# delete student name 

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted")

    else:
        print(f"Student {name} not found ")  


# view all students

def display_all_students():
    if student_grades:
        print("\nStudent Records:")
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")

    else:
        print("No students found !")  


def get_valid_grade():
      while True:
        try:
            grade = int(input("Enter student grade (0 - 100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")       

def get_valid_name():
    while True:
    
        name = input("Enter Student Name : ").strip().title()
        if not name:
            print("Name can not be empty.") 
        elif not name.replace(" ","").isalpha():
            print("Name must contain alphabets")
        else:
            return name    
        

def main():
    while True:
        menu = """
 ========== Students Grades Management System =================

                (1. Add student)
                (2. Update student)
                (3. Delete student)
                (4. View student)
                (5. Exit )
=================================================================
            """
        print(menu)
        
        try:
            choice = int(input("Enter your choice : "))
        except ValueError:
            print("Invalid Input. Please enter number ") 
            continue 
        
        if choice == 1:
           name = get_valid_name()
           grade = get_valid_grade()
           add_student(name,grade)
           
        elif choice == 2:
            name = get_valid_name()
            grade = get_valid_grade()
            update_student(name,grade)

        elif choice == 3:
            name = get_valid_name()
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program ") 
            break

        else:
            print("Invalid choice ")  

    
main()   

   









