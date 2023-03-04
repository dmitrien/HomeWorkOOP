class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avrg_grade(self):
        sum_g = 0
        len_g = 0
        for g in list(self.grades.values()):
            sum_g += sum(g)
            len_g += len(g)
            result = sum_g / len_g
        return round(result, 2)


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avrg_grade()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}




class Lecturer(Mentor):

    def avrg_grade(self):
        sum_g = 0
        len_g = 0
        for g in list(self.grades.values()):
            sum_g += sum(g)
            len_g += len(g)
            result = sum_g / len_g
        return round(result, 2)

    def __str__(self):

        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avrg_grade()}'
        return res

    def __lt__(self, student):
        if self.avrg_grade() == student.avrg_grade():
            return f"У лектора и студента одинаковый средний бал {self.avrg_grade()}"
        elif self.avrg_grade() < student.avrg_grade():
            return f"У студента средний бал {student.avrg_grade()} выше чем {self.avrg_grade()} у лектора"
        else:
            return f"У лектора средний бал {self.avrg_grade()} выше чем {student.avrg_grade()} у студента"


class Reviewer(Mentor):

    def _rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

best_student = Student('Ruoy', 'Eman', 'M')
best_student.courses_in_progress += ['Python', 'math', 'Russia']
best_student.finished_courses += ['Введение в программирование']

second_student = Student('Jamy', 'Person', 'W')
second_student.courses_in_progress += ['Python', 'math', 'English']
second_student.finished_courses += ['Введение в программирование']

student_list = [best_student, second_student]

cool_lec = Lecturer('Some', 'Buddy')
cool_lec.courses_attached += ['Python', 'math']

bad_lec = Lecturer('Doby', 'Elf')
bad_lec.courses_attached += ['Python', 'math']
lector_list = [cool_lec, bad_lec]

cool_rew = Reviewer('Some', 'Buddy')
cool_rew.courses_attached += ['Python', 'math']

bad_rew = Reviewer('Brain', 'Tipson')
bad_rew.courses_attached += ['English', 'Russia', 'math']

cool_rew._rate_hw(best_student, 'Python', 9)
cool_rew._rate_hw(best_student, 'math', 10)
cool_rew._rate_hw(best_student, 'math', 7)
cool_rew._rate_hw(second_student, 'Python', 6)
cool_rew._rate_hw(second_student, 'Python', 5)
cool_rew._rate_hw(second_student, 'math', 2)

best_student.rate_lecturer(cool_lec, 'Python', 9)
best_student.rate_lecturer(bad_lec, 'Python', 2)
second_student.rate_lecturer(bad_lec, 'math', 3)

second_student.rate_lecturer(cool_lec, 'math', 9)
second_student.rate_lecturer(bad_lec, 'math', 4)
second_student.rate_lecturer(bad_lec, 'Python', 5)

def grades_students(student_list, course):
    sum_grade = 0
    len_grade = 0
    for student in student_list:
        sum_grade += sum(student.grades.get(course))
        len_grade += len(student.grades.get(course))
    return f'Средняя оценка студентов за курс "{course}" составляет {round(sum_grade / len_grade, 2)}'

def grades_lectors(lector_list, course):
    sum_grade = 0
    len_grade = 0
    for lector in lector_list:
        sum_grade += sum(lector.grades.get(course))
        len_grade += len(lector.grades.get(course))
    return f'Средняя оценка всех лекторов за лукцию по "{course}" составляет {round(sum_grade / len_grade, 2)}'




print(cool_lec)
print(bad_lec)
print(best_student)
print(second_student)

print(grades_students(student_list, 'Python'))
print(grades_lectors(lector_list, 'math'))


