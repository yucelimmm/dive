class Student:
    university = "yorukler universitesi"
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major
        self.current_course=[]

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa


        
    def update_major(self, new_major):
        self.major = new_major
