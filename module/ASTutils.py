from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from datetime import datetime
from module.utilFunction import utilFunction

class CycleStatusOp:
    def __init__(self, time):
        self.time = time
        self.utilFunction = utilFunction()
    def action(self):
        return str (self.utilFunction.getCycleStatusOnDate(self.time))


class SpecificPhraseOp:
    def __init__(self, phrase, time):
        self.phrase = phrase
        self.time = time
    def action (self):
        if (self.phrase == 'ovulation'):
            return "phuc oi lam cho toi nay la lay phrase ovulation o thang do (time)"
        elif (self.phrase == 'fertile'):
            return "phuc oi lam cho toi nay la lay phrase fertile o thang do (time)"
        elif (self.phrase == 'non-fertile'):
            return "phuc oi lam cho toi nay la lay phrase non-fertile o thang do (time)"
        elif (self.phrase == 'period'):
            return "phuc oi lam cho toi nay la lay phrase period o thang do (time)"

class RequireOp:
    def __init__(self, verb, time):
        self.verb = verb
        self.time = time
        self.utilFunction = utilFunction()
    def action (self):
        if (self.verb == 'show'):
            return str(self.utilFunction.getPeriodCycle())
        elif (self.verb == 'start'):
            if (self.time == None):
                return "Please input date"
            else:
                return str(self.utilFunction.requireStart(self.time))
        elif (self.verb == 'end'):
            if (self.time == None):
                return "Please input date"
            else:
                return str (self.utilFunction.requireEnd(self.time))

    def to_dict(self):
        return {
            "type": "RequireOp",
            "verb": self.verb,
            "time": self.time,
        }

    def __repr__(self):
        return str(self.to_dict())