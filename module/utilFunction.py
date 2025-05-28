import calendar
from module.Database import Database
from datetime import datetime, timedelta
from module.UserReport import UserReport
from pymongo import DESCENDING


class utilFunction:
    def __init__(self):
        self.databaseCon = Database()

    def getPeriodCycle(self):
        user_reports = self.databaseCon.db["user_reports"]
        last_three_reports = list(
            user_reports.find().sort("start_at", DESCENDING).limit(3)
        )
        return last_three_reports

    def getPeriodForMonth(self, month: int):
        year = datetime.now().year

        collection = self.databaseCon.db["user_reports"]
        last_report = collection.find_one(sort=[("start_at", -1)])

        if not last_report or "start_at" not in last_report:
            return []

        start_date = last_report["start_at"]
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        elif isinstance(start_date, dict) and "$date" in start_date:
            start_date = datetime.fromisoformat(
                start_date["$date"]
            )  # Mongo shell formats

        cycle_length = 29
        period_length = 5

        # Define month boundaries
        start_of_month = datetime(year, month, 1)
        end_of_month = datetime(year, month, calendar.monthrange(year, month)[1])

        predicted_days = []
        current = start_date

        while current <= end_of_month:
            for i in range(period_length):
                day = current + timedelta(days=i)
                if start_of_month <= day <= end_of_month:
                    predicted_days.append(day.strftime("%d/%m/%Y"))
            current += timedelta(days=cycle_length)

        return predicted_days

    def requireStart(self, date):
        user_report = UserReport(start_at=date, end_at=date + timedelta(days=5))
        user_report.save_to_db()
        return user_report

    def requireEnd(self, date):
        latest_report = self.databaseCon.db["user_reports"].find_one(
            sort=[("start_at", DESCENDING)]
        )
        if not latest_report:
            return None
        self.databaseCon.db["user_reports"].update_one(
            {"_id": latest_report["_id"]}, {"$set": {"end_at": date}}
        )
        return UserReport(
            _id=latest_report["_id"], start_at=latest_report["start_at"], end_at=date
        )
