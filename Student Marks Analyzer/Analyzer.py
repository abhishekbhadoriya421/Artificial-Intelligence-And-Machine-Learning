class Analyzer:
    studentCount = 0
    def __init__(self,students: list):
        self.students = students
        self.studentCount = len(students)
        
    def get_total_students(self):
        return self.studentCount
    
    def get_maximum_scorer(self):
        max_scorer_id = None
        max_marks = -1
        for student in self.students:
            marksObject = student.get_student_marks()
            maximum_marks = marksObject.get_total()
            if(maximum_marks > max_marks):
                max_marks = maximum_marks
                max_scorer_id = student.student_id
        return max_scorer_id
    
    def get_minimum_scorer(self):
        min_scorer_id = None
        min_marks = float('inf')
        for student in self.students:
            marksObject = student.get_student_marks()
            minimum_marks = marksObject.get_total()
            if(minimum_marks < min_marks):
                min_marks = minimum_marks
                min_scorer_id = student.student_id
        return min_scorer_id
    
    def get_average_marks(self):
        total_marks = 0
        for student in self.students:
            marksObject = student.get_student_marks()
            total_marks += marksObject.get_total()
        if self.studentCount == 0:
            return 0
        average_marks = total_marks / self.studentCount
        return average_marks