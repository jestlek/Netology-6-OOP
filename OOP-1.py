class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self._average_grade() < other._average_grade()

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\n'
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return result
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def _average_grade(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self._average_grade() < other._average_grade()

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
        f'Средняя оценка за лекции: {self._average_grade()}')
        return result

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

notbest_student = Student('Lok', 'Meme', 'male')
notbest_student.courses_in_progress += ['Python', 'Git']
notbest_student.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Lecturer', 'Buddy')
cool_lecturer.courses_attached += ['Python']

notcool_lecturer = Lecturer('Bok', 'Foko')
notcool_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Reviewer', 'Body')
cool_reviewer.courses_attached += ['Python']

notcool_reviewer = Reviewer('Reviewer', 'Tom')
notcool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 5)

cool_reviewer.rate_hw(notbest_student, 'Python', 9)
cool_reviewer.rate_hw(notbest_student, 'Python', 5)

best_student.rate_lec(cool_lecturer, 'Python', 10)
notbest_student.rate_lec(notcool_lecturer, 'Python', 7)

student_list = [best_student, notbest_student]
lecturer_list = [cool_lecturer, notcool_lecturer]


students_grades_list = []
def average_student_grade(student_list, course):
    '''This function print average grade of all students on course'''
    for student in student_list:
        for key, value in student.grades.items():
            if key is course:
                students_grades_list.extend(value)
    result = sum(students_grades_list) / len(students_grades_list)
    print(f'Средний бал по всем студентам курса {course}: {result}')


lecturer_grades_list = []
def average_lecturer_grade(lecturer_list, course):
    '''This function print average grade of all lecturer on course'''
    for lecturer in lecturer_list:
        for key, value in lecturer.grades.items():
            if key is course:
                lecturer_grades_list.extend(value)
    result = sum(lecturer_grades_list) / len(lecturer_grades_list)
    print(f'Средний бал по всем лекторам курса {course}: {result}')

average_student_grade(student_list, 'Python')
average_lecturer_grade(lecturer_list, 'Python')

print(cool_lecturer.grades)
print(notcool_lecturer.grades)
print(best_student.grades)
print(notbest_student.grades)
print(best_student > notbest_student)
print(cool_lecturer > notcool_lecturer)
print(best_student)
print(notbest_student)
print(cool_lecturer)
print(notcool_lecturer)
print(cool_reviewer)
print(notcool_reviewer)

