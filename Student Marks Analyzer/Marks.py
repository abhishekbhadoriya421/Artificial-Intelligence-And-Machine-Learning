class Marks:
    def __init__(self,hindi,english,maths,science,social):
        self.hindi = hindi
        self.english = english
        self.maths = maths
        self.science = science
        self.social = social
    
    def get_total(self):
        return self.hindi + self.english + self.maths + self.science + self.social