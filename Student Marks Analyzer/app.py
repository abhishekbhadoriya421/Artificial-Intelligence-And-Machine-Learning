from Students import Students
from Marks import Marks
import random

def main():
    student_tupels = []
    while True:
        try:
            student_name = input("Enter student name (or type 'exit' to quit): ")
            student_id = random.randint(1000, 9999) 
            if(student_name.lower() == 'exit'):
                break
            hindi = float(input("Enter marks in Hindi: "))
            english = float(input("Enter marks in English: "))
            maths = float(input("Enter marks in Maths: "))
            science = float(input("Enter marks in Science: "))
            social = float(input("Enter marks in Social Studies: "))
            marksObject = Marks(hindi, english, maths, science, social)
            studentObject = Students(student_name, student_id, marksObject)
            student_tupels.append(studentObject)
        except Exception as e:
            print(f"An error occurred: {e}")

    # Display all student details
    for student in student_tupels:
        details = student.get_details()
        marks = student.get_student_marks()
        print(f"{details}, Marks: Hindi={marks.hindi}, English={marks.english}, Maths={marks.maths}, Science={marks.science}, Social={marks.social}")
    
if __name__ == "__main__":
    main()