from answer import Answer


class BotMind:

    answers = []

    def __init__(self, name):
        self.name = name

    def replay(self,req,author):

        if len(self.answers) == 0:
            return Answer("")

        current_answer = self.answers[0]
        current_weight = current_answer.weight(req, author)

        for a in self.answers:
            def_weight = a.weight(req, author)
            if def_weight > current_weight:
                current_weight = def_weight
                current_answer = a

        self.answers.remove(current_answer)

        return current_answer

    def set_answers(self, answers):
        self.answers = answers
