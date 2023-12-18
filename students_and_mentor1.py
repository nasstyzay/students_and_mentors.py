class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_Lecturer(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average(self):
        result = 0

        if self.grades:
            for grade in self.grades.values():
                result += sum(grade) / len(grade)
            return result / len(self.grades)
        else:
            return 0
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задание: {self.average()}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}\n')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average(self):
        return sum(self.grades) // len(self.grades)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\n Средняя оценка за лекции {self.average}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        print(student.grades, course, grade)
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            print(student.grades)
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print("ошибка")
            return 'Ошибка'


student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Web']
student1.finished_courses += ['Введение в программирование']
student1.finished_courses += ['Git']

student2 = Student('Pit', 'Aman', 'male')
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Введение в программирование']

lector1 = Lecturer('Samy', 'Bobby')
lector1.courses_attached += ['Python']

lector2 = Lecturer('Mary', 'Jane')
lector2.courses_attached += ['Git']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']
reviewer1.courses_attached += ['Web']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Web', 8)
student1.rate_Lecturer(lector1, 'Python', 10)
student2.rate_Lecturer(lector2, 'Git', 9)

print(student1)
print()
print(student2)
print()
print(lector1)
print()
print(lector2)