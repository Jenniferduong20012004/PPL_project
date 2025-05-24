import os
import sys
from Database import Database


class UtilFunction:
    def __init__(self):
        self.db = Database()

    def getPeriodCycle(self):
        collection = self.db["user_reports"]
        last_three_reports = list(collection.find().sort("created_at", -1).limit(3))
        return last_three_reports

    def getPeriodForMonth(self):
        return "nghi oi lam cho toi"

    def requireStart(self, dateType, date):
        if dateType == "dateCompare":
            return "aks"
        elif dateType == "dateInNum":
            return "ajks"
        elif dateType == "dateInWord":
            return "askjd ak"
