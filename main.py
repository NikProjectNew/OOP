class Student:
    LST = []

    def __init__(self, name, surname, gender):
        Student.LST.append(self)
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.grades[course] = lecturer.grades.get(course, []) + [grade]
        else:
            return 'Ошибка'

    def average(self):
        s = sum([v for v in self.grades.values()], [])
        return sum(s) / len(s)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n\
Средняя оценка за домашние задания: {self.average():.1f}\n\
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n\
Завершенные курсы: Введение в программирование'

    def __lt__(self, other):
        return self.average() < other.average()

class Mentor:
    LST = []

    def __init__(self, name, surname):
        Mentor.LST.append(self)
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average(self):
        s = sum([v for v in self.grades.values()], [])
        return sum(s) / len(s)

    def __lt__(self, other):
        return self.average() < other.average()

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average():.1f}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 5)
some_reviewer.rate_hw(some_student, 'Python', 7)

some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 10)


print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)
print()
print(some_lecturer.average() > some_student.average())