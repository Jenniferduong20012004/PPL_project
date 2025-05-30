import calendar
from module.Database import Database
from datetime import datetime, timedelta
from module.UserReport import UserReport
from pymongo import DESCENDING
from dateutil.relativedelta import relativedelta
import diskcache as dc



class utilFunction:
    
    def __init__(self):
        self.databaseCon = Database()
        self.cache = dc.Cache('./mycache')
        self.cycle_length = 29
        self.period_length = 5
        self.fertile_start_offset = 10
        self.fertile_end_offset = 16
        self.ovulation_offset = 14
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
                "reminder":f"You are currently in your period. {result} are common period symptoms, usually linked to PMS or primary dysmenorrhea. They’re caused by hormonal shifts, uterine contractions, and prostaglandins. If symptoms are severe, disrupt daily life, don’t improve with medication, or suddenly worsen, it may signal a condition like endometriosis or fibroids—see a doctor."
            }
        else:
            return {
                "reminder": f"You are currently not in your period. If you're experiencing {result} now, it could be due to other causes such as ovulation, stress, digestive issues, or underlying conditions like IBS, hormonal imbalance, or infections. If these symptoms are frequent, severe, or unusual for you, it's best to consult a healthcare provider for proper evaluation."
            }

    def checkStatistic(self):
        cycle_length = self.cache.get("cycle_length")
        period_length = self.cache.get("period_length")
        cycleNormal = True
        periodNormal = True
        if (cycle_length <21 or cycle_length > 35):
            cycleNormal = False
        if (period_length < 2 or period_length > 7):
            periodNormal = False
        reminder = None
        if (cycleNormal and periodNormal):
            reminder = "Your cycle falls within the normal range. A typical menstrual cycle lasts 21 to 35 days, with periods lasting 2 to 7 days. While most people have a 28-day cycle and bleed for 3 to 5 days, slight variations are perfectly normal."
        elif (cycleNormal and not periodNormal):
            if (periodNormal > 7):
                reminder = "Your cycle is normal, but bleeding for over 7 days may indicate menorrhagia. This could be due to hormonal imbalances, fibroids, or other conditions. If your period consistently lasts 10 days or involves heavy bleeding, clots, or fatigue, consider seeing a healthcare provider."
            else:
                reminder = "Your cycle is normal, but your period is shorter than usual. Occasional short periods can result from stress, hormones, puberty, or birth control. If it’s consistent or unusually light, it could signal hormonal imbalance, spotting, or thyroid issues. One-time changes aren't usually a concern, but see a healthcare provider if it continues."
        elif (not cycleNormal and periodNormal):
            if (cycleNormal <21):
                reminder = "Your period is normal, but a cycle shorter than 21 days may indicate polymenorrhea, meaning more frequent bleeding. Causes include hormonal imbalances, perimenopause, thyroid issues, stress, intense exercise, or low body weight. Occasional short cycles may be harmless, but if consistent, see a healthcare provider for evaluation."
            else:
                reminder = "Your period is normal, but a cycle longer than 35 days may indicate oligomenorrhea, or infrequent periods. Causes include PCOS, hormonal or thyroid issues, stress, weight changes, or perimenopause. Occasional delays may be lifestyle-related, but frequent irregular cycles should be checked by a healthcare provider."
        else:
            reminder = "Both your cycle length and period duration fall outside the normal range. A typical cycle is 21–35 days with bleeding lasting 2–7 days. While some variation is normal, consistently irregular or unpredictable periods should be evaluated by a healthcare provider."
        return {
            "cycle_length": cycle_length,
            "period_length": period_length,
            "reminder": reminder
        }
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
            if isinstance(start, str):
                start = datetime.fromisoformat(start)
            if isinstance(end, str):
                end = datetime.fromisoformat(end)
            diff_days = (end.date() - start.date()).days
            durations.append(diff_days)

        mean_duration = sum(durations) / len(durations) if durations else 5
        self.cache['period_length'] = mean_duration  # Store
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

        mean_start_diff = sum(start_diffs) / len(start_diffs) if start_diffs else 29
        self.cache['cycle_length'] = mean_start_diff  # Store
        # Ovulation usually happens 14 days before the next period
        ovulation_offset = mean_start_diff - 14   # days after period starts

        # Fertile window is 5-6 days ending on ovulation day
        fertile_start_offset = ovulation_offset - 5  # 5 days before ovulation
        fertile_end_offset = ovulation_offset        # ends at ovulation day

        self.cache['ovulation_offset'] = ovulation_offset 
        self.cache['fertile_start_offset'] = fertile_start_offset
        self.cache['fertile_end_offset']= fertile_end_offset

        
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

    def getPeriodCycle(self):
        return list(
            self.databaseCon.db["user_reports"]
            .find()
            .sort("start_at", DESCENDING)
            .limit(3)
        )


    def requireStart(self, date):
        user_report = UserReport(
            start_at=date, end_at=date + timedelta(days=self.cache.get('period_length'))
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

            # Keep adding cycle_length days until we pass the given date
        predicted_start = start_at
        while predicted_start <= date:
            predicted_start += timedelta(days=cycle_length)

        predicted_end = predicted_start + timedelta(days=period_length)
        ovulation = predicted_start + relativedelta(months=1) - timedelta (days = self.cache.get ("ovulation_offset"))
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

    def getPeriodRangeByTime(self, date: datetime):
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

            # Keep adding cycle_length days until we pass the given date
        predicted_start = start_at
        while predicted_start <= date:
            predicted_start += timedelta(days=cycle_length)

        predicted_end = predicted_start + timedelta(days=period_length)
        if (predicted_start + timedelta (days=cycle_length) < date + relativedelta(months=1)):
            second_period = predicted_start + timedelta (days=cycle_length)
            second_period_end = second_period + timedelta(days=period_length)
            return {
                "start_at": predicted_start.strftime("%d/%m/%Y"),
                "end_at": predicted_end.strftime("%d/%m/%Y"),
                "second_start_at": second_period.strftime("%d/%m/%Y"),
                "second_end_at": second_period_end.strftime("%d/%m/%Y"),
                "reminder": "During your period, it's important to maintain good hygiene by changing sanitary products regularly to prevent infections. Stay hydrated, get enough rest, and manage any cramps or discomfort with gentle exercise, heat packs, or pain relief if needed. Eating balanced meals and avoiding excessive caffeine or salty foods can help reduce bloating and mood swings. While fertility is low during menstruation, remember that cycle lengths vary, so pregnancy is still possible if you have a short cycle. Listening to your body and practicing self-care during this time supports overall well-being.",
            }

        return {
                "start_at": predicted_start.strftime("%d/%m/%Y"),
                "end_at": predicted_end.strftime("%d/%m/%Y"),
                "second_start_at": None,
                "second_end_at": None,
                "reminder": "During your period, it's important to maintain good hygiene by changing sanitary products regularly to prevent infections. Stay hydrated, get enough rest, and manage any cramps or discomfort with gentle exercise, heat packs, or pain relief if needed. Eating balanced meals and avoiding excessive caffeine or salty foods can help reduce bloating and mood swings. While fertility is low during menstruation, remember that cycle lengths vary, so pregnancy is still possible if you have a short cycle. Listening to your body and practicing self-care during this time supports overall well-being.",
        }


    
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
        ovupredict = start_at-timedelta(days = self.cache.get ("ovulation_offset"))
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



