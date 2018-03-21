class WeightCalcDefault(object):

    def calc(self, req, author):
        return 1


class WeightCalcByWords(WeightCalcDefault):

    def __init__(self, worlds):
        self.worlds = worlds

    def calc(self, req, author):
        weight = 1
        for world in self.worlds:
            if world in req:
                weight=weight+1
        return weight