import calendar
from module.Database import Database
from datetime import datetime, timedelta
from module.UserReport import UserReport
from pymongo import DESCENDING
from dateutil.relativedelta import relativedelta


class utilFunction:
    def __init__(self):
        self.databaseCon = Database()

        # Shared cycle parameters
        self.cycle_length = 29
        self.period_length = 5
        self.fertile_start_offset = 10
        self.fertile_end_offset = 16
        self.ovulation_offset = 14

    def getCycleStatusOnDate(self, date: datetime):
        latest_report = self.databaseCon.db["user_reports"].find_one(
            sort=[("start_at", DESCENDING)]
        )
        if not latest_report or "start_at" not in latest_report:
            return None

        start_at = latest_report["start_at"]
        if isinstance(start_at, str):
            start_at = datetime.strptime(start_at, "%Y-%m-%d")
        elif isinstance(start_at, dict) and "$date" in start_at:
            start_at = datetime.fromisoformat(start_at["$date"])

        current_cycle_start = start_at
        while current_cycle_start + timedelta(days=self.cycle_length) < date:
            current_cycle_start += timedelta(days=self.cycle_length)

        period_range = (
            current_cycle_start,
            current_cycle_start + timedelta(days=self.period_length - 1),
        )
        fertile_range = (
            current_cycle_start + timedelta(days=self.fertile_start_offset),
            current_cycle_start + timedelta(days=self.fertile_end_offset),
        )
        ovulation_date = current_cycle_start + timedelta(days=self.ovulation_offset)

        if period_range[0] <= date <= period_range[1]:
            return "period"
        elif fertile_range[0] <= date <= fertile_range[1]:
            if ovulation_date == date:
                return "ovulation"
            return "fertile"
        else:
            return "non-fertile"

    def getPeriodCycle(self):
        return list(
            self.databaseCon.db["user_reports"]
            .find()
            .sort("start_at", DESCENDING)
            .limit(3)
        )

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
            start_date = datetime.fromisoformat(start_date["$date"])

        start_of_month = datetime(year, month, 1)
        end_of_month = datetime(year, month, calendar.monthrange(year, month)[1])

        predicted_days = []
        current = start_date

        while current <= end_of_month:
            for i in range(self.period_length):
                day = current + timedelta(days=i)
                if start_of_month <= day <= end_of_month:
                    predicted_days.append(day.strftime("%d/%m/%Y"))
            current += timedelta(days=self.cycle_length)

        return predicted_days

    def requireStart(self, date):
        user_report = UserReport(
            start_at=date, end_at=date + timedelta(days=self.period_length)
        )
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

    def getNonFertileRangeByTime(self, date: datetime):
        latest_report = self.databaseCon.db["user_reports"].find_one(
            sort=[("start_at", DESCENDING)]
        )
        if not latest_report or "end_at" not in latest_report:
            return None

        end_at = latest_report["end_at"]
        if isinstance(end_at, str):
            end_at = datetime.strptime(end_at, "%Y-%m-%d")
        elif isinstance(end_at, dict) and "$date" in end_at:
            end_at = datetime.fromisoformat(end_at["$date"])

        delta = relativedelta(date, end_at)
        total_months = delta.years * 12 + delta.months
        ovulation_day = (
            end_at
            + relativedelta(months=+total_months)
            + timedelta(days=self.ovulation_offset)
        )

        non_fertile_start = ovulation_day - timedelta(days=5)
        non_fertile_end = ovulation_day + timedelta(days=5)

        return {
            "start_at": non_fertile_start.strftime("%d/%m/%Y"),
            "end_at": non_fertile_end.strftime("%d/%m/%Y"),
        }

    def getPeriodRangeByTime(self, date: datetime):
        latest_report = self.databaseCon.db["user_reports"].find_one(
            sort=[("start_at", DESCENDING)]
        )
        if not latest_report or "end_at" not in latest_report:
            return None

        end_at = latest_report["end_at"]
        if isinstance(end_at, str):
            end_at = datetime.strptime(end_at, "%Y-%m-%d")
        elif isinstance(end_at, dict) and "$date" in end_at:
            end_at = datetime.fromisoformat(end_at["$date"])

        delta = relativedelta(date, end_at)
        total_months = delta.years * 12 + delta.months
        predicted_start = end_at + relativedelta(months=+total_months)
        predicted_end = predicted_start + timedelta(days=self.period_length - 1)

        return {
            "start_at": predicted_start.strftime("%d/%m/%Y"),
            "end_at": predicted_end.strftime("%d/%m/%Y"),
        }
