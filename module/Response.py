from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from parserAnalyzer.CompiledFiles.TreeToArrayVisitor import TreeToArrayVisitor
from parserAnalyzer.CompiledFiles.FluLexer import FluLexer
from parserAnalyzer.CompiledFiles.FluParser import FluParser

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.has_error = False
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Input rejected: {msg}")
        self.has_error = True
        # exit(1)  # Exit the program with an error
class Response():
    def __init__ (self):
        self.helper = TreeToArrayVisitor()
        self.err = CustomErrorListener()
    def checkError (self, user_str):
        input_stream = InputStream(user_str) 
        lexer = FluLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = FluParser(stream) 
        parser.removeErrorListeners()
        parser.addErrorListener(self.err)    
        tree = parser.program() 
        if (self.err.has_error):
            self.err.has_error = False
            return "Wrong input format, please input again"
        else:
            self.classifySentence(tree, parser)
    def classifySentence (self, tree, parser):
        visitor = TreeToArrayVisitor()
        result_string =tree.toStringTree(recog=parser)
        res = visitor.getRequirementFromUser(result_string)
        requireOrAsk = res[0][0]
        if (requireOrAsk == 'ask'):
            self.ask (res)
        elif (requireOrAsk =='verb'):
            self.getRequirement (res)
    def getRequirement (self, res):
        verb = res[0][1].lower()
        if (verb == 'start'):
            print ('a')
        elif (verb =='show'):
            print ('s')
        elif (verb == 'end'):
            print ('e')
    def ask (self, res):
        specificPhraseOrCycleStatus = res[1][0]
        if (specificPhraseOrCycleStatus == 'cycleStatus'):
            print ("cyc")
        #    implement for get question  what is the cycle status on 01-04-2025?
        else: 
            specificPhrase = res[1][1].lower().split()[0]
            if (specificPhrase== 'period'):
                print (res)
            elif (specificPhrase =='ovulation'):
                print ("ovu")
            elif (specificPhrase == 'fertile'):
                print ("fertule")
            elif (specificPhrase =='non-fertile'):
                print ('non-fer')

def main():
    user_input = input("Enter your sentence: ")
    responder = Response()
    success = responder.checkError(user_input)

if __name__ == '__main__':
    main()