import calendar
from module.Database import Database
from datetime import datetime, timedelta
from module.UserReport import UserReport
from pymongo import DESCENDING
from dateutil.relativedelta import relativedelta
import diskcache as dc
from calendar import monthrange


class utilFunction:
    
    def __init__(self):
        self.databaseCon = Database()
        self.cache = dc.Cache('./mycache')
        self.cycle_length = 29
        self.period_length = 5
        self.fertile_start_offset = 10
        self.fertile_end_offset = 16
        self.ovulation_offset = 14
        

    def initPeriodForMonth(self):
        latest_report = self.databaseCon.db["user_reports"].find_one(
            sort=[("start_at", DESCENDING)]
        )

        if not latest_report or "start_at" not in latest_report:
            self.cache['period_length'] = 5
            self.cache['cycle_length'] = 29
            self.cache['ovulation_offset'] = 14
            self.cache['fertile_start_offset'] = 10
            self.cache['fertile_end_offset']= 16
            return "Quick reminder: You have not entered any period day into the system. Please add for calculation!"
        
        user_reports = self.databaseCon.db["user_reports"]
        last_three_reports = list(
            user_reports.find().sort("start_at", DESCENDING).limit(3)
        )
        last_three_reports.sort(key=lambda x: x['start_at'])

        durations = []
        for report in last_three_reports:
            start = report['start_at']
            end = report['end_at']
            if not end:
                continue
            if isinstance(start, str):
                start = datetime.fromisoformat(start)
            if isinstance(end, str):
                end = datetime.fromisoformat(end)
            diff_days = (end.date() - start.date()).days + 1
            durations.append(diff_days)

        mean_duration = sum(durations) / len(durations) if durations else 5
        self.cache['period_length'] = mean_duration

        # print(cache['key'])     
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

        mean_start_diff = sum(start_diffs) / len(start_diffs) if start_diffs else 29 # mean cycle length of 2 nearest cycles
        self.cache['cycle_length'] = mean_start_diff

        # Ovulation usually happens 14 days before the next period
        ovulation_offset = mean_start_diff - 14   # days after period starts

        # Fertile window is 5-6 days ending on ovulation day
        fertile_start_offset = ovulation_offset - 5  # 5 days before ovulation
        fertile_end_offset = ovulation_offset        # ends at ovulation day

        self.cache['ovulation_offset'] = ovulation_offset 
        self.cache['fertile_start_offset'] = fertile_start_offset
        self.cache['fertile_end_offset']= fertile_end_offset

        return f"Initialized cache: period_length={mean_duration:.1f}, cycle_length={mean_start_diff:.1f}"

    # symptom logging
    def getSymp (self, listOfSymp):
        now = datetime.now()
        latest_report = self.databaseCon.db["user_reports"].find_one(
            sort=[("start_at", DESCENDING)]
        )

        if not latest_report or "end_at" not in latest_report:
            return None

        start_at = latest_report["start_at"]
        if isinstance(start_at, str):
            start_at = datetime.strptime(start_at, "%Y-%m-%d")
        elif isinstance(start_at, dict) and "$date" in start_at:
            start_at = datetime.fromisoformat(start_at["$date"])

        cycle_length = self.cache.get("cycle_length")
        period_length = self.cache.get("period_length")

        # Calculate how many full cycles have passed since start_at
        days_passed = (now - start_at).days
        cycles_passed = days_passed // cycle_length + 1  # Next predicted cycle

        predicted_start = start_at + timedelta(days=cycles_passed * cycle_length)
        predicted_end = predicted_start + timedelta(days=period_length)
        result = ", ".join(listOfSymp)
        # Check if now is within the predicted period
        if predicted_start <= now <= predicted_end:
            return {
                "recorded_date": now.strftime("%Y-%m-%d"),
                "predicted_start": predicted_start.strftime("%Y-%m-%d"),
                "predicted_end": predicted_end.strftime("%Y-%m-%d"),
                "phase": "period",
                "reminder": f"You are currently in your period. {result} are common period symptoms, usually linked to PMS or primary dysmenorrhea..."
            }
        else:
            return {
                "recorded_date": now.strftime("%Y-%m-%d"),
                "predicted_start": predicted_start.strftime("%Y-%m-%d"),
                "predicted_end": predicted_end.strftime("%Y-%m-%d"),
                "phase": "non-period",
                "reminder": f"You are currently not in your period. If you're experiencing {result} now, it could be due to other causes such as ovulation, stress, digestive issues, or underlying conditions like IBS, hormonal imbalance, or infections."
            }

    # check cycle statistic
    def checkStatistic(self):
        period_length = self.cache.get('period_length', 5)
        cycle_length = self.cache.get('cycle_length', 29)

        cycleNormal = 21 <= cycle_length <= 35
        periodNormal = 2 <= period_length <= 7

        if cycleNormal and periodNormal:
            reminder = (
                "\nYour cycle falls within the normal range. "
                "A typical menstrual cycle lasts 21 to 35 days, with periods lasting 2 to 7 days. "
                "While most people have a 28-day cycle and bleed for 3 to 5 days, slight variations are perfectly normal."
            )
        elif cycleNormal and not periodNormal:
            if period_length > 7:
                reminder = "\nYour cycle is normal, but bleeding for over 7 days may indicate menorrhagia..."
            else:  # < 2
                reminder = "\nYour cycle is normal, but your period is shorter than usual..."
        elif not cycleNormal and periodNormal:
            if cycle_length < 21:
                reminder = "\nYour period is normal, but a cycle shorter than 21 days may indicate polymenorrhea..."
            else:  # > 35
                reminder = "\nYour period is normal, but a cycle longer than 35 days may indicate oligomenorrhea..."
        else:
            reminder = (
                "\nBoth your cycle length and period duration fall outside the normal range. "
                "A typical cycle is 21–35 days with bleeding lasting 2–7 days. "
                "While some variation is normal, consistently irregular or unpredictable periods should be evaluated by a healthcare provider."
            )

        return {
            "cycle_length": round(cycle_length, 2),
            "period_length": round(period_length, 2),
            "reminder": reminder
        }
    
    # cycle status on date
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
        while current_cycle_start + timedelta(days=self.cache.get('cycle_length')) < date:
            current_cycle_start += timedelta(days=self.cache.get('cycle_length'))

        period_range = (
            current_cycle_start,
            current_cycle_start + timedelta(days=self.cache.get('period_length') - 1),
        )
        fertile_range = (
            current_cycle_start + timedelta(days=self.cache.get('fertile_start_offset')),
            current_cycle_start + timedelta(days=self.cache.get('fertile_end_offset')),
        )
        ovulation_date = current_cycle_start + timedelta(days=self.cache.get('ovulation_offset'))

        if period_range[0] <= date <= period_range[1]:
            return "period"
        elif fertile_range[0] <= date <= fertile_range[1]:
            if ovulation_date == date:
                return "ovulation"
            return "fertile"
        else:
            return "non-fertile"

    # show period cycle
    def getPeriodCycle(self):
        return list(
            self.databaseCon.db["user_reports"]
            .find()
            .sort("start_at", DESCENDING)
            .limit(3)
        )

    # start date
    def requireStart(self, date):
        user_report = UserReport(
            start_at=date, end_at=date + timedelta(days=self.cache.get('period_length'))
        )
        user_report.save_to_db()
        self.initPeriodForMonth()
        return user_report

    # end date
    def requireEnd(self, date):
        latest_report = self.databaseCon.db["user_reports"].find_one(
            sort=[("start_at", DESCENDING)]
        )
        if not latest_report:
            return None
        
        start_at = latest_report["start_at"]
        if isinstance(start_at, str):
            start_at = datetime.fromisoformat(start_at)

        if date < start_at:
            return {
                "type": "RequireOp",
                "verb": "end",
                "time": date,
                "result": "End date cannot be earlier than start date"
            }

        self.databaseCon.db["user_reports"].update_one(
            {"_id": latest_report["_id"]}, {"$set": {"end_at": date}}
        )
        self.initPeriodForMonth()
        return UserReport(
            _id=latest_report["_id"], start_at=start_at, end_at=date
        )

    # get non-fertile days (predicted)
    def getNonFertileRangeByTime(self, date: datetime):
        latest_report = self.databaseCon.db["user_reports"].find_one(
                sort=[("start_at", DESCENDING)]
        )
        if not latest_report or "end_at" not in latest_report:
            return None

        start_at = latest_report["start_at"]
        if isinstance(start_at, str):
            start_at = datetime.strptime(start_at, "%Y-%m-%d")
        elif isinstance(start_at, dict) and "$date" in start_at:
            start_at = datetime.fromisoformat(start_at["$date"])

        cycle_length = self.cache.get("cycle_length")
        period_length = self.cache.get("period_length")

            # Keep adding cycle_length days until we pass the given date
        predicted_start = start_at
        while predicted_start <= date:
            predicted_start += timedelta(days=cycle_length)

        predicted_end = predicted_start + timedelta(days=period_length)
        # ovulation = predicted_start + relativedelta(months=1) - timedelta (days = self.cache.get ("ovulation_offset"))
        ovulation = predicted_start + timedelta(days=self.cache.get("ovulation_offset"))

        fertile_start = ovulation - timedelta(days=5)
        fertile_end = ovulation + timedelta(days=1)
        non_fertile_ranges = [
            (predicted_start, fertile_start - timedelta(days=1)),  # Before fertile window
            (fertile_end + timedelta(days=1), predicted_start + timedelta(days=cycle_length - 1))  # After fertile window
        ]


        return {
            "start_at": non_fertile_ranges[0][0].strftime("%d/%m/%Y"),
            "end_at": non_fertile_ranges[0][1].strftime("%d/%m/%Y"),
            "start_at_2": non_fertile_ranges[1][0].strftime("%d/%m/%Y"),
            "end_at_2": non_fertile_ranges[1][1].strftime("%d/%m/%Y"),
            "reminder": "During non-fertile days—the times outside your fertile window and menstruation—your chance of pregnancy is lower but not zero, especially if your cycle is irregular. It’s still important to maintain regular contraception if you want to avoid pregnancy. Use this time to focus on overall health: stay active, eat well, and manage stress. Keep tracking your cycle to better understand your body and prepare for upcoming fertile or period days.",
        }

    # get period days (in past months -> retrieve DB)
    def getPeriodRangeFromDB(self, date: datetime):
        """
        Retrieve actual recorded period ranges from MongoDB for a given past month.
        Used when user asks about 'last month', '2 months before', or specific past months.
        """

        start_of_month = datetime(date.year, date.month, 1)
        end_of_month = (start_of_month + relativedelta(months=1)) - timedelta(days=1)

        reports = list(self.databaseCon.db["user_reports"].find({
            "$or": [
                {
                    "start_at": {"$lte": end_of_month},
                    "end_at": {"$gte": start_of_month}
                }
            ]
        }).sort("start_at", DESCENDING))

        if not reports:
            next_report = self.databaseCon.db["user_reports"].find_one(
                {"start_at": {"$gt": end_of_month}},
                sort=[("start_at", 1)]
            )
            if next_report:
                next_start = next_report["start_at"]
                next_end = next_report.get("end_at", next_start + timedelta(days=self.cache.get("period_length", 5)))
                return {
                    "start_at": None,
                    "end_at": None,
                    "second_start_at": next_start.strftime("%d/%m/%Y"),
                    "second_end_at": next_end.strftime("%d/%m/%Y"),
                    "reminder": (
                        f"\n\nNo recorded period found for {calendar.month_name[date.month]} {date.year}. "
                        f"The next recorded period begins on {next_start.strftime('%d/%m/%Y')} "
                        f"and ends on {next_end.strftime('%d/%m/%Y')}."
                    )
                }
            return {
                "start_at": None,
                "end_at": None,
                "second_start_at": None,
                "second_end_at": None,
                "reminder": (
                    f"\n\nNo recorded period found for {calendar.month_name[date.month]} {date.year}. "
                    "You might not have logged any data for that time."
                )
            }

        results = []
        for r in reports:
            start_at = r["start_at"]
            end_at = r["end_at"]

            if isinstance(start_at, str):
                start_at = datetime.fromisoformat(start_at)
            if isinstance(end_at, str):
                end_at = datetime.fromisoformat(end_at)

            if start_at <= end_of_month and end_at >= start_of_month:
                results.append((start_at, end_at))

        if not results:
            return {
                "start_at": None,
                "end_at": None,
                "second_start_at": None,
                "second_end_at": None,
                "reminder": (
                    f"\n\nNo period recorded in {calendar.month_name[date.month]} {date.year}. "
                    "Try checking your recent months."
                )
            }

        primary = results[0]
        start_fmt = primary[0].strftime("%d/%m/%Y")
        end_fmt = primary[1].strftime("%d/%m/%Y")

        second_start_fmt = second_end_fmt = None
        if len(results) > 1:
            second_start_fmt = results[1][0].strftime("%d/%m/%Y")
            second_end_fmt = results[1][1].strftime("%d/%m/%Y")


        return {
            "start_at": start_fmt,
            "end_at": end_fmt,
            "second_start_at": second_start_fmt,
            "second_end_at": second_end_fmt,
            "reminder": (
                f"\n\nYour recorded period in {calendar.month_name[date.month]} {date.year} "
                f"was from {start_fmt} to {end_fmt}. "
                "Remember to keep logging your cycles for better tracking accuracy."
            )
        }

    # get period days (predicted)
    def getPeriodRangeByTime(self, date: datetime):
        latest_report = self.databaseCon.db["user_reports"].find_one(
                sort=[("start_at", DESCENDING)]
        )
        if not latest_report or "end_at" not in latest_report:
            return None

        start_at = latest_report["start_at"]
        if isinstance(start_at, str):
            start_at = datetime.strptime(start_at, "%Y-%m-%d")
        elif isinstance(start_at, dict) and "$date" in start_at:
            start_at = datetime.fromisoformat(start_at["$date"])

        cycle_length = self.cache.get("cycle_length")
        period_length = self.cache.get("period_length")

            # Keep adding cycle_length days until we pass the given date
        predicted_start = start_at
        while predicted_start <= date:
            predicted_start += timedelta(days=cycle_length)

        predicted_end = predicted_start + timedelta(days=period_length)

        asked_month = date.month
        asked_year = date.year

        if predicted_start.month != asked_month or predicted_start.year != asked_year:
            predicted_end = predicted_start + timedelta(days=period_length)
            return {
                "start_at": predicted_start.strftime("%d/%m/%Y"),
                "end_at": predicted_end.strftime("%d/%m/%Y"),
                "second_start_at": None,
                "second_end_at": None,
                "reminder": (
                    f"\n\nNo period is expected to start in {calendar.month_name[asked_month]} {asked_year}. "
                ),
            }
        
        if (predicted_start + timedelta (days=cycle_length) < date + relativedelta(months=1)):
            second_period = predicted_start + timedelta (days=cycle_length)
            second_period_end = second_period + timedelta(days=period_length)
            return {
                "start_at": predicted_start.strftime("%d/%m/%Y"),
                "end_at": predicted_end.strftime("%d/%m/%Y"),
                "second_start_at": second_period.strftime("%d/%m/%Y"),
                "second_end_at": second_period_end.strftime("%d/%m/%Y"),
                "reminder": "\n\nDuring your period, it's important to maintain good hygiene by changing sanitary products regularly to prevent infections. Stay hydrated, get enough rest, and manage any cramps or discomfort with gentle exercise, heat packs, or pain relief if needed. Eating balanced meals and avoiding excessive caffeine or salty foods can help reduce bloating and mood swings. While fertility is low during menstruation, remember that cycle lengths vary, so pregnancy is still possible if you have a short cycle. Listening to your body and practicing self-care during this time supports overall well-being.",
            }

        return {
                "start_at": predicted_start.strftime("%d/%m/%Y"),
                "end_at": predicted_end.strftime("%d/%m/%Y"),
                "second_start_at": None,
                "second_end_at": None,
                "reminder": "\n\nDuring your period, it's important to maintain good hygiene by changing sanitary products regularly to prevent infections. Stay hydrated, get enough rest, and manage any cramps or discomfort with gentle exercise, heat packs, or pain relief if needed. Eating balanced meals and avoiding excessive caffeine or salty foods can help reduce bloating and mood swings. While fertility is low during menstruation, remember that cycle lengths vary, so pregnancy is still possible if you have a short cycle. Listening to your body and practicing self-care during this time supports overall well-being.",
        }


    # get ovulation days (predicted)
    def getOvulationRangeByTime(self,date):
        latest_report = self.databaseCon.db["user_reports"].find_one(
                sort=[("start_at", DESCENDING)]
        )
        if not latest_report or "end_at" not in latest_report:
            return None

        start_at = latest_report["start_at"]
        if isinstance(start_at, str):
            start_at = datetime.strptime(start_at, "%Y-%m-%d")
        elif isinstance(start_at, dict) and "$date" in start_at:
            start_at = datetime.fromisoformat(start_at["$date"])

        cycle_length = self.cache.get("cycle_length")
        period_length = self.cache.get("period_length")

            # Keep adding cycle_length days until we pass the given date
        # ovupredict = start_at-timedelta(days = self.cache.get ("ovulation_offset"))
        ovupredict = start_at + timedelta(days = self.cache.get ("ovulation_offset"))
        while ovupredict <= date:
            ovupredict += timedelta(days=cycle_length)
        if (ovupredict + timedelta (days=cycle_length) < date + relativedelta(months=1)):
            second_ovulation = ovupredict+ timedelta(days=cycle_length)
            return {
                "ovulation_day": ovupredict.strftime("%d/%m/%Y"),
                "second_ovulation_day": second_ovulation.strftime("%d/%m/%Y"),
                "reminder": "During ovulation, your body releases an egg, making this the peak fertile day with the highest chance of conception. Pay attention to signs like increased cervical mucus, mild pelvic pain, or a slight rise in basal body temperature. If you’re trying to conceive, having intercourse on this day or the days leading up to it boosts your chances. If avoiding pregnancy, use reliable contraception, as ovulation is when you’re most likely to get pregnant. Staying hydrated and managing any discomfort can also help you feel your best during this time.",
            }


        return {
            "ovulation_day": ovupredict.strftime("%d/%m/%Y"),
            "second_ovulation_day": None,
            "reminder": "During ovulation, your body releases an egg, making this the peak fertile day with the highest chance of conception. Pay attention to signs like increased cervical mucus, mild pelvic pain, or a slight rise in basal body temperature. If you’re trying to conceive, having intercourse on this day or the days leading up to it boosts your chances. If avoiding pregnancy, use reliable contraception, as ovulation is when you’re most likely to get pregnant. Staying hydrated and managing any discomfort can also help you feel your best during this time.",
        }
    
    # get fertile days (predicted)
    def getFertileRangeByTime (self, date):
        latest_report = self.databaseCon.db["user_reports"].find_one(
                sort=[("start_at", DESCENDING)]
        )
        if not latest_report or "end_at" not in latest_report:
            return None

        start_at = latest_report["start_at"]
        if isinstance(start_at, str):
            start_at = datetime.strptime(start_at, "%Y-%m-%d")
        elif isinstance(start_at, dict) and "$date" in start_at:
            start_at = datetime.fromisoformat(start_at["$date"])

        cycle_length = self.cache.get("cycle_length")
        period_length = self.cache.get("period_length")
        predicted_start = start_at
        while predicted_start <= date:
            predicted_start += timedelta(days=cycle_length)
        ovulation_day = predicted_start -timedelta(days = self.cache.get ("ovulation_offset"))

        fertile_start = ovulation_day - timedelta(days=5)
        fertile_end = ovulation_day

        return {
            "start_at": fertile_start.strftime("%d/%m/%Y"),
            "end_at": fertile_end.strftime("%d/%m/%Y"),
            "reminder": "During fertile days, typically around ovulation, a woman is most likely to conceive. If trying to get pregnant, this is the best time for unprotected sex, supported by a healthy lifestyle and tracking signs like cervical mucus or ovulation kits. If avoiding pregnancy, it's crucial to use protection, as this window is the riskiest for unplanned conception. Understanding your cycle and being mindful of your goals helps you make informed reproductive choices.",
        }



