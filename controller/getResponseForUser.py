import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from module.Response import Response


class getResponseForUser:
    def __init__(self):
        self.response = Response()

    def getResponse(self, user_str):
        response = self.response.checkError(user_str)
        return response
