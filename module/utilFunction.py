import calendar
from module.Database import Database
from datetime import datetime, timedelta
from module.UserReport import UserReport
from pymongo import DESCENDING


class utilFunction:
    def __init__(self):
        self.databaseCon = Database()
        user_reports = self.databaseCon.db["user_reports"]
        last_three_reports = list(
            user_reports.find().sort("start_at", DESCENDING).limit(3)
        )
        last_three_reports.sort(key=lambda x: x['start_at'])
        durations = []
        for report in last_three_reports:
            start = report['start_at']
            end = report['end_at']
            if isinstance(start, str):
                start = datetime.fromisoformat(start)
            if isinstance(end, str):
                end = datetime.fromisoformat(end)
            diff_days = (end.date() - start.date()).days
            durations.append(diff_days)

        mean_duration = sum(durations) / len(durations) if durations else 0
        

        # Calculate differences between start_at of different reports
        start_diffs = []
        for i in range(1, len(last_three_reports)):
            prev_start = last_three_reports[i - 1]['start_at']
            curr_start = last_three_reports[i]['start_at']
            if isinstance(prev_start, str):
                prev_start = datetime.fromisoformat(prev_start)
            if isinstance(curr_start, str):
                curr_start = datetime.fromisoformat(curr_start)
            diff_days = (curr_start.date() - prev_start.date()).days
            start_diffs.append(diff_days)

        mean_start_diff = sum(start_diffs) / len(start_diffs) if start_diffs else 0
    def getOvulationWithMonth(self, time):
        user_reports = self.databaseCon.db["user_reports"]
        last_three_reports = list(
            user_reports.find().sort("start_at", DESCENDING).limit(3)
        )
        last_three_reports.sort(key=lambda x: x['start_at'])
        durations = []
        for report in last_three_reports:
            start = report['start_at']
            end = report['end_at']
            if isinstance(start, str):
                start = datetime.fromisoformat(start)
            if isinstance(end, str):
                end = datetime.fromisoformat(end)
            diff_days = (end.date() - start.date()).days
            durations.append(diff_days)

        mean_duration = sum(durations) / len(durations) if durations else 0

        # Calculate differences between start_at of different reports
        start_diffs = []
        for i in range(1, len(last_three_reports)):
            prev_start = last_three_reports[i - 1]['start_at']
            curr_start = last_three_reports[i]['start_at']
            if isinstance(prev_start, str):
                prev_start = datetime.fromisoformat(prev_start)
            if isinstance(curr_start, str):
                curr_start = datetime.fromisoformat(curr_start)
            diff_days = (curr_start.date() - prev_start.date()).days
            start_diffs.append(diff_days)

        mean_start_diff = sum(start_diffs) / len(start_diffs) if start_diffs else 0

        print("Mean report duration:", mean_duration)
        print("Mean start_at difference between reports:", mean_start_diff)
    def getCycleStatusOnDate(self, date):
        # lay thong tin cycle bang ngay (co trong ovulation, period non fertile hay z ko nha), ngay da co the input vao mongo
        return "lam dum tui nha phuc"

    def getPeriodCycle(self):
        user_reports = self.databaseCon.db["user_reports"]
        last_three_reports = list(
            user_reports.find().sort("start_at", DESCENDING).limit(3)
        )
        return last_three_reports


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
