from class_definitions import Person as p
from class_definitions import Student as s

person1 = p('Horvath', 'Jessie', '123 Cherry Ln')
# print(person1.display())

student1 = s(person1, 'Biology', 'January 1, 2022', 4.00)
print(student1.display())

student1.change_major("Being Awesome!")
student1.update_gpa(3.0)
print(student1.display())