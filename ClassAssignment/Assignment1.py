import random

# Courses map to store all the existing courses infromation
# key: course number, value: Course object
course_list_map = {}
# Students list to store all the students information
student_list = []

# Global functions
# check whether a student is already existed
def check_student(name):
    for student in student_list:
        if name == student.get_name():
            return student
    print("The Student Didn't Existed!")
    return -1

# check whether the course number is already in the student's course list
def check_course_enroll(number, student_enroll_course_list):
    return number in student_enroll_course_list.keys()

# check whether a course number is already been used
def check_course_number(number):
    return number in course_list_map.keys()

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
    for course in course_list_map.values():
        print("Course Number: " + str(course.get_number()) + " Course Name: " + course.get_name() + " Description: " + course.get_description())

# print the whole enrolled students list of current course
def check_enrolled_students(enroll_student_list):
    print("The current enrolled student list is: ")
    for student in enroll_student_list:
        print("Student Name: " + student)

# generate a unique course number for each course
def course_number_generator():
    new_number = random.randint(0, 99)
    while(check_course_number(new_number)):
        new_number = random.randint(0, 99)
    return str(new_number)

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

class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        super().set_role("Admin")

    def submit_grade(self, student_name, course_number, grade):
        student = check_student(student_name)
        if (student == -1):
            print("The Student Name doesn't exist!")
            return
        student_list = student.get_enrolled_course_list()
        if (check_course_enroll(course_number, student_list)):
            student_list[course_number] = grade
            student.set_course_list(student_list)
            print("Submit Grade Successfully!")
        else:
            print("Submit Grade Error: The student " + student_name + " didn't enroll in this course. Course Number: " + str(course_number))
    
    def create_course(self):
        course_name = input("Please Enter the Course Name: ")
        if (check_course_name(course_name)):
            print("Create Course Failed: The Course Name already existed!")
            return
        course_number = course_number_generator()
        course_description = input("Please Enter the Course Description: ")
        course_list_map[course_number] = Course(course_name, course_number, course_description)
        print("New Course Create Successfully")

    def update_course(self, course_number):
        if not check_course_number(course_number):
            print("The Course Number didn't existed!")
            return
        course = course_list_map[course_number]
        operation_case = int(input("Please choose your operation, 1 for update course name, 2 for update course description, 3 for update enrolled student list, others for exist: "))
        match operation_case:
            case 1:
                course_name = input("Please Enter the new Course Name: ")
                if (check_course_name(course_name)):
                    print("The Course Name is already existed!")
                    self.update_course(course_number)
                else:
                    course.set_name(course_name)
                    print("Update Course Name Successful!")
            case 2:
                course_description = input("Please Enter the new Course Description: ")
                course.set_description(course_description)
                print("Update Course Description Successful!")
            case 3:
                self.update_course_student_list(course_number)
            case _:
                print("Existed Successful.")
                return
    
    def update_course_student_list(self, course_number):
        course = course_list_map[course_number]
        check_enrolled_students(course.get_enroll_student_list())
        operation_case = int(input("Please choose your operation, 1 for enroll new student in this course, 2 for remove student from this course, others for exist: "))
        match operation_case:
            case 1:
                student_name = input("Please Enter the Student Name: ")
                if check_student(student_name) == -1:
                    print("Enrolled Failed!")
                else:
                    if check_student_in_course_list(student_name, course):
                        print("The Student is already enrolled this course")
                    else:
                        enrolled_list = course.get_enroll_student_list()
                        enrolled_list.append(student_name)
                        course.set_enroll_student_list(enrolled_list)
                        print("Enrolled Successful!")
            case 2:
                student_name = input("Please Enter the Student Name: ")
                if check_student(student_name) == -1:
                    print("Removed Failed!")
                else:
                    if not check_student_in_course_list(student_name, course):
                        print("The Student is not enrolled this course")
                    else:
                        enrolled_list = course.get_enroll_student_list()
                        enrolled_list.remove(student_name)
                        course.set_enroll_student_list(enrolled_list)
                        print("Removed Successful!")
            case _:
                print("Existed Successful.")
                return
    
    def delete_course(self, course_number):
        if not check_course_number(course_number):
            print("The Course Number didn't existed!")
        else:
            del course_list_map[course_number]
            print("Deleted Course Successful!")

class Student(User):
    def __init__(self, name):
        super().__init__(name)
        super().set_role("Student")
        self.__enrolled_course_map = {}

    def get_enrolled_course_list(self):
        return self.__enrolled_course_map

    def set_enrolled_course_list(self, enrolled_course_map):
        self.__enrolled_course_map = enrolled_course_map

class CourseManageSystem:
    def create_new_student(self):
        new_name = input("Create a new student, enter your name: ")
        if check_student(new_name) != -1:
            print("The name is already existed")
            print("Failed to create new student")
            return False
        else:
            student_list.append(Student(new_name))
            print("Create Student Success")
            return True

    def set_up(self):
        current_name = input("Welcome, Please enter your name: ")
        current_user = User("")
        if current_name == "Admin":
            current_user = Admin("Admin")
        else:
            if check_student(current_name) == -1:
                print("Didn't find the student name, will create a new one")
                while(check_student(current_name) == -1):
                    self.create_new_student()
            current_user = check_student(current_name)
        
        role = current_user.get_role()
        if role ==  "Admin":
            print("Signed in as an Admin")
            operation_number = 1
            while (operation_number != 3):
                operation_number = int(input("Please choose your operation, 1 for Course, 2 for Student, 3 for exist: "))
                if operation_number == 1:
                    course_operation_number = int(input("Please choose your operation, 1 for check current course list, 2 for create new course, 3 for update course, 4 for delete a course, others for exist: "))
                    match course_operation_number:
                        case 1:
                            check_course_list()
                        case 2:
                            current_user.create_course()
                        case 3: 
                            course_number = input("Please Enter the Course Number: ")
                            current_user.update_course(course_number)
                        case 4:
                            course_number = input("Please Enter the Course Number: ")
                            current_user.delete_course(course_number)
                        case _:
                            print("Existed Successful.")
                            return
                elif operation_number == 2:
                    print("Operation for Student is coming soon")
                elif operation_number == 3:
                    print("Existed Successful.")
                    return
                else:
                    print("You must enter numbers between 1 and 3.")
# ==========================================================================
system = CourseManageSystem()
course_list_map["123"] = Course("Test", "123", "Test")
student_list.append(Student("Test"))
while(True):
    system.set_up()
