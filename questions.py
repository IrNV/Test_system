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
    def __init__(self, question, left_dot, right_dot):
        self.question = question
        self.left_dot = left_dot
        self.right_dot = right_dot

    def set_user_answer(self, user_left_dot, user_right_dot):
        self.user_left_dot = user_left_dot
        self.user_right_dot = user_right_dot

    def get_user_left_dot(self):
        return self.user_left_dot

    def get_user_right_dot(self):
        return self.user_right_dot

    def get_question(self):
        return self.question

    def get_left_dot(self):
        return self.left_dot

    def get_right_dot(self):
        return self.right_dot


class Question5(Question4):
    def __init__(self, question, left_dot, right_dot):
        Question4.__init__(self, question, left_dot, right_dot)


class Question6:
    def __init__(self, question, mode, interval):
        self.question = question
        self.mode = mode
        self.interval = interval

    def set_user_answer(self, user_mode, user_interval):
        self.user_mode = user_mode
        self.user_interval = user_interval

    def get_user_mode(self):
        return self.user_mode

    def get_user_interval(self):
        return self.user_interval

    def get_question(self):
        return self.question

    def get_mode(self):
        return self.mode

    def get_interval(self):
        return self.interval


class Question7:
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