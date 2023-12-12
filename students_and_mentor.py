
class Student:
    def __init__(self, name, surname, gender):
        self.finished = None
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def add_courses(self, course_name):
        self.finished_courses.append = 'SqL', 'Python'


def __str__(self,student):
  return print(f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {aver_stud(student)}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}")

def aver_stud(student):
    count = 0
    countlen = 0
    for value in student.grades.values():
        countlen +=len(value)
        for item in value:
            count += item
class Mentor:
    def __init__(self, name: object, surname: object) -> object:
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name: object, surname: object) -> object:
        super().__init__:(Lecturer, name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __init__(self, name: object, surname: object) -> object:
        super().__init__:(Reviewer, name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

    lecturer1 = Lecturer("Ivan", "Petrov")
    lecturer2 = Lecturer("Fedor", "Ivanov")
    student1 = Student("Ivan", "Petrov", "male")
    student1.__str__()
    print(aver_stud(student1))
    student1.finished = Student
    student1.finished_courses =[courses == "Sql", "Python"]

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)