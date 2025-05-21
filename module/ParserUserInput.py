from antlr4 import *
from PPL_project.parserAnalyzer.CompiledFiles.FluLexer import FluLexer
from PPL_project.parserAnalyzer.CompiledFiles.FluParser import FluParser
from antlr4.error.ErrorListener import ErrorListener

class Parser:
    def parse_input(self, input):   
        input_stream = FileStream(input)
        lexer = FluLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = FluParser(stream)
        tree = parser.program() 
        token_stream = CommonTokenStream(lexer)
        parser = FluParser(token_stream)   
        parser.removeErrorListeners()
       
    
    