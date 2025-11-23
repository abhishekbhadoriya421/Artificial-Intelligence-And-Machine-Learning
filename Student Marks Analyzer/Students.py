from Marks import Marks
class Students:
    unique_student_ids = set()
    def __init__(self,name:str,student_id:int,marks:Marks):
        if not isinstance(marks, Marks):
            raise TypeError("marks must be an instance of Marks class")
        if student_id in Students.unique_student_ids:
            raise ValueError(f"Student ID {student_id} already exists.")
        Students.unique_student_ids.add(student_id)
        
        self.name = name
        self.student_id = student_id
        self.marks = marks
    
    def get_details(self):
        return f"Name: {self.name}, ID: {self.student_id}"
    def get_student_name(self):
        return self.name
    
    def get_student_marks(self):
        return self.marks
    
    @staticmethod
    def show_all_ids():
        return Students.unique_student_ids
