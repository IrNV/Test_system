from tkinter import *
from questions import *
from views import *
import csv
import codecs


class Test:
    def __init__(self, root):
        self.questions = []
        self.questions_views = []
        self.current_question = 0
        self.root = root

    def start(self):
        self.questions_views[self.current_question].show()

        button = Button(self.root, text="Підтвердити відповідь", font='arial 14')
        button.bind("<Button>", self.answer)

        button.pack()

    def calc_result(self):
        return sum([question.calc_question_mark() for question in self.questions])

    def result(self):
        Label(self.root, text="Ваш результат: {}".format(self.calc_result())).pack()

    def answer(self, event):
        self.questions_views[self.current_question].answer()

        if self.current_question < len(self.questions) - 1:
            self.current_question += 1

            for widget in self.root.winfo_children():
                widget.destroy()

            self.start()
        else:
            for widget in self.root.winfo_children():
                widget.destroy()

            self.result()

    def load_questions(self):
        # self.load_questions1()
        # self.load_questions2()
        # self.load_questions3()
        # self.load_questions4()
        # self.load_questions5()
        # self.load_questions6()
        self.load_questions7()

    def load_questions1(self):
        with codecs.open("questions1.csv", "r", encoding='utf-8') as file_obj:
            reader = csv.reader(file_obj, delimiter=';')
            next(reader, None)
            for raw in reader:
                question = Question1(raw[0], raw[1])
                self.questions.append(question)
                self.questions_views.append(Question1View(question, self.root))

    def load_questions2(self):
        with codecs.open("questions2.csv", "r", encoding='utf-8') as file_obj:
            reader = csv.reader(file_obj, delimiter=';')
            next(reader, None)
            for raw in reader:
                keys = raw[1].split(",")
                marks = list(map(float, raw[2].split(",")))
                data = dict(zip(keys, marks))
                question = Question2(raw[0], data)
                self.questions.append(question)
                self.questions_views.append(Question2View(question, self.root))

    def load_questions3(self):
        with codecs.open("questions3.csv", "r", encoding='utf-8') as file_obj:
            reader = csv.reader(file_obj, delimiter=';')
            next(reader, None)
            for raw in reader:
                keys = raw[1].split(",")
                marks = list(map(float, raw[2].split(",")))
                data = dict(zip(keys, marks))
                question = Question3(raw[0], data)
                self.questions.append(question)
                self.questions_views.append(Question3View(question, self.root))

    def load_questions4(self):
        with codecs.open("questions4.csv", "r", encoding='utf-8') as file_obj:
            reader = csv.reader(file_obj, delimiter=';')
            next(reader, None)
            for raw in reader:
                question = Question4(raw[0], float(raw[1]), float(raw[2]))
                self.questions.append(question)
                self.questions_views.append(Question4View(question, self.root))

    def load_questions5(self):
        with codecs.open("questions5.csv", "r", encoding='utf-8') as file_obj:
            reader = csv.reader(file_obj, delimiter=';')
            next(reader, None)
            for raw in reader:
                question = Question5(raw[0], float(raw[1]), float(raw[2]))
                self.questions.append(question)
                self.questions_views.append(Question5View(question, self.root))

    def load_questions6(self):
        with codecs.open("questions6.csv", "r", encoding='utf-8') as file_obj:
            reader = csv.reader(file_obj, delimiter=';')
            next(reader, None)
            for raw in reader:
                question = Question6(raw[0], float(raw[1]), float(raw[2]))
                self.questions.append(question)
                self.questions_views.append(Question6View(question, self.root))

    def load_questions7(self):
        with codecs.open("questions7.csv", "r", encoding='utf-8') as file_obj:
            reader = csv.reader(file_obj, delimiter=';')
            next(reader, None)
            for raw in reader:
                keys = raw[1].split(",")
                marks = list(map(float, raw[2].split(",")))
                data = dict(zip(keys, marks))
                question = Question7(raw[0], data)
                self.questions.append(question)
                self.questions_views.append(Question7View(question, self.root))


def main():
    root = Tk()
    root.geometry("300x300")

    test = Test(root)
    test.load_questions()
    test.start()

    root.mainloop()

if __name__ == '__main__':
    main()
