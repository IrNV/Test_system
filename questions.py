from sympy.geometry import *


class Question1:
    def __init__(self, question, right_answer):
        self.question = question
        self.right_answer = right_answer
        self.user_answer = ""
        self.result = 0

    def calc_question_mark(self):
        if self.get_user_answer() == self.get_right_answer():
            self.result += 1

        return self.result

    def get_right_answer(self):
        return self.right_answer

    def set_user_answer(self, user_answer):
        self.user_answer = user_answer

    def get_user_answer(self):
        return self.user_answer

    def get_question(self):
        return self.question


class Question2:
    def __init__(self, question, data):
        self.question = question
        self.data = data
        self.user_answer = ""
        self.result = 0

    def calc_question_mark(self):

        self.result += self.data[self.user_answer]

        return self.result

    def set_user_answer(self, user_answer):
        self.user_answer = user_answer

    def get_user_answer(self):
        return self.user_answer

    def get_question(self):
        return self.question


class Question3:
    def __init__(self, question, data):
        self.question = question
        self.data = data
        self.user_answer = ""
        self.result = 0

    def calc_question_mark(self):

        for answer in self.user_answer:
            self.result += self.data[answer]

        return self.result

    def set_user_answer(self, user_answer):
        self.user_answer = user_answer

    def get_question(self):
        return self.question


class Question4:
    def __init__(self, question, left_dot, right_dot):
        self.question = question
        self.left_dot = left_dot
        self.right_dot = right_dot
        self.user_answer = ""
        self.result = 0

    def calc_question_mark(self):
        left_dot = self.left_dot
        right_dot = self.right_dot
        if left_dot <= self.user_answer <= right_dot:
            self.result += 1 - abs(left_dot + right_dot - 2 * self.user_answer) \
                               / (right_dot - left_dot)

        return self.result

    def set_user_answer(self, user_answer):
        self.user_answer = user_answer

    def get_question(self):
        return self.question


class Question5:
    def __init__(self, question, left_dot, right_dot):
        self.question = question
        self.left_dot = left_dot
        self.right_dot = right_dot
        self.user_answer = ""
        self.result = 0

    def calc_question_mark(self):
        left_dot = self.left_dot()
        right_dot = self.right_dot()
        user_left_dot = self.user_left_dot()
        user_right_dot = self.user_right_dot()

        if left_dot == user_left_dot and right_dot == user_right_dot:
            self.result += 1
        elif left_dot <= user_left_dot <= user_right_dot <= right_dot:
            self.result += (user_right_dot - user_left_dot) / (right_dot - left_dot)
        elif left_dot <= user_left_dot <= right_dot <= user_right_dot:
            self.result += (right_dot - user_left_dot) / (right_dot - left_dot)
        elif user_left_dot <= left_dot <= user_right_dot <= right_dot:
            self.result += (user_right_dot - left_dot) / (right_dot - left_dot)
        elif user_left_dot <= left_dot <= right_dot <= user_right_dot:
            self.result += (right_dot - left_dot) / (user_right_dot - user_left_dot)
        else:
            self.result += -1

        return self.result

    def set_user_answer(self, user_left_dot, user_right_dot):
        self.user_left_dot = user_left_dot
        self.user_right_dot = user_right_dot

    def get_question(self):
        return self.question


class Question6:
    def __init__(self, question, mode, interval):
        self.question = question
        self.mode = mode
        self.interval = interval
        self.result = 0

    def calc_question_mark(self):
        question_mode = self.mode
        question_interval = self.interval
        user_mode = self.user_mode
        user_interval = self.user_interval

        if question_mode == user_mode:
            if question_interval >= user_interval:
                self.result += user_interval / question_interval
            else:
                self.result += question_interval / user_interval
        else:
            p1, p2, p3 = map(Point, [(question_mode - question_interval, 0),
                                     (question_mode, 1),
                                     (question_mode + question_interval, 0)])
            poly1 = Triangle(p1, p2, p3)

            p4, p5, p6 = map(Point, [(user_mode - user_interval, 0),
                                     (user_mode, 1),
                                     (user_mode + user_interval, 0)])
            poly2 = Triangle(p4, p5, p6)

            intersection = poly1.intersection(poly2)

            if len(intersection) == 2:
                self.result += Triangle(intersection[0],
                                        intersection[1].points[0],
                                        intersection[1].points[1]).area / (poly1.area + poly2.area)
            else:
                self.result += -1

        return self.result

    def set_user_answer(self, user_mode, user_interval):
        self.user_mode = user_mode
        self.user_interval = user_interval

    def get_question(self):
        return self.question


class Question7:
    def __init__(self, question, data):
        self.question = question
        self.data = data
        self.user_answer = ""
        self.result = 0

    def calc_question_mark(self):
        if self.user_answer in self.data:
            self.result += self.data[self.user_answer]
        else:
            self.result += -1

        return self.result

    def set_user_answer(self, user_answer):
        self.user_answer = user_answer

    def get_question(self):
        return self.question