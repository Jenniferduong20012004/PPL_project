# Generated from F:\\PPL\\PPL_Project\\parserAnalyzer\\Flu.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FluParser import FluParser
else:
    from FluParser import FluParser

# This class defines a complete generic visitor for a parse tree produced by FluParser.

class FluVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FluParser#program.
    def visitProgram(self, ctx:FluParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#sentence.
    def visitSentence(self, ctx:FluParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#require.
    def visitRequire(self, ctx:FluParser.RequireContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#ask.
    def visitAsk(self, ctx:FluParser.AskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#verb.
    def visitVerb(self, ctx:FluParser.VerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#phrase.
    def visitPhrase(self, ctx:FluParser.PhraseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#cycleStatus.
    def visitCycleStatus(self, ctx:FluParser.CycleStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#specificPharse.
    def visitSpecificPharse(self, ctx:FluParser.SpecificPharseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#date.
    def visitDate(self, ctx:FluParser.DateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#dateInNum.
    def visitDateInNum(self, ctx:FluParser.DateInNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#dateInWord.
    def visitDateInWord(self, ctx:FluParser.DateInWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#dateCompare.
    def visitDateCompare(self, ctx:FluParser.DateCompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#dateMonth.
    def visitDateMonth(self, ctx:FluParser.DateMonthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#monthWord.
    def visitMonthWord(self, ctx:FluParser.MonthWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FluParser#monthCompare.
    def visitMonthCompare(self, ctx:FluParser.MonthCompareContext):
        return self.visitChildren(ctx)



del FluParser