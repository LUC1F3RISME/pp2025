class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.dob = ""
        self.gpa = 0.0

    def input_entity(self):
        self.id = input(" ID: ")
        self.name = input(" Name: ")
        self.dob = input(" DoB: ")

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}, GPA: {self.gpa:.2f}"

class Course:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.credits = 0

    def input_entity(self):
        self.id = input(" ID: ")
        self.name = input(" Name: ")
        self.credits = int(input(" Credits: "))

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Credits: {self.credits}"

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
    def input_number_of_entities(self, entity_type):
        count = int(input(f"Enter number of {entity_type}: "))
        return count

    def input_students(self):
        print("\n--- Input Student Info ---")
        num = self.input_number_of_entities("students")
        for i in range(num):
            print(f"Student {i + 1}:")
            student = Student()
            student.input_entity()
            self.students.append(student)

    def input_courses(self):
        print("\n--- Input Course Info ---")
        num = self.input_number_of_entities("courses")
        for i in range(num):
            print(f"Course {i + 1}:")
            course = Course()
            course.input_entity()
            self.courses.append(course)

    def list_students(self):
        print("\n--- Student List (Sorted by GPA Descending) ---")
        self.students.sort(key=lambda x: x.gpa, reverse=True)
        
        for s in self.students:
            print(s)

    def list_courses(self):
        print("\n--- Course List ---")
        for c in self.courses:
            print(c)

    def input_marks(self):
        print("\n--- Input Marks ---")
        if not self.courses:
            print("No courses available.")
            return

        self.list_courses()
        course_id = input("Select course ID: ")

        found_course = None
        for c in self.courses:
            if c.id == course_id:
                found_course = c
                break
        
        if not found_course:
            print("Course not found!")
            return

        for s in self.students:
            try:
                raw_mark = float(input(f"Enter mark for {s.name} (ID: {s.id}): "))              
                rounded_mark = int(raw_mark * 10) / 10
                key = (s.id, course_id)
                self.marks[key] = rounded_mark
            except ValueError:
                print("Invalid input, skipping student.")
        self.calculate_all_gpas()
    def calculate_all_gpas(self):
        for student in self.students:
            total_weighted_score = 0
            total_credits = 0
            
            for course in self.courses:
                key = (student.id, course.id)
                if key in self.marks:
                    mark = self.marks[key]
                    credit = course.credits
                    
                    total_weighted_score += mark * credit
                    total_credits += credit
            
            if total_credits > 0:
                student.gpa = total_weighted_score / total_credits
            else:
                student.gpa = 0.0

    def show_student_marks(self):
        print("\n--- Show Marks ---")
        self.list_courses()
        course_id = input("Select course ID to view: ")

        print(f"\nMarks for course {course_id}:")
        found = False
        for s in self.students:
            key = (s.id, course_id)
            if key in self.marks:
                print(f"Student: {s.name}, Mark: {self.marks[key]}")
                found = True
        
        if not found:
            print("No marks found for this course.")

    def menu(self):
        while True:
            print("\n=== USER MENU ===")
            print("1. Input students")
            print("2. Input courses")
            print("3. List students (with GPA)")
            print("4. List courses")
            print("5. Input marks")
            print("6. Show marks")
            print("0. Exit")
            
            option = input("Choose option: ")
            
            if option == "1":
                self.input_students()
            elif option == "2":
                self.input_courses()
            elif option == "3":
                self.list_students()
            elif option == "4":
                self.list_courses()
            elif option == "5":
                self.input_marks()
            elif option == "6":
                self.show_student_marks()
            elif option == "0":
                print("Exiting...")
                break
            else:
                print("Invalid option")

if __name__ == "__main__":
    system = SchoolSystem()
    system.menu()