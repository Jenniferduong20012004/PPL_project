from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from datetime import datetime


class CycleStatusOp:
    def __init__(self, time):
        self.time = time


class SpecificPhraseOp:
    def __init__(self, phrase, time):
        self.phrase = (phrase,)
        self.time = time


class RequireOp:
    def __init__(self, verb, time):
        self.verb = verb
        self.time = time

    def to_dict(self):
        return {
            "type": "RequireOp",
            "verb": self.verb,
            "time": self.time,
        }

    def __repr__(self):
        return str(self.to_dict())
