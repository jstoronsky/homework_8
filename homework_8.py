import random

questions_dict = [{
    "q": "How many days do we have in a week?",
    "d": "1",
    "a": "7"
}, {
    "q": "How many letters are there in the English alphabet?",
    "d": "3",
    "a": "26"
}, {
    "q": "How many sides are there in a triangle?",
    "d": "2",
    "a": "3"
}, {
    "q": "How many years are there in one Millennium?",
    "d": "2",
    "a": "1000"
}, {
    "q": "How many sides does hexagon have?",
    "d": "4",
    "a": "6"
}]


class Question:
    def __init__(self, question, difficulty, correct_ans, score=0):
        self.question = question
        self.difficulty = int(difficulty)
        self.correct_ans = correct_ans
        self.score = score

    def get_points(self):
        """
        Считаем количество баллов за правильный ответ в зависимости от сложности
        """
        self.score = self.difficulty * 10
        return self.score

    def build_question(self):
        """
        Построение вопроса и отображение его сложности
        """
        return f"Вопрос: {self.question} \nCложность: {self.difficulty}/5"

    def build_positive_feedback(self):
        """
        Построение вывода программы при правильном ответе
        """
        return f"Ответ верный, получено баллов {self.score}"

    def build_negative_feedback(self):
        """
        Построение вывода программы при неправильном ответе
        """
        return f"Ответ неверный, верный ответ -- {self.correct_ans}"


# Перемешываем наш список словарей и создаём переменные для списка ответов и итогового балла
random.shuffle(questions_dict)
list_of_asked_questions = []
total_score = 0

# Запускаем перебор по нашему списку словарей
for question_ in questions_dict:
    question_1 = Question(question_["q"], question_["d"], question_["a"])
    print(question_1.build_question())
    user_input_1 = input("Введите ваш ответ: ")
    question_1.answer = user_input_1
    if user_input_1 == question_1.correct_ans:
        list_of_asked_questions.append(True)
        total_score += question_1.get_points()
        print(f"{question_1.build_positive_feedback()}")
    else:
        list_of_asked_questions.append(False)
        print(f"{question_1.build_negative_feedback()}")

# Итоговый вывод
print(f"Вот и всё! Отвечено {list_of_asked_questions.count(True)} вопроса из {len(list_of_asked_questions)}")
print(f"Набрано баллов: {total_score}")
