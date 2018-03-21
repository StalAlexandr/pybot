from weightcalc import WeightCalcDefault


class Answer:

    def calc(self, req, author):
        return self.weight_calc.calc(req, author)

    def __init__(self, phrase, weight_calc=WeightCalcDefault()):
        self.phrase = phrase
        self.weight_calc = weight_calc

    def weight(self, req, author):
        return self.calc(req, author)