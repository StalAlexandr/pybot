# -*- coding: utf-8 -*-

from answer import Answer
from botmind import BotMind
from weightcalc import WeightCalcByWords

mb = BotMind("aa")

phrases= ["Привет", "Как дела?", "Ты ко такой?"]
answers = list(map(lambda x: Answer(x), phrases))

wwc = WeightCalcByWords(list('выпить'))

answers.append(Answer('да, давайте бухнем!', wwc))

mb.set_answers(answers)

rep = mb.replay("1", "2")
print rep.phrase

rep = mb.replay("надо выпить", "2")
print rep.phrase

rep = mb.replay("1", "2")
print rep.phrase

