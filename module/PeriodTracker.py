from datetime import datetime, timedelta
import calendar
from module.Database import DatabaseConnector

class PeriodTracker:
    def __init__(self):
        self.db = DatabaseConnector()
        # Default user ID (in a real app, you'd have user authentication)
        self.user_id = "default_user"
    
    def set_user(self, user_id):
        """Set the current user ID"""
        self.user_id = user_id