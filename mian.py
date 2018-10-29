from tkinter import *
from questions import *
from views import *


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
        user_left_dot = question.get_user_answer()[0]
        user_right_dot = question.get_user_answer()[1]

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


def main():
    q1 = Question5("write pi", [1, 3])

    root = Tk()
    view = Question5View(q1, root)
    view.show()
    root.mainloop()

    print(calc_question5_mark([q1]))
if __name__ == '__main__':
    main()
