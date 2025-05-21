from datetime import datetime
from module.Database import db


class Parser:
    def __init__(self):
        self.db = db
    
    def parse_data(self, data):
        """
        Phân tích dữ liệu
        
        Args:
            data (dict): Dữ liệu cần phân tích
            
        Returns:
            dict: Dữ liệu đã được phân tích
        """
        # Logic phân tích dữ liệu của bạn
        parsed_data = {
            "parsed_at": datetime.now(),
            "original_data": data,
            # Thêm các trường phân tích khác
        }
        
        return parsed_data
    
    def save_parsed_data(self, user_id, parsed_data):
        """
        Lưu dữ liệu đã phân tích
        
        Args:
            user_id (str): ID của người dùng
            parsed_data (dict): Dữ liệu đã phân tích
            
        Returns:
            str: ID của document hoặc None nếu thất bại
        """
        parsed_data["user_id"] = user_id
        return self.db.save_data("parsed_data", parsed_data)