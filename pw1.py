students = [] 
courses = [] 
marks = {} 
num_students = int(input("Enter number of students in class: "))
for i in range(num_students):
    print(f"\n Student {i+1} ")
    sid = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth: ")
    students.append((sid, name, dob))

num_courses = int(input("\nEnter number of courses: "))
for i in range(num_courses):
    print(f"\n Course {i+1} ")
    cid = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append((cid, name))
while True:
    print("\n Menu ")
    print("1. Input marks for a course")
    print("2. Show student list")
    print("3. Show course list")
    print("4. Show marks for a course")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        cid = input("Enter course ID to input marks: ")
        if cid not in [course[0] for course in courses]:
            print("Course ID not found.")
            continue
        marks[cid] = {}
        for student in students:
            sid = student[0]
            mark = float(input(f"Enter mark for {student[1]} (ID: {sid}): "))
            marks[cid][sid] = mark
            
    elif choice == '2':
        print("\n Student List: ")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")
            
    elif choice == '3':
        print("\n Course List: ")
        for course in courses:
            print(f"ID: {course[0]}, Name: {course[1]}")
            
    elif choice == '4':
        cid = input("Enter course ID to show marks: ")
        if cid not in marks:
            print("No marks recorded for this course.")
            continue
        print(f"\n Marks for Course ID: {cid} ")
        for sid, mark in marks[cid].items():
            student_name = next((s[1] for s in students if s[0] == sid), "Unknown")
            print(f"Student ID: {sid}, Name: {student_name}, Mark: {mark}")
            
    elif choice == '5':
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please try again.")