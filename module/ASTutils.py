from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from datetime import datetime
from module.utilFunction import utilFunction
class SympOp:
    def __init__(self, listSymp):
        self.utilFunction = utilFunction()
        self.listSymp = listSymp
        self.result = None
    def action(self):
        self.result = self.utilFunction.getSymp(self.listSymp)
    def to_dict(self):
        return {
            "type": "SympOp",
            "result": self.result,
        }
class CheckOp:
    def __init__(self):
        self.utilFunction = utilFunction()
        self.result = None
    def action(self):
        self.result = self.utilFunction.checkStatistic()
    def to_dict(self):
        return {
            "type": "CheckOp",
            "result": self.result,
        }
class CycleStatusOp:
    def __init__(self, time):
        self.time = time
        self.utilFunction = utilFunction()
        self.result = None

    def to_dict(self):
        return {
            "type": "CycleStatusOp",
            "time": self.time,
            "result": self.result,
        }

    def action(self):
        self.result = self.utilFunction.getCycleStatusOnDate(self.time)


class SpecificPhraseOp:
    def __init__(self, phrase, time):
        self.phrase = phrase
        self.time = time
        self.utilFunction = utilFunction()
        self.result = None

    def action(self):
        if self.phrase == "ovulation":
            self.result = self.utilFunction.getOvulationRangeByTime(self.time)
        elif self.phrase == "fertile":
            self.result = self.utilFunction.getFertileRangeByTime(self.time)
        elif self.phrase == "non-fertile":
            self.result = self.utilFunction.getNonFertileRangeByTime(self.time)
        elif self.phrase == "period":
            self.result = self.utilFunction.getPeriodRangeByTime(self.time)

    def to_dict(self):
        return {
            "type": "SpecificPhraseOp",
            "phrase": self.phrase,
            "time": self.time,
            "result": self.result,
        }


class RequireOp:
    def __init__(self, verb, time):
        self.verb = verb
        self.time = time
        self.utilFunction = utilFunction()
        self.result = None

    def action(self):
        if self.verb == "show":
            self.result = self.utilFunction.getPeriodCycle()
        elif self.verb == "start":
            if self.time is None:
                self.result = "Please input date"
            else:
                self.result = self.utilFunction.requireStart(self.time)
        elif self.verb == "end":
            if self.time is None:
                self.result = "Please input date"
            else:
                self.result = self.utilFunction.requireEnd(self.time)

    def to_dict(self):
        return {
            "type": "RequireOp",
            "verb": self.verb,
            "time": self.time,
            "result": self.result,
        }

    def __repr__(self):
        return self.to_dict()
