from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
import sys
import os
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from parserAnalyzer.CompiledFiles.FluLexer import FluLexer
from parserAnalyzer.CompiledFiles.FluParser import FluParser
from module.utilFunction import utilFunction
from module.ASTGeneration import ASTGeneration
class CustomErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.has_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Input rejected: {msg}")
        self.has_error = True
        # exit(1)  # Exit the program with an error

class Response():
    def __init__(self):
        self.astGeneration = ASTGeneration()
        self.err = CustomErrorListener()
        self.utilFunction = utilFunction()
        self.responses = {
            "hi": ["Hello! 💖", "Hey there! 🌸", "Hi! How can I help you today? 🤗"],
            "hello": ["Hi! 😄", "Hello! What's up? 🌟", "Hey, good to see you! 💕"],
            "how are you": [
                "I'm doing great, thanks! How are you feeling? 💖",
                "I'm here and ready to help! 🌸",
                "Awesome! How's your health today? 🤗",
            ],
            "bye": ["Goodbye! Take care! 👋💕", "See you later! Stay healthy! 😊🌸", "Bye! Remember to track your cycle! 💖"],
            "what is your name": [
                "I'm Luna, your period tracking assistant! 🌸💖",
                "Call me Luna! I'm here to help with your health! 💕",
                "I'm Luna, nice to meet you! 🤗🌸",
            ],
            "default": [
                "Tell me more about how you're feeling! 🤔💖",
                "I'm here to help with your period tracking! 🌸",
                "What would you like to know about your health? 💕",
            ],
        }
    
    # check for simple keyword matching first
    def get_simple_response(self, user_message):
        user_message = user_message.lower().strip()
        
        for key in self.responses:
            if key in user_message:
                return random.choice(self.responses[key])
        
        return None
    
    # if input user is incorrect, return a random default response
    def get_default_response(self):
        return random.choice(self.responses["default"])
    
    def checkError(self, user_str):
        # try simple response matching
        simple_response = self.get_simple_response(user_str)
        if simple_response:
            return simple_response
        
        # if no simple match, try with ANTLR parsing for correct format
        input_stream = InputStream(user_str) 
        lexer = FluLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = FluParser(stream) 
        parser.removeErrorListeners()
        parser.addErrorListener(self.err)    
        tree = parser.program() 

        if (self.err.has_error):
            self.err.has_error = False
            # return "Wrong input format, please input again"
            return self.get_default_response()
        else:
            return tree.accept (self.astGeneration)
            # return self.classifySentence(tree, parser)
        