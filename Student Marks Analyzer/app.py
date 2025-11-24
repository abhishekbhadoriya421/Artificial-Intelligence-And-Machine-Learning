from Students import Students
from Marks import Marks
from  Analyzer import Analyzer
import random

def main():
    student_list = []
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
            student_list.append(studentObject)
        except Exception as e:
            print(f"An error occurred: {e}")

    # Display all student details
    for student in student_list:
        details = student.get_details()
        marks = student.get_student_marks()
        print(f"{details}, Marks: Hindi={marks.hindi}, English={marks.english}, Maths={marks.maths}, Science={marks.science}, Social={marks.social}")
    
    while True:
        try:
            analyzer = Analyzer(student_list)
            choice = int(input("Choose an option:\n1. Total Students\n2. Maximum Scorer\n3. Minimum Scorer\n4. Average Marks\n5. Exit\n"))
            match choice:
                case 1:
                    print(f"Total Students: {analyzer.get_total_students()}")
                case 2:
                    max_scorer_id = analyzer.get_maximum_scorer()
                    for student in student_list:
                        if student.student_id == max_scorer_id:
                            print(f"Maximum Scorer: {student.get_details()}")
                            details = student.get_details()
                            marks = student.get_student_marks()
                            print(f"Marks: Hindi={marks.hindi}, English={marks.english}, Maths={marks.maths}, Science={marks.science}, Social={marks.social} \nTotal={marks.get_total()}")
                            break
                case 3:
                    min_scorer_id = analyzer.get_minimum_scorer()
                    for student in student_list:
                        if student.student_id == min_scorer_id:
                            print(f"Minimum Scorer: {student.get_details()}")
                            details = student.get_details()
                            marks = student.get_student_marks()
                            print(f"Marks: Hindi={marks.hindi}, English={marks.english}, Maths={marks.maths}, Science={marks.science}, Social={marks.social} \nTotal={marks.get_total()}")
                            break
                case 4:
                    print(f"Average Marks: {analyzer.get_average_marks()}")
        except Exception as e:
            print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()