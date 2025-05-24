import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module.Database import Database
from datetime import datetime, timedelta

class utilFunction():
    def __init__(self):
        self.databaseCon = Database();
    def  getPeriodCycle(self):
        return ("phuc oi lam cho toi")

    def getPeriodForMonth(self, month: int):
        year = datetime.now().year

        collection = self.db.db["user_reports"]
        last_report = collection.find_one(sort=[("created_at", -1)])

        if not last_report or "start_date" not in last_report:
            return []

        start_date = last_report["start_date"]
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d")

        settings = self.db.db["user_settings"].find_one()
        cycle_length = settings.get("cycle_length", 29)
        period_length = settings.get("period_length", 5)

        start_of_month = datetime(year, month, 1)
        end_of_month = datetime(year, month, calendar.monthrange(year, month)[1])

        predicted_days = []
        current = start_date

        while current <= end_of_month:
            for i in range(period_length):
                day = current + timedelta(days=i)
                if start_of_month <= day <= end_of_month:
                    predicted_days.append(day.strftime("%Y-%m-%d"))
            current += timedelta(days=cycle_length)

        return predicted_days

    def requireStart (self,  date):
        # implement input start with date is accepted by mongo already (nay la cho period nha)
        return ("phuc oi lam dum toi nha")
    def requireEnd (self,  date):
        # implement input end with date is accepted by mongo already (nay la cho period nha)
        return ("phuc oi lam dum toi nha")