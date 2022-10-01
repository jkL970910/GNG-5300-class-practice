import random
# ==================================================================================
# assignment assumptions: 
# 1 - To login as a Admin, enter the name "Admin", we can not create any other admin
# 2 - We assume that all the course & student name are unique, and case sensitive
# ==================================================================================

# ==================================================================================
# Globle Variables
# ==================================================================================
# Courses map to store all the existing courses infromation
# key: course number, value: course object
course_list_map = {}
# Students list to store all the students information
student_list = []

# ==================================================================================
# Course Class
# ==================================================================================
class Course:
    def __init__(self, name, number, description):
        self.__name = name
        self.__number = number
        self.__description = description
        self.__enroll_student_list = []
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # the course number is generated automatically and unique to be unchanged
    def get_number(self):
        return self.__number

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_enroll_student_list(self):
        return self.__enroll_student_list

    def set_enroll_student_list(self, list):
        self.__enroll_student_list = list

# ==================================================================================
# User Class
# ==================================================================================
class User:
    def __init__(self, name):
        self.__name = name
        self.__role = "user"

    def get_name(self):
        return self.__name
    
    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role

# ==================================================================================
# Admin Class
# ==================================================================================
class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        super().set_role("Admin")

    # submit grade for a student by input the student name & course number
    def submit_grade(self):
        student_name = input("Enter the student name: ")
        student = check_student(student_name)
        if (student == -1):
            print("The Student Name didn't exist!")
            print("Submitted grade failed")
            return
        course_number = input("Enter the course number: ")
        if check_course_number(course_number) == -1:
            print("The Course Number didn't exist!")
            print("Submitted grade failed")
            return
        grade = input("Enter the grade of the student: ")
        student_list = student.get_enrolled_course_list()
        if (check_course_enroll(course_number, student_list)):
            student_list[course_number] = grade
            student.set_enrolled_course_list(student_list)
            print("Submit Grade Successfully!")
        else:
            print("Submit Grade Error: The student " + student_name + " didn't enroll in this course. Course Number: " + str(course_number))
    
    # create a new course into the system course list
    def create_course(self):
        course_name = input("Please Enter the Course Name: ")
        if (check_course_name(course_name)):
            print("Create Course Failed: The Course Name already existed!")
            return
        course_number = course_number_generator()
        course_description = input("Please Enter the Course Description: ")
        course_list_map[course_number] = Course(course_name, course_number, course_description)
        print("New Course Create Successfully")

    # update a course's name or description or enrolled student list
    def update_course(self, course_number):
        if check_course_number(course_number) == -1:
            print("The Course Number didn't exist!")
            return
        course = course_list_map[course_number]
        operation_case = input("Please choose your operation, 1 for update course name, 2 for update course description, 3 for update enrolled student list, others for exist: ")
        if operation_case == "1":
            course_name = input("Please Enter the new Course Name: ")
            if (check_course_name(course_name)):
                print("The Course Name is already existed!")
                self.update_course(course_number)
            else:
                course.set_name(course_name)
                print("Update Course Name Successful!")
        elif operation_case == "2":
            course_description = input("Please Enter the new Course Description: ")
            course.set_description(course_description)
            print("Update Course Description Successful!")
        elif operation_case == "3":
            self.update_course_student_list(course_number)
        else:
            print("Existed Successful.")
            return
    
    def update_course_student_list(self, course_number):
        course = course_list_map[course_number]
        check_enrolled_students(course.get_enroll_student_list())
        operation_case = input("Please choose your operation, 1 for enroll new student in this course, 2 for remove student from this course, others for exist: ")
        if operation_case == "1":
            student_name = input("Please Enter the Student Name: ")
            if check_student(student_name) == -1:
                print("Student didn't exist, enrolled Failed!")
            else:
                if check_student_in_course_list(student_name, course):
                    print("The Student is already enrolled this course")
                else:
                    update_student_list_and_course_list(student_name, course_number, "enroll")
        elif operation_case == "2":
            student_name = input("Please Enter the Student Name: ")
            if check_student(student_name) == -1:
                print("Student didn't exist, removed Failed!")
            else:
                if not check_student_in_course_list(student_name, course):
                    print("The Student is not enrolled this course")
                else:
                    update_student_list_and_course_list(student_name, course_number, "unenroll")
        else:
            print("Existed Successful.")
            return
    
    def delete_course(self, course_number):
        if check_course_number(course_number) == -1:
            print("The Course Number didn't exist!")
        else:
            del course_list_map[course_number]
            print("Deleted Course Successful!")

# ==================================================================================
# Student Class
# ==================================================================================
class Student(User):
    def __init__(self, name):
        super().__init__(name)
        super().set_role("Student")
        self.__enrolled_course_list = {} # key: course_number, value: course_grade, initial value as "No Grade"

    def get_enrolled_course_list(self):
        return self.__enrolled_course_list

    def set_enrolled_course_list(self, enrolled_course_list):
        self.__enrolled_course_list = enrolled_course_list

    def check_enrolled_course_list(self):
        print("Your current enrolled course list is: ")
        for course_number in self.__enrolled_course_list.keys():
            course = check_course_number(course_number)
            print("Course Number: " + str(course.get_number()) + " Course Name: " + course.get_name() + " Description: " + course.get_description())

    # enter the course number to check the course grade for a student
    def check_grade(self, enroll_course_number):
        if check_course_number(enroll_course_number) == -1:
            print("You have entered a wrong course number!")
        elif not check_student_in_course_list(super().get_name(), check_course_number(enroll_course_number)):
            print("You have not enrolled this course!")
        else:
            enrolled_course_list = self.get_enrolled_course_list()
            print("Your score for course " + enroll_course_number + " is: " + enrolled_course_list[enroll_course_number])
    
    # enroll a course into the student course list
    def enroll_course(self, student_name, enroll_course_number):
        if check_course_number(enroll_course_number) == -1:
            print("You have entered a wrong course number!")
        elif check_student_in_course_list(super().get_name(), check_course_number(enroll_course_number)):
            print("You have already enrolled this course!")
        else:
            update_student_list_and_course_list(student_name, enroll_course_number, "enroll")
            
    # remove a enrolled course from the student course list
    def remove_course(self, student_name, enroll_course_number):
        if check_course_number(enroll_course_number) == -1:
            print("You have entered a wrong course number!")
        elif not check_student_in_course_list(super().get_name(), check_course_number(enroll_course_number)):
            print("You have not enrolled this course!")
        else:
            update_student_list_and_course_list(student_name, enroll_course_number, "unenroll")

# ==================================================================================
# Global functions
# ==================================================================================
# check whether a student is already existed
def check_student(name):
    for student in student_list:
        if name == student.get_name():
            return student
    return -1

# print the whole list of current students 
def check_student_list():
    if len(student_list) == 0:
        print("Empty, no student in the system yet")
    else:
        print("The current student list is: ")
        for student in student_list:
            print("Student Name: " + student.get_name())

# print the enrolled course list of the current student
def check_enroll_course_list(enrolled_course_list):
    print("Your current enrolled course list is: ")
    if len(enrolled_course_list.keys()) == 0:
        print("Empty")
    else:
        for entry in enrolled_course_list.keys():
            course = check_course_number(entry)
            print("Course Number: " + str(course.get_number()) + " Course Name: " + course.get_name() + " Description: " + course.get_description())

# check whether the course number is already in the student's course list
def check_course_enroll(number, student_enroll_course_list):
    return number in student_enroll_course_list.keys()

# check whether a course number is already been used
def check_course_number(number):
    for course in course_list_map.values():
        if number == course.get_number():
            return course
    return -1

# check whether a course name is already been used
def check_course_name(name):
    for course in course_list_map.values():
        if name == course.get_name():
            return True
    return False

# check whether a student name is already in a course list
def check_student_in_course_list(name, course):
    return name in course.get_enroll_student_list()

# print the whole list of current courses 
def check_course_list():
    print("The current course list is: ")
    if len(course_list_map) == 0:
        print("Empty, no course available yet")
    else:
        for course in course_list_map.values():
            print("Course Number: " + str(course.get_number()) + " Course Name: " + course.get_name() + " Description: " + course.get_description())

# print the whole enrolled students list of current course
def check_enrolled_students(enroll_student_list):
    print("The current enrolled student list is: ")
    if len(enroll_student_list) == 0:
        print("Empty, no student enroll yet")
    else:
        for student in enroll_student_list:
            print("Student Name: " + student)

# generate a unique course number for each course
def course_number_generator():
    new_number = random.randint(0, 99)
    while(check_course_number(new_number) != -1):
        new_number = random.randint(0, 99)
    return str(new_number)

# update both the student list & course list
def update_student_list_and_course_list(student_name, enroll_course_number, case):
    if case == "enroll":
        # update the course list
        course = check_course_number(enroll_course_number)
        enroll_student_list = course.get_enroll_student_list()
        enroll_student_list.append(student_name)
        course.set_enroll_student_list(enroll_student_list)
        # update the student list
        student = check_student(student_name)
        enrolled_course_list = student.get_enrolled_course_list()
        enrolled_course_list[enroll_course_number] = "No Grade"
        student.set_enrolled_course_list(enrolled_course_list)
        print("Enrolled Successful")
    else:
        # update the course list
        course = check_course_number(enroll_course_number)
        enroll_student_list = course.get_enroll_student_list()
        enroll_student_list.remove(student_name)
        course.set_enroll_student_list(enroll_student_list)
        # update the student list
        student = check_student(student_name)
        enrolled_course_list = student.get_enrolled_course_list()
        del enrolled_course_list[enroll_course_number]
        student.set_enrolled_course_list(enrolled_course_list)
        print("Unenrolled Successful")

# ==================================================================================
# CourseManageSystem Class
# ==================================================================================
class CourseManageSystem:
    # create new student object into the system student list
    def create_new_student(self):
        new_name = input("Create a new student, enter your name: ")
        if check_student(new_name) != -1:
            print("The name is already existed, failed to create new student")
            return -1
        else:
            student_list.append(Student(new_name))
            print("Create Student Success")
            return check_student(new_name)

    # remove student object from the system student list
    def remove_student(self):
        remove_name = input("Enter the student name you want remove: ")
        if check_student(remove_name) == -1:
            print("The student name didn't exist")
            print("Failed to delete student")
        else:
            for student in student_list:
                if student.get_name() == remove_name:
                    student_list.remove(student)
            print("Remove Student Success")

    # set up the system, users can be logged in as Admin or Student
    def set_up(self):
        current_name = input("Welcome, Please enter your name: ")
        current_user = User("")
        if current_name == "Admin":
            current_user = Admin("Admin")
        else:
            current_user = check_student(current_name)
            if current_user == -1:
                operation_word = input("Didn't find the student name, enter y to create a new one: ")
                if operation_word == 'y':
                    current_user = self.create_new_student()
                    if current_user == -1:
                        return
        role = current_user.get_role()
        if role ==  "Admin":
            print("Signed in as an Admin")
            operation_number = "1"
            while (operation_number != "3"):
                operation_number = input("Please choose your operation, 1 for Course, 2 for Student, 3 for exist: ")
                if operation_number == "1":
                    course_operation_number = input("Please choose your operation, 1 for check current course list, 2 for create new course, 3 for update course, 4 for delete a course, others for exist: ")
                    if course_operation_number == "1":
                        check_course_list()
                    elif course_operation_number == "2":
                        current_user.create_course()
                    elif course_operation_number == "3": 
                        course_number = input("Please Enter the Course Number: ")
                        current_user.update_course(course_number)
                    elif course_operation_number == "4":
                        course_number = input("Please Enter the Course Number: ")
                        current_user.delete_course(course_number)
                    else:
                        print("Existed Successful.")
                elif operation_number == "2":
                    student_operation_number = input("Please choose your operation, 1 for check current student list, 2 for submit grade for student, 3 for create new student, 4 for remove student from the program, others for exist: ")
                    if student_operation_number == "1":
                        check_student_list()
                    elif student_operation_number == "2":
                        current_user.submit_grade()
                    elif student_operation_number == "3":
                        self.create_new_student()
                    elif student_operation_number == "4":
                        self.remove_student()
                    else:
                        print("Existed Successful.")
                elif operation_number == "3":
                    print("Existed Successful.")
                    return
                else:
                    print("You must enter numbers between 1 and 3.")
        else:
            print("Signed in as an Student, student name: " + current_user.get_name())
            operation_number = "1"
            while (operation_number != "5"):
                operation_number = input("Please choose your operation, 1 for check the course list, 2 for enroll a course, 3 for drop a Course, 4 for grade check, 5 for exist: ")
                if operation_number == "1":
                    check_course_list()
                elif operation_number == "2":
                    check_enroll_course_list(current_user.get_enrolled_course_list())
                    choose_course_number = input("Please entern the course number you want to enroll: ")
                    current_user.enroll_course(current_user.get_name(), choose_course_number)
                elif operation_number == "3":
                    check_enroll_course_list(current_user.get_enrolled_course_list())
                    choose_course_number = input("Please entern the course number you want to unenroll: ")
                    current_user.remove_course(current_user.get_name(), choose_course_number)
                elif operation_number == "4":
                    choose_course_number = input("Please entern the course number you want to check: ")
                    current_user.check_grade(choose_course_number)
                elif operation_number == "5":
                    print("Existed Successful.")
                    return
                else:
                    print("You must enter numbers between 1 and 4.")

# ==================================================================================
# System Init
# ==================================================================================
system = CourseManageSystem()
course_list_map["123"] = Course("Test", "123", "Test")
student_list.append(Student("Test"))
while(True):
    system.set_up()
