
from validate import validate_student_data


class Student:

    def __init__(self, name, level, id):
        if validate_student_data(name, level, id):
            self.id = id
            self.name = name
            self.level = level
            self.exercises = []
            self.submitted = []
            self.av_score = None

    def do_exercise(self, subject, answer):
        if len(self.exercises) == 0:
            return False
        for exercise in self.exercises:
            if exercise.subject == subject:
                for question in exercise.questions:
                    if question.subject == subject:
                        question.answer_me(answer)
                        question.submitted = True
                        return question.answer
        return False


class Teacher:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.exercises = []
        self.students = []

    def add_quize(self, quize):
        if quize:
            self.exercises.append(quize)

    def add_my_student(self, student):
        self.students.append(student)
        return self.students

    def add_exercise_to_student(self, student, exercise):
        if exercise in self.exercises and student in self.students:
            student.exercises.append(exercise)
            return student.exercises
        else:
            return False
  
    def grade_student(self, student, subject):
        if student in self.students:
            for exercise in student.exercises:
                if exercise.subject == subject:
                    for question in exercise.questions:
                        total_score = 0
                        count = 0
                        if question.submitted is True:
                            count += 1
                            if question.score == 1:
                                total_score += 1
                            elif question.score == 0:
                                total_score = 0
                        av_score = total_score/count
                        student.av_score = av_score
                        return student.av_score
    

class Question:
    def __init__(self, value, answer, subject):
        self.value = value
        self.choices = []
        self.subject = subject
        self.answer = answer
        self.submitted = False
        self.score = 0

    def add_choices(self, choices):
        if len(choices) > 4:
            return False
        for choice in choices:
            self.choices.append(choice)
        return True

    def answer_me(self, answer):
        if answer in self.choices and answer == self.answer:
            self.score = 1
            return True
        else:
            self.answer = answer

    def submit(self):
        self.submitted = True


class Subject:

    def __init__(self):
        self.subject = None
        self.questions = []

    def add_subject(self, subject):
        if self.subject == subject:
            return False
        self.subject = subject
        return self

    def add_question(self, question):
        if question.subject == self.subject:
            self.questions.append(question)
            return True
        return False


# question1 = "What is 1 + 1"
# choices = [1, 3, 2, 4]
# question2 = "What is the symbol of oxygen"
# choices1 = ["CO2", "H20", "02", "C"]
# student = Student('nakatude', 1)
# # print(student.level)
# quize1 = Quize('Math')
# quize2 = Quize('Chem')
# quest = Question(question1)
# quest.add_choices(choices)
# print(quest.choices)
# quest2 = Question(question2)
# quest2.add_choices(choices1)
# quize1.add_question(quest)
# quize2.add_question(quest2)
# T = Teacher('james', 1)
# T.add_quize(quize1)
# T.add_quize(quize2)
# T.add_my_student(student)
# T.assign_quize(student, quize1)

# for q in student.exercises:
#     for j in q.questions:
#         answer = input(j.question + " > ")
#         j.answer_me(answer)
#         print(j.answer)