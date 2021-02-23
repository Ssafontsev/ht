class PersonWithGrades:
    def __init__(self):
        self.grades = {}

    def get_average_grades(self):
        grades_all = []
        for grades in self.grades.values():
            grades_all += grades
        grades_average = sum(grades_all) / len(grades_all)
        return round(grades_average, 1)

    # def rate(self, person, course, grade):
    #     pass


class Student(PersonWithGrades):
    def __init__(self, name, surname, gender):
        super().__init__()
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return 'Имя: {} \nФамилия: {} \nСредняя оценка за домашние задания: {} \nКурсы в процессе изучения: {} ' \
               '\nЗавершенные курсы: {}'.format(self.name, self.surname, self.get_average_grades(), ', '
                                                                                                    ''.join(
            self.courses_in_progress), ', '.join(self.finished_courses))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor, PersonWithGrades):
    def __init__(self, name, surname):
        PersonWithGrades.__init__(self)
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.med_grades = {}

    def __str__(self):
        return 'Имя: {} \nФамилия: {} \nСредняя оценка за лекции: {}'.format(self.name, self.surname, self.
                                                                             get_average_grades())


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


some_student = Student('Ruoy', 'Eman', 'male')
some_student.courses_in_progress += ['Git']
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['FrontEND']
some_student.finished_courses += ['C++']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_student.rate_lc(some_lecturer, 'Python', 10)
some_student.rate_lc(some_lecturer, 'Python', 7)
some_student.rate_lc(some_lecturer, 'Python', 8)

some_reviewer = Reviewer('Sam', 'Brown')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 7)

print(some_student.grades)
print()
# print(some_lecturer.courses_attached)
print(some_lecturer.grades)

print(some_lecturer)
print()
print(some_student)
# print(some_student.get_average_grades())
