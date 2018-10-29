class Question1:
    def __init__(self, question, right_answer):
        self.question = question
        self.right_answer = right_answer
        self.user_answer = ""

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

    def set_user_answer(self, user_answer):
        self.user_answer = user_answer

    def get_user_answer(self):
        return self.user_answer

    def get_question(self):
        return self.question


class Question4:
    def __init__(self, question, interval):
        self.question = question
        self.interval = interval
        self.user_answer = ""

    def set_user_answer(self, user_answer):
        self.user_answer = user_answer

    def get_user_answer(self):
        return self.user_answer

    def get_question(self):
        return self.question

    def get_left_dot(self):
        return self.interval[0]

    def get_right_dot(self):
        return self.interval[1]

