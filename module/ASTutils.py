from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module.utilFunction import utilFunction
class CycleStatusOp ():
    def __init__ (self, time):
        self.time =time

class SpecificPhraseOp():
    def __init__ (self, phrase, time):
        self.phrase = phrase,
        self.time = time
        util = utilFunction()
class RequireOp():
    def __init__(self, verb, time):
        self.util = utilFunction()
        self.verb = verb
        self.time = time
    def action (self):
        if (self.verb == "start"):
            self.util.requireStart(self.time)
        elif (self.verb == 'end'):
            self.util.requireEnd(self.time)
