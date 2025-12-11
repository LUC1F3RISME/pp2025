class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.dob = ""

    def input_entity(self):
        self.id = input(" ID: ")
        self.name = input(" Name: ")
        self.dob = input(" DoB: ")

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self):
        self.id = ""
        self.name = ""

    def input_entity(self):
        self.id = input(" ID: ")
        self.name = input(" Name: ")

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class SchoolSystem:
    def __init__(self):

        self.students = []
        self.courses = []
        self.marks = {}

    def input_number_of_entities(self, entity_type):
        count = int(input(f"Enter number of {entity_type}: "))
        return count

    def input_students(self):
        print("\nInput student info")
        num = self.input_number_of_entities("students")
        for i in range(num):
            print(f"Student {i + 1}:")
            student = Student()
            student.input_entity()
            self.students.append(student)

    def input_courses(self):
        print("\nInput course info")
        num = self.input_number_of_entities("courses")
        for i in range(num):
            print(f"Course {i + 1}:")
            course = Course()
            course.input_entity()
            self.courses.append(course)

    def list_students(self):
        print("\nStudent list")
        for s in self.students:
            print(s)

    def list_courses(self):
        print("\nCourse list")
        for c in self.courses:
            print(c)

    def input_marks(self):
        print("\nInput marks")
        self.list_courses()
        course_id = input("Select course ID: ")

        found_course = False
        for c in self.courses:
            if c.id == course_id:
                found_course = True
                break
        
        if not found_course:
            print("Course not found!")
            return

        for s in self.students:
            mark = float(input(f"Enter mark for {s.name} (ID: {s.id}): "))
            key = (s.id, course_id)
            self.marks[key] = mark

    def show_student_marks(self):
        print("\nShow marks")
        self.list_courses()
        course_id = input("Select course ID to view: ")

        print(f"\nMarks for course {course_id}:")
        for s in self.students:
            key = (s.id, course_id)
            mark = self.marks.get(key, "N/A")
            print(f"Student: {s.name}, Mark: {mark}")

    def menu(self):
        while True:
            print("User menu")
            print("1. Input students")
            print("2. Input courses")
            print("3. List students")
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