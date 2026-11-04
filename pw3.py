import math
import numpy as np
import curses

class Student:
    def __init__(self, sid="", name="", dob=""):
        self.__sid = sid
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self): return self.__sid
    def get_name(self): return self.__name
    def get_dob(self): return self.__dob
    def get_gpa(self): return self.__gpa
    def set_gpa(self, gpa): self.__gpa = gpa


class Course:
    def __init__(self, cid="", name="", credits=0):
        self.__cid = cid
        self.__name = name
        self.__credits = credits

    def get_id(self): return self.__cid
    def get_name(self): return self.__name
    def get_credits(self): return self.__credits


class StudentMarkSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def _write_line(self, stdscr, row, text):
        height, width = stdscr.getmaxyx()
        if 0 <= row < height - 1 and width > 1:
            stdscr.addnstr(row, 1, str(text), width - 2)

    def _read_text(self, stdscr, prompt):
        stdscr.clear()
        stdscr.box()
        stdscr.addstr(2, 2, prompt)
        stdscr.addstr(4, 2, "> ")
        stdscr.refresh()
        curses.echo()
        value = stdscr.getstr(4, 4).decode("utf-8").strip()
        curses.noecho()
        return value

    def _read_number(self, stdscr, prompt, number_type):
        while True:
            value = self._read_text(stdscr, prompt)
            try:
                return number_type(value)
            except ValueError:
                self._show_message(stdscr, "Invalid number. Press any key to try again.")

    def _show_message(self, stdscr, message):
        stdscr.clear()
        stdscr.box()
        stdscr.addstr(2, 2, message)
        stdscr.addstr(4, 2, "Press any key to continue")
        stdscr.refresh()
        stdscr.getch()

    def _show_lines(self, stdscr, title, lines):
        height, width = stdscr.getmaxyx()
        page_size = max(1, height - 5)
        lines = lines or ["No records."]
        pages = (len(lines) + page_size - 1) // page_size

        for page in range(pages):
            stdscr.clear()
            stdscr.box()
            self._write_line(stdscr, 1, title)
            start = page * page_size
            for row, line in enumerate(lines[start:start + page_size], start=3):
                self._write_line(stdscr, row, line)
            footer = "Press any key to continue" if page + 1 < pages else "Press any key to return"
            self._write_line(stdscr, height - 2, footer)
            stdscr.refresh()
            stdscr.getch()

    def input_students(self, stdscr):
        num_students = self._read_number(stdscr, "Number of students: ", int)
        for i in range(max(0, num_students)):
            sid = self._read_text(stdscr, f"Student {i + 1} ID: ")
            name = self._read_text(stdscr, "Name: ")
            dob = self._read_text(stdscr, "Date of birth: ")
            self.students.append(Student(sid, name, dob))
        self._show_message(stdscr, "Students saved")

    def input_courses(self, stdscr):
        num_courses = self._read_number(stdscr, "Number of courses: ", int)
        for i in range(max(0, num_courses)):
            cid = self._read_text(stdscr, f"Course {i + 1} ID: ")
            name = self._read_text(stdscr, "Name: ")
            credits = self._read_number(stdscr, "Credits: ", int)
            self.courses.append(Course(cid, name, credits))
        self._show_message(stdscr, "Courses saved")

    def input_marks(self, stdscr):
        if not self.courses or not self.students:
            self._show_message(stdscr, "Input students and courses first. Press any key.")
            return

        self._show_lines(
            stdscr,
            "Courses",
            [f"{course.get_id()} | {course.get_name()} | {course.get_credits()} credits"
             for course in self.courses],
        )
        cid = self._read_text(stdscr, "Course ID for marks: ")
        if cid not in [c.get_id() for c in self.courses]:
            self._show_message(stdscr, "Course ID not found. Press any key.")
            return

        if cid not in self.marks:
            self.marks[cid] = {}

        for student in self.students:
            raw_mark = self._read_number(
                stdscr,
                f"Mark for {student.get_name()} (ID: {student.get_id()}): ",
                float,
            )
            floored_mark = math.floor(raw_mark * 10) / 10.0
            self.marks[cid][student.get_id()] = floored_mark

        self._show_message(stdscr, "Marks saved. Press any key.")

    def calculate_gpa(self):
        for student in self.students:
            sid = student.get_id()
            s_marks = []
            s_credits = []
            for course in self.courses:
                cid = course.get_id()
                if cid in self.marks and sid in self.marks[cid]:
                    s_marks.append(self.marks[cid][sid])
                    s_credits.append(course.get_credits())

            if s_credits:
                marks_np = np.array(s_marks)
                credits_np = np.array(s_credits)
                gpa = np.sum(marks_np * credits_np) / np.sum(credits_np)
                student.set_gpa(round(gpa, 2))
            else:
                student.set_gpa(0.0)

    def sort_and_show_students(self, stdscr):
        self.calculate_gpa()
        self.students.sort(key=Student.get_gpa, reverse=True)
        self._show_lines(
            stdscr,
            "Student List (GPA descending)",
            [f"{s.get_id()} | {s.get_name()} | DoB: {s.get_dob()} | GPA: {s.get_gpa():.2f}"
             for s in self.students],
        )

    def show_courses(self, stdscr):
        self._show_lines(
            stdscr,
            "Course List",
            [f"{c.get_id()} | {c.get_name()} | {c.get_credits()} credits"
             for c in self.courses],
        )

    def run(self, stdscr):
        while True:
            stdscr.clear()
            stdscr.box()
            self._write_line(stdscr, 1, "Student Mark System")
            self._write_line(stdscr, 3, "1. Input students")
            self._write_line(stdscr, 4, "2. Input courses")
            self._write_line(stdscr, 5, "3. Input marks for a course")
            self._write_line(stdscr, 6, "4. Show students sorted by GPA")
            self._write_line(stdscr, 7, "5. Show course list")
            self._write_line(stdscr, 8, "6. Exit")
            stdscr.refresh()
            choice = self._read_text(stdscr, "Choose (1-6): ")

            if choice == '1':
                self.input_students(stdscr)
            elif choice == '2':
                self.input_courses(stdscr)
            elif choice == '3':
                self.input_marks(stdscr)
            elif choice == '4':
                self.sort_and_show_students(stdscr)
            elif choice == '5':
                self.show_courses(stdscr)
            elif choice == '6':
                break
            else:
                self._show_message(stdscr, "Invalid choice. Press any key to try again.")

if __name__ == "__main__":
    app = StudentMarkSystem()
    curses.wrapper(app.run)