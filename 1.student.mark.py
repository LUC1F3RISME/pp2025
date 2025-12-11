students = []
courses = []
marks = {}


def input_number_of_students():
    count = int(input("Enter number of students: "))
    return count

def input_student_information():
    print("\n--- Input Student Info ---")
    num = input_number_of_students()
    for i in range(num):
        print(f"Student {i + 1}:")
        sid = input(" ID: ")
        name = input(" Name: ")
        dob = input(" DoB: ")

        student = {'id': sid, 'name': name, 'dob': dob}
        students.append(student)

def input_number_of_courses():
    count = int(input("Enter number of courses: "))
    return count

def input_course_information():
    print("\n--- Input Course Info ---")
    num = input_number_of_courses()
    for i in range(num):
        print(f"Course {i + 1}:")
        cid = input(" ID: ")
        name = input(" Name: ")
        
        course = {'id': cid, 'name': name}
        courses.append(course)

def input_marks():
    print("\n--- Input Marks ---")
    list_courses()
    course_id = input("Select Course ID: ")
    
    found = False
    for c in courses:
        if c['id'] == course_id:
            found = True
            break
            
    if not found:
        print("Course not found!")
        return

    for s in students:
        mark = float(input(f"Enter mark for {s['name']} (ID: {s['id']}): "))
        
        key = (s['id'], course_id) 
        marks[key] = mark

def list_students():
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")

def list_courses():
    print("\n--- Course List ---")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def show_student_marks():
    print("\n--- Show Marks ---")
    list_courses()
    course_id = input("Select Course ID to view: ")
    
    print(f"\nMarks for Course {course_id}:")
    for s in students:
        key = (s['id'], course_id)
        
        mark = marks.get(key, "N/A") 
        print(f"Student: {s['name']}, Mark: {mark}")

while True:
    print("USER MENU")
    print("1. Input Students")
    print("2. Input Courses")
    print("3. List Students")
    print("4. List Courses")
    print("5. Input Marks")
    print("6. Show Marks")
    print("0. Exit")
    
    option = input("Choose option: ")
    
    if option == "1":
        input_student_information()
    elif option == "2":
        input_course_information()
    elif option == "3":
        list_students()
    elif option == "4":
        list_courses()
    elif option == "5":
        input_marks()
    elif option == "6":
        show_student_marks()
    elif option == "0":
        print("Exiting...")
        break
    else:
        print("Invalid option")