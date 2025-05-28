from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from module.Database import Database


class UserReport:
    def __init__(
        self,
        _id: Optional[str] = None,
        start_at: Optional[datetime] = None,
        end_at: Optional[datetime] = None,
    ):
        self.id = _id or ObjectId()
        self.start_at = start_at
        self.end_at = end_at

    def to_dict(self):
        return {
            "_id": self.id,
            "start_at": self.start_at,
            "end_at": self.end_at,
        }

    def save_to_db(self):
        db_instance = Database()
        result_id = db_instance.save_data("user_reports", self.to_dict())
        if result_id:
            print(f"User report saved with ID: {result_id}")
        else:
            print("Failed to save user report.")
        return result_id
