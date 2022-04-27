from Student_class import Student

student1 = Student("Yucel", 2.5, "Hoca" )
student2 = Student("Mustafa", 3.5, "Amele")
student3 = Student ("Akin", 1, "Mazlum")

print(student3.name)
print(student2.university)
student2.update_gpa(5)
print(student2.major)
student2.update_major("Hafiz")
print(student2.major)