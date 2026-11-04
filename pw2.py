class Student:
    def __init__(self, sid="", name="", dob=""):
        self.__sid = sid
        self.__name = name
        self.__dob = dob

    def get_id(self): return self.__sid
    def get_name(self): return self.__name
    def get_dob(self): return self.__dob

    def input(self):
        self.__sid = input("Enter student ID: ")
        self.__name = input("Enter student name: ")
        self.__dob = input("Enter student Date of Birth: ")

    def list(self):
        print(f"ID: {self.__sid}, Name: {self.__name}, DoB: {self.__dob}")


class Course:
    def __init__(self, cid="", name=""):
        self.__cid = cid
        self.__name = name

    def get_id(self): return self.__cid
    def get_name(self): return self.__name

    def input(self):
        self.__cid = input("Enter course ID: ")
        self.__name = input("Enter course name: ")

    def list(self):
        print(f"ID: {self.__cid}, Name: {self.__name}")


class StudentMarkSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}

    def input_students(self):
        num_students = int(input("Enter number of students in class: "))
        for i in range(num_students):
            print(f"\n Student {i+1} ")
            s = Student()
            s.input()
            self.__students.append(s)

    def input_courses(self):
        num_courses = int(input("\nEnter number of courses: "))
        for i in range(num_courses):
            print(f"\n Course {i+1} ")
            c = Course()
            c.input()
            self.__courses.append(c)

    def input_marks(self):
        cid = input("Enter course ID to input marks: ")
        if cid not in [c.get_id() for c in self.__courses]:
            print("Course ID not found.")
            return

        self.__marks[cid] = {}
        for student in self.__students:
            sid = student.get_id()
            mark = float(input(f"Enter mark for {student.get_name()} (ID: {sid}): "))
            self.__marks[cid][sid] = mark

    def show_students(self):
        print("\n Student List ")
        for student in self.__students:
            student.list()

    def show_courses(self):
        print("\n Course List ")
        for course in self.__courses:
            course.list()

    def show_marks(self):
        cid = input("Enter course ID to show marks: ")
        if cid not in self.__marks:
            print("No marks recorded for this course.")
            return
        print(f"\n Marks for Course ID: {cid} ")
        for sid, mark in self.__marks[cid].items():
            s_name = next((s.get_name() for s in self.__students if s.get_id() == sid), "Unknown")
            print(f"Student ID: {sid}, Name: {s_name}, Mark: {mark}")

    def run(self):
        self.input_students()
        self.input_courses()
        while True:
            print("\n Menu ")
            print("1. Input marks for a course:")
            print("2. Show student list:")
            print("3. Show course list:")
            print("4. Show marks for a course:")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1': self.input_marks()
            elif choice == '2': self.show_students()
            elif choice == '3': self.show_courses()
            elif choice == '4': self.show_marks()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = StudentMarkSystem()
    system.run()