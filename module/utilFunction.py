import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module.Database import Database
class utilFunction():
    def __init__(self):
        self.databaseCon = Database();
    def  getPeriodCycle(self):
        return ("phuc oi lam cho toi")
    def getPeriodForMonth(self):
        return ("nghi oi lam cho toi")
    def requireStart (self, dateType, date):
        print (dateType)
        return "akb"