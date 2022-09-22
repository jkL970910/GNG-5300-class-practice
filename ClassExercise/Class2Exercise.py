class_grade_list_map = []

class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def get_name(self):
        return self.__name

    def set_grade(self, grade):
        self.__grade = grade

class GradeSystem:
    def check_student(self, name):
        for student in class_grade_list_map:
            if name == student.get_name():
                return student
        return -1

    def create_new_student(self):
        new_name = input("Create a new student, enter your name: ")
        if self.check_student(new_name) != -1:
            print("The name is already existed")
            print("Failed to create new student")
            return False
        else:
            new_grade = int(input("Enter your grade: "))
            class_grade_list_map.append(Student(new_name, new_grade))
            print("Create Student Success")
            return True

    def check_grade(self, current_student):
        print("Your grade is: " + str(current_student.get_grade()))

    def update_grade(self, current_student):
        print("Your current grade is: " + str(current_student.get_grade()))
        new_grade = int(input("Please enter a new grade: "))
        if new_grade < 1 or new_grade > 100:
            print("Update failed, please enter a valid grade between 1 and 100")
            self.update_grade(current_student)
        else:
            current_student.set_grade(new_grade)
            print("Update Grade Success")

    def delete_grade(self, current_student):
        class_grade_list_map.remove(current_student)
        print("Delete Successful")

    def set_up(self):
        current_name = input("Please enter your name: ")
        if self.check_student(current_name) == -1:
            print("Didn't find the student name, will create a new one")
            self.create_new_student()
        else:
            current_student = self.check_student(current_name)
            operation_number = int(input("Please choose your operation, 1 for check grade, 2 for update grade, 3 for delete grade: "))
            match operation_number:
                case 1:
                    self.check_grade(current_student)
                case 2:
                    self.update_grade(current_student)
                case 3:
                    self.delete_grade(current_student)
                case _:
                    print("Please enter number between 1 and 3")

system = GradeSystem()
class_grade_list_map.append(Student("test", 90))
while(True):
    system.set_up()