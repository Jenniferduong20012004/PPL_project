from typing import List, Optional
from bson import ObjectId
from Database import Database


class SymptomCategory:
    def __init__(
        self,
        name: str,
        description: str,
        time_duration: int,
        expected_next_period: int,
        is_in_the_period: bool,
        symptom_keywords: List[str],
        _id: Optional[str] = None,
    ):
        self.id = _id or str(ObjectId())
        self.name = name
        self.description = description
        self.time_duration = time_duration
        self.expected_next_period = expected_next_period
        self.is_in_the_period = is_in_the_period
        self.symptom_keywords = symptom_keywords or []

    def to_dict(self):
        return {
            "_id": self.id,
            "name": self.name,
            "description": self.description,
            "time_duration": self.time_duration,
            "expected_next_period": self.expected_next_period,
            "is_in_the_period": self.is_in_the_period,
            "symptom_keywords": self.symptom_keywords,
        }

    def save_to_db(self):
        db_instance = Database()
        result_id = db_instance.save_data("symptom_categories", self.to_dict())
        if result_id:
            print(f"Symptom category saved with ID: {result_id}")
        else:
            print("Failed to save symptom category.")
        return result_id

    @staticmethod
    def save_many_to_db(categories: List["SymptomCategory"]):
        db_instance = Database()
        docs = [cat.to_dict() for cat in categories]
        result_ids = db_instance.save_many("symptom_categories", docs)
        if result_ids:
            print(f"{len(result_ids)} symptom categories saved.")
        else:
            print("Failed to save symptom categories.")
        return result_ids


if __name__ == "__main__":
    categories = [
        SymptomCategory(
            name="Menstrual Phase",
            description="The menstrual phase is the first stage of the menstrual cycle. It begins when the uterus sheds its lining, resulting in menstrual bleeding. This phase typically lasts 5 to 7 days and may be accompanied by symptoms such as cramps, fatigue, and mood changes.",
            time_duration=5,
            expected_next_period=23,
            is_in_the_period=True,
            symptom_keywords=[
                "lower abdominal pain",
                "fatigue",
                "back pain",
                "mild nausea",
                "breast tenderness",
                "irritable mood",
                "menstrual bleeding",
            ],
        ),
        SymptomCategory(
            name="Ovulation Phase",
            description="The ovulation phase is the stage in the menstrual cycle when a mature egg is released from the ovary. It typically occurs around the middle of the cycle (day 14 in a 28-day cycle). This is the most fertile period, and symptoms may include a slight rise in body temperature, increased cervical mucus, and mild pelvic pain.",
            time_duration=8,
            expected_next_period=15,
            is_in_the_period=False,
            symptom_keywords=[
                "increased vaginal discharge",
                "mild pain on one side of the abdomen",
                "increased libido",
                "slight rise in body temperature",
                "breast tenderness",
            ],
        ),
        SymptomCategory(
            name="Luteal Phase",
            description="The luteal phase occurs after ovulation and prepares the uterus for pregnancy. It lasts about 14 days and may cause symptoms like breast tenderness, bloating, and mood changes.",
            time_duration=15,
            expected_next_period=0,
            is_in_the_period=False,
            symptom_keywords=[
                "headache",
                "acne",
                "mood swings",
                "bloating",
                "food cravings (especially sweets)",
                "fatigue",
                "insomnia",
                "breast pain",
            ],
        ),
    ]

    SymptomCategory.save_many_to_db(categories)
