from tkinter import *
from questions import *
from views import *
from sympy import *
from sympy.geometry import *


def calc_question1_mark(questions1):
    result = 0

    for question in questions1:
        if question.get_user_answer() == question.get_right_answer():
            result += 1

    return result


def calc_question2_mark(questions2):
    result = 0

    for question in questions2:
        result += question.data[question.get_user_answer()]

    return result


def calc_question3_mark(questions3):
    result = 0

    for question in questions3:
        for answer in question.get_user_answer():
            result += question.data[answer]

    return result


def calc_question4_mark(questions4):
    result = 0

    for question in questions4:
        left_dot = question.get_left_dot()
        right_dot = question.get_right_dot()
        if left_dot <= question.get_user_answer() <= right_dot:
            result += 1 - abs(left_dot + right_dot - 2 * question.get_user_answer()) / (right_dot - left_dot)

    return result


def calc_question5_mark(questions5):
    result = 0

    for question in questions5:
        left_dot = question.get_left_dot()
        right_dot = question.get_right_dot()
        user_left_dot = question.get_user_left_dot()
        user_right_dot = question.get_user_right_dot()

        if left_dot == user_left_dot and right_dot == user_right_dot:
            result += 1
        elif left_dot <= user_left_dot <= user_right_dot <= right_dot:
            result += (user_right_dot - user_left_dot) / (right_dot - left_dot)
        elif left_dot <= user_left_dot <= right_dot <= user_right_dot:
            result += (right_dot - user_left_dot) / (right_dot - left_dot)
        elif user_left_dot <= left_dot <= user_right_dot <= right_dot:
            result += (user_right_dot - left_dot) / (right_dot - left_dot)
        elif user_left_dot <= left_dot <= right_dot <= user_right_dot:
            result += (right_dot - left_dot) / (user_right_dot - user_left_dot)
        else:
            result += -1

    return result


def calc_question6_mark(questions6):
    result = 0

    for question in questions6:
        question_mode = question.get_mode()
        question_interval = question.get_interval()
        user_mode = question.get_user_mode()
        user_interval = question.get_user_interval()

        if question_mode == user_mode:
            if question_interval >= user_interval:
                result += user_interval / question_interval
            else:
                result += question_interval / user_interval
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
            print(intersection)
            if len(intersection) == 2:
                    result += Triangle(intersection[0],
                                       intersection[1].points[0],
                                       intersection[1].points[1]).area / (poly1.area + poly2.area)
            else:
                result += -1

    return result


def calc_question7_mark(questions7):
    result = 0

    for question in questions7:
        if question.get_user_answer() in question.data:
            result += question.data[question.get_user_answer()]
        else:
            result += -1

    return result


def main():
    q1 = Question7("write pi", {"1": 1, "2": 2})

    root = Tk()
    view = Question7View(q1, root)
    view.show()
    root.mainloop()

    print(calc_question7_mark([q1]))
if __name__ == '__main__':
    main()
