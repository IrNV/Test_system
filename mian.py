from tkinter import *
from questions import *
from views import *


class Test:
    def __init__(self, root):
        self.questions6 = [
            Question6("write pi", 2, 1)]
        self.current_question = 0
        self.root = root
        self.questions6_views = [Question6View(self.questions6[0], self.root)]

    def start(self):
        self.questions6_views[self.current_question].show()

        button = Button(self.root, text="Підтвердити відповідь", font='arial 14')
        button.bind("<Button>", self.answer)

        button.pack()

    def calc_result(self):
        return sum([question.calc_question_mark() for question in self.questions6])

    def result(self):
        Label(self.root, text="Ваш результат: {}".format(self.calc_result())).pack()

    def answer(self, event):
        self.questions6_views[self.current_question].answer()

        if self.current_question < len(self.questions6) - 1:
            self.current_question += 1

            for widget in self.root.winfo_children():
                widget.destroy()

            self.start()
        else:
            for widget in self.root.winfo_children():
                widget.destroy()

            self.result()


def main():
    root = Tk()
    root.geometry("200x200")
    Test(root).start()
    root.mainloop()

if __name__ == '__main__':
    main()
