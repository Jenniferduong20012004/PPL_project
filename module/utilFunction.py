import calendar
from module.Database import Database
from datetime import datetime, timedelta
from module.UserReport import UserReport
from pymongo import DESCENDING
from dateutil.relativedelta import relativedelta


class utilFunction:
    def __init__(self):
        self.databaseCon = Database()
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
            "reminder": "During your period, it's important to maintain good hygiene by changing sanitary products regularly to prevent infections. Stay hydrated, get enough rest, and manage any cramps or discomfort with gentle exercise, heat packs, or pain relief if needed. Eating balanced meals and avoiding excessive caffeine or salty foods can help reduce bloating and mood swings. While fertility is low during menstruation, remember that cycle lengths vary, so pregnancy is still possible if you have a short cycle. Listening to your body and practicing self-care during this time supports overall well-being.",
        }
    
    def getOvulationRangeByTime(self,date):
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


        return {
            "ovulation_day": ovulation_day.strftime("%d/%m/%Y"),
        }
    def getFertileRangeByTime (self, date):
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

        fertile_start = ovulation_day - timedelta(days=5)
        fertile_end = ovulation_day

        return {
            "start_at": fertile_start.strftime("%d/%m/%Y"),
            "end_at": fertile_end.strftime("%d/%m/%Y"),
            "reminder": "During fertile days, typically around ovulation, a woman is most likely to conceive. If trying to get pregnant, this is the best time for unprotected sex, supported by a healthy lifestyle and tracking signs like cervical mucus or ovulation kits. If avoiding pregnancy, it's crucial to use protection, as this window is the riskiest for unplanned conception. Understanding your cycle and being mindful of your goals helps you make informed reproductive choices.",
        }





#         user_reports = self.databaseCon.db["user_reports"]
#         last_three_reports = list(
#             user_reports.find().sort("start_at", DESCENDING).limit(3)
#         )
#         last_three_reports.sort(key=lambda x: x['start_at'])
#         durations = []
#         for report in last_three_reports:
#             start = report['start_at']
#             end = report['end_at']
#             if isinstance(start, str):
#                 start = datetime.fromisoformat(start)
#             if isinstance(end, str):
#                 end = datetime.fromisoformat(end)
#             diff_days = (end.date() - start.date()).days
#             durations.append(diff_days)

#         mean_duration = sum(durations) / len(durations) if durations else 0
        

#         # Calculate differences between start_at of different reports
#         start_diffs = []
#         for i in range(1, len(last_three_reports)):
#             prev_start = last_three_reports[i - 1]['start_at']
#             curr_start = last_three_reports[i]['start_at']
#             if isinstance(prev_start, str):
#                 prev_start = datetime.fromisoformat(prev_start)
#             if isinstance(curr_start, str):
#                 curr_start = datetime.fromisoformat(curr_start)
#             diff_days = (curr_start.date() - prev_start.date()).days
#             start_diffs.append(diff_days)

#         mean_start_diff = sum(start_diffs) / len(start_diffs) if start_diffs else 0
#     def getOvulationWithMonth(self, time):
#         user_reports = self.databaseCon.db["user_reports"]
#         last_three_reports = list(
#             user_reports.find().sort("start_at", DESCENDING).limit(3)
#         )
#         last_three_reports.sort(key=lambda x: x['start_at'])
#         durations = []
#         for report in last_three_reports:
#             start = report['start_at']
#             end = report['end_at']
#             if isinstance(start, str):
#                 start = datetime.fromisoformat(start)
#             if isinstance(end, str):
#                 end = datetime.fromisoformat(end)
#             diff_days = (end.date() - start.date()).days
#             durations.append(diff_days)

#         mean_duration = sum(durations) / len(durations) if durations else 0

#         # Calculate differences between start_at of different reports
#         start_diffs = []
#         for i in range(1, len(last_three_reports)):
#             prev_start = last_three_reports[i - 1]['start_at']
#             curr_start = last_three_reports[i]['start_at']
#             if isinstance(prev_start, str):
#                 prev_start = datetime.fromisoformat(prev_start)
#             if isinstance(curr_start, str):
#                 curr_start = datetime.fromisoformat(curr_start)
#             diff_days = (curr_start.date() - prev_start.date()).days
#             start_diffs.append(diff_days)

#         mean_start_diff = sum(start_diffs) / len(start_diffs) if start_diffs else 0

#         print("Mean report duration:", mean_duration)
#         print("Mean start_at difference between reports:", mean_start_diff)
#     def getCycleStatusOnDate(self, date):
#         # lay thong tin cycle bang ngay (co trong ovulation, period non fertile hay z ko nha), ngay da co the input vao mongo
#         return "lam dum tui nha phuc"
# =======
