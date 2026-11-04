import os
import zipfile
import curses
import numpy as np
from domains import Student, Course
from input import read_text, input_students, input_courses, input_marks
from output import write_line, show_lines, show_message

class StudentMarkSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def decompress_and_load(self):
        if os.path.exists("students.dat"):
            with zipfile.ZipFile("students.dat", "r") as zip_ref:
                zip_ref.extractall()

        if os.path.exists("students.txt"):
            with open("students.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        self.students.append(Student(parts[0], parts[1], parts[2]))

        if os.path.exists("courses.txt"):
            with open("courses.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        self.courses.append(Course(parts[0], parts[1], int(parts[2])))

        if os.path.exists("marks.txt"):
            with open("marks.txt", "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        cid, sid, mark = parts[0], parts[1], float(parts[2])
                        if cid not in self.marks:
                            self.marks[cid] = {}
                        self.marks[cid][sid] = mark

    def compress_on_exit(self):
        files = ["students.txt", "courses.txt", "marks.txt"]
        with zipfile.ZipFile("students.dat", "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                if os.path.exists(file):
                    zipf.write(file)

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
        show_lines(
            stdscr,
            "Student List (GPA descending)",
            [f"{s.get_id()} | {s.get_name()} | DoB: {s.get_dob()} | GPA: {s.get_gpa():.2f}"
             for s in self.students],
        )

    def show_courses(self, stdscr):
        show_lines(
            stdscr,
            "Course List",
            [f"{c.get_id()} | {c.get_name()} | {c.get_credits()} credits"
             for c in self.courses],
        )

    def draw_menu(self, stdscr):
        stdscr.clear()
        stdscr.box()
        write_line(stdscr, 1, " Student Mark System (PW5 - Persistent Info) ")
        write_line(stdscr, 3, "1. Input students")
        write_line(stdscr, 4, "2. Input courses")
        write_line(stdscr, 5, "3. Input marks for a course")
        write_line(stdscr, 6, "4. Show students sorted by GPA")
        write_line(stdscr, 7, "5. Show course list")
        write_line(stdscr, 8, "6. Exit")
        write_line(stdscr, 10, "Choose (1-6): ")
        stdscr.refresh()

    def run(self, stdscr):
        self.decompress_and_load()

        while True:
            self.draw_menu(stdscr)
            curses.echo()
            choice = stdscr.getstr(10, 16, 2).decode("utf-8").strip()
            curses.noecho()

            if choice == '1':
                input_students(stdscr, self.students)
            elif choice == '2':
                input_courses(stdscr, self.courses)
            elif choice == '3':
                input_marks(stdscr, self.students, self.courses, self.marks)
            elif choice == '4':
                self.sort_and_show_students(stdscr)
            elif choice == '5':
                self.show_courses(stdscr)
            elif choice == '6':
                self.compress_on_exit()
                break
            else:
                show_message(stdscr, "Invalid choice. Press any key to try again.")

if __name__ == "__main__":
    app = StudentMarkSystem()
    curses.wrapper(app.run)