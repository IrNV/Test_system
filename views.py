from tkinter import *


class Question1View:
    def __init__(self, obj, root):
        self.quest_obj = obj
        self.root = root
        self.radio_var = StringVar(value=" ")

    def show(self):
        Label(self.root, text=self.quest_obj.get_question()).pack()

        rbutton1 = Radiobutton(self.root, text='YES', variable=self.radio_var, value="YES")
        rbutton2 = Radiobutton(self.root, text='NO', variable=self.radio_var, value="NO")
        rbutton1.pack()
        rbutton2.pack()

    def answer(self):
        print(self.radio_var.get())
        self.quest_obj.set_user_answer(self.radio_var.get())


class Question2View:
    def __init__(self, obj, root):
        self.quest_obj = obj
        self.root = root
        self.radio_var = StringVar(value=" ")

    def show(self):
        Label(self.root, text=self.quest_obj.get_question()).pack()

        for key, value in self.quest_obj.data.items():
            Radiobutton(self.root, text=key, variable=self.radio_var, value=key).pack()

    def answer(self):
        print(self.radio_var.get())
        self.quest_obj.set_user_answer(self.radio_var.get())


class Question3View:
    def __init__(self, obj, root):
        self.quest_obj = obj
        self.root = root
        self.radio_vars = []

    def show(self):
        Label(self.root, text=self.quest_obj.get_question()).pack()

        for key, value in self.quest_obj.data.items():
            self.radio_vars.append(StringVar(value=""))
            Checkbutton(self.root, text=key, variable=self.radio_vars[-1],
                        onvalue=key, offvalue="").pack()

    def answer(self):
        self.quest_obj.set_user_answer([radio_var.get() for radio_var in self.radio_vars if radio_var.get()])


class Question4View:
    def __init__(self, obj, root):
        self.quest_obj = obj
        self.root = root

    def show(self):
        Label(self.root, text=self.quest_obj.get_question()).pack()

        self.entry = Entry(self.root)
        self.entry.pack()

    def answer(self):
        print(self.entry.get())
        self.quest_obj.set_user_answer(float(self.entry.get()))


class Question5View:
    def __init__(self, obj, root):
        self.quest_obj = obj
        self.root = root

    def show(self):
        Label(self.root, text=self.quest_obj.get_question()).pack()

        self.entry_left = Entry(self.root)
        self.entry_left.pack()

        self.entry_right = Entry(self.root)
        self.entry_right.pack()

    def answer(self):
        print([float(self.entry_left.get()), float(self.entry_right.get())])
        left_dot = float(self.entry_left.get())
        right_dot = float(self.entry_right.get())
        self.quest_obj.set_user_answer(left_dot, right_dot)


class Question6View:
    def __init__(self, obj, root):
        self.quest_obj = obj
        self.root = root

    def show(self):
        Label(self.root, text=self.quest_obj.get_question()).pack()

        self.entry_left = Entry(self.root)
        self.entry_left.pack()

        self.entry_right = Entry(self.root)
        self.entry_right.pack()

    def answer(self):
        print([float(self.entry_left.get()), float(self.entry_right.get())])
        mode = float(self.entry_left.get())
        interval = float(self.entry_right.get())
        self.quest_obj.set_user_answer(mode, interval)


class Question7View:
    def __init__(self, obj, root):
        self.quest_obj = obj
        self.root = root

    def show(self):
        Label(self.root, text=self.quest_obj.get_question(), font='arial 14').pack()

        self.entry = Entry(self.root, font='arial 14')
        self.entry.pack()

    def answer(self):
        print(self.entry.get())
        self.quest_obj.set_user_answer(self.entry.get())