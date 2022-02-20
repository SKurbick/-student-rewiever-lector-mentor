class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        arithmetic_mean_grades = []
        for grades in self.grades.values():
            for grade in grades:
                arithmetic_mean_grades.append(grade)

        return (f'Имя:{self.name}\n'
                f'Фамилия:{self.surname}\n'
                f'Средняя оценка за домашнюю работу:{sum(arithmetic_mean_grades) / len(arithmetic_mean_grades)}\n'
                f'Курсы в процессе изучения:{" ".join(self.courses_in_progress)}\n'
                f'Завершённые курсы:{" ".join(self.finished_courses)}\n')


#######################################################################################################################
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


########################################################################################################################
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
        return (f'Имя:{self.name}\n'
                f'Фамилия:{self.surname}\n')


########################################################################################################################
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def arithmetic_mean(self):
        all_grades = []
        for grades in self.grades.values():
            for grade in grades:
                all_grades.append(grade)
        arithmetic_mean_grades = (sum(all_grades) / len(all_grades))
        return arithmetic_mean_grades

    def __str__(self):
        all_grades = []
        for grades in self.grades.values():
            for grade in grades:
                all_grades.append(grade)
        arithmetic_mean_grades = (sum(all_grades) / len(all_grades))
        return (f'Имя:{self.name}\n'
                f'Фамилия:{self.surname}\n'
                f'Средняя оценка за домашнюю работу:{arithmetic_mean_grades}\n')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return print('не корректное сравнение')
        else:
            return self.arithmetic_mean() < other.arithmetic_mean()


# одна функция справляется как со студентами так и с лекторами(если конечно я правильно понял задание)
def rate_average_grade(persons, course):
    all_grades = []
    for person in persons:
        for grades in person.grades.items():
            if grades[0] == course:
                for grade in grades[1]:
                    print(grade)
                    all_grades.append(grade)

    return f'средняя оценка по курсу {course}: {sum(all_grades) / len(all_grades)}'


some_student = Student('Roy', 'Eman', 'your_gender')
some_student2 = Student('Jon', 'Jones', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer2 = Reviewer('Every', 'Buddy')

some_reviewer.courses_attached += ['Python']
some_reviewer2.courses_attached += ['Python']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer2 = Lecturer('Some2', 'Buddy2')

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer2.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student2, 'Python', 8)
some_reviewer2.rate_hw(some_student2, 'Python', 7)
some_student.rate_hw(some_lecturer, 'Python', 6)
some_student2.rate_hw(some_lecturer2, 'Python', 5)

students = [some_student, some_student2]
lectures = [some_lecturer, some_lecturer2]

print(some_student.grades)
print(some_student)
print(some_reviewer)
print(some_lecturer)
print(some_lecturer < some_lecturer2)
print(some_lecturer.arithmetic_mean())
print(some_lecturer2.arithmetic_mean())

print(rate_average_grade(students, 'Python'))
print(rate_average_grade(lectures, 'Python'))
