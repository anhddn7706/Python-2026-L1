import math
import curses
from output import show_message, show_lines
from domains import Student, Course

def read_text(stdscr, prompt):
    stdscr.clear()
    stdscr.box()
    stdscr.addstr(2, 2, prompt)
    stdscr.addstr(4, 2, "> ")
    stdscr.refresh()
    curses.echo()
    value = stdscr.getstr(4, 4).decode("utf-8").strip()
    curses.noecho()
    return value

def read_number(stdscr, prompt, number_type):
    while True:
        value = read_text(stdscr, prompt)
        try:
            return number_type(value)
        except ValueError:
            show_message(stdscr, "Invalid number. Press any key to try again.")

def input_students(stdscr, students):
    num_students = read_number(stdscr, "Number of students: ", int)
    for i in range(max(0, num_students)):
        sid = read_text(stdscr, f"Student {i + 1} ID: ")
        name = read_text(stdscr, "Name: ")
        dob = read_text(stdscr, "Date of birth: ")
        students.append(Student(sid, name, dob))

    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students:
            f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()}\n")

    show_message(stdscr, "Students saved to file")

def input_courses(stdscr, courses):
    num_courses = read_number(stdscr, "Number of courses: ", int)
    for i in range(max(0, num_courses)):
        cid = read_text(stdscr, f"Course {i + 1} ID: ")
        name = read_text(stdscr, "Name: ")
        credits = read_number(stdscr, "Credits: ", int)
        courses.append(Course(cid, name, credits))

    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in courses:
            f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")

    show_message(stdscr, "Courses saved to file")

def input_marks(stdscr, students, courses, marks):
    if not courses or not students:
        show_message(stdscr, "Input students and courses first. Press any key.")
        return

    show_lines(
        stdscr,
        "Courses",
        [f"{course.get_id()} | {course.get_name()} | {course.get_credits()} credits"
         for course in courses],
    )
    cid = read_text(stdscr, "Course ID for marks: ")
    if cid not in [c.get_id() for c in courses]:
        show_message(stdscr, "Course ID not found. Press any key.")
        return

    if cid not in marks:
        marks[cid] = {}

    for student in students:
        raw_mark = read_number(
            stdscr,
            f"Mark for {student.get_name()} (ID: {student.get_id()}): ",
            float,
        )
        floored_mark = math.floor(raw_mark * 10) / 10.0
        marks[cid][student.get_id()] = floored_mark

    with open("marks.txt", "w", encoding="utf-8") as f:
        for course_id, student_marks in marks.items():
            for student_id, mark in student_marks.items():
                f.write(f"{course_id},{student_id},{mark}\n")

    show_message(stdscr, "Marks saved to file. Press any key.")