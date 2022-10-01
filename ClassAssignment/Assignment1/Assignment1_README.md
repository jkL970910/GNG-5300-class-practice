Assignment 1: A Student and Course Management Program designed via Python  

The basic assumptions of this project:  
- To login as a Admin, enter the name "Admin", we can not create any other admin  
- We assume that all the course & student name are unique, and case sensitive  
- We assume a course grade is between 0 - 100
- We assume that if a course is dropped by a student or a student is removed from a course list by the Admin, the previous submitted grade will be clear, the Admin will need to submit the grade again  

What this system can do:   
1: Login by entering the name of the user, "Admin" stands for the admin, others for student, if a name isn't existed, will ask to create a new student  

2: Admin functions:  
  - functions for Courses:  
    - check the whole course lists in the system  
    - create a new course, by entering the course name & course description, the system will generate a unique course number automatically  
    - update a course:  
      - update the course name & descritption  
      - update the enrolled student list of the course  
        - enroll a new student into the course, by entering the student name  
        - unenroll a existing student from the course, by entering the student name  
    - delete a course, by entering the course number  
  - functions for Students:  
    - check the whole student list in the system  
    - submit a course grade for a student, by entering the course number, the student name and the grade  
    - create a new student in the system, by entering a student name  
    - delete a student in the system, by entering the student name  

3: Student functions:
  - check the whole course lists in the system  
  - enroll a course, by entering the course number  
  - drop a course, by entering the course number
  - check a course grade, by entering the course number
