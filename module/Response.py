from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
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


class Response:
    def __init__(self):
        self.astGeneration = ASTGeneration()
        self.err = CustomErrorListener()
        self.utilFunction = utilFunction()
        # fallback response: random responses for fallback when parsing fails
        self.fallback_responses = [
            "Tell me more about how you're feeling! 🤔💖",
            "I'm here to help with your period tracking! 🌸",
            "What would you like to know about your health? 💕",
            "I can help you track your cycle, symptoms, and health! 💗",
            "Feel free to ask me about your menstrual cycle! 🌙",
            "How can I assist you with your health tracking today? 🤗",
            "I'm Luna, your period tracking companion! What's on your mind? 💖",
        ]

    def get_fallback_response(self):
        return random.choice(self.fallback_responses)

    def checkError(self, user_str):
        self.err.has_error = False
        
        # process input through ANTLR parser
        input_stream = InputStream(user_str)
        lexer = FluLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = FluParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(self.err)
        tree = parser.program()

        if self.err.has_error:
            # if parsing failed, return random fallback response
            return self.get_fallback_response()
        else:
            # if parsing succeeded, generate AST and execute operations
            result = tree.accept(self.astGeneration)
            return result