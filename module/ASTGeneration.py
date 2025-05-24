import sys
import os
from functools import reduce
from datetime import datetime, timedelta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from module.ASTutils import *
from parserAnalyzer.CompiledFiles.TreeToArrayVisitor import TreeToArrayVisitor
from parserAnalyzer.CompiledFiles.FluLexer import FluLexer
from parserAnalyzer.CompiledFiles.FluParser import FluParser
from parserAnalyzer.CompiledFiles.FluVisitor import FluVisitor
from module.utilFunction import utilFunction
class ASTGeneration (FluVisitor):
    def visitProgram (self, ctx: FluParser.ProgramContext):
        return ctx.sentence().accept(self)
    def visitSentence(self, ctx: FluParser.SentenceContext):
        if ctx.ask():
            return ctx.ask().accept(self)
        elif ctx.require():
            return ctx.require().accept(self)
        
    def visitAsk (self, ctx: FluParser.AskContext):
        if ctx.cycleStatus():
            return CycleStatusOp(ctx.cycleStatus.accept (self))
        elif ctx.specificPharse():
            return
    def visitStatus (self, ctx: FluParser.CycleStatusContext ):
        return ctx.date().accept(self)
    def visitRequire (self, ctx: FluParser.RequireContext):
        return RequireOp (ctx.verb().accept(self), ctx.date().accept(self))
    def visitVerb (self, ctx: FluParser.VerbContext):
        if ctx.START():
            return "start"
        elif ctx.END():
            return "end"
        elif ctx.SHOW():
            return "show"
    def visitDate(self, ctx:FluParser.DateContext):
        if ctx.dateCompare():
            return self.visitDateCompare(ctx.dateCompare())
        elif ctx.dateInNum():
            return self.visitDateInNum(ctx.dateInNum())
        elif ctx.dateInWord():
            return self.visitDateInWord(ctx.dateInWord())
    def visitDateInNum (self, ctx:FluParser.DateInNumContext):
        day = int(ctx.NUMBER(0).getText())
        month = int(ctx.NUMBER(1).getText())
        year = int(ctx.NUMBER(2).getText())
        return datetime(year, month, day)
    def visitDateCompare(self, ctx:FluParser.DateCompareContext):
        beforeAfter = ctx.BeforeAfter().getText().lower()
        now = datetime.today()
        if (beforeAfter == 'before'):
            now = now - timedelta(int(ctx.NUMBER()))
        elif (beforeAfter == 'after'):
            now = now + timedelta(int(ctx.NUMBER()))
        return now
    def visitDateInWord (self, ctx: FluParser.DateInWordContext):
        time = ctx.getText()
        now = datetime.today()
        if (time == 'yesterday'):
            now = now - timedelta(1)
        elif (time == 'today'):
            now = now + timedelta(1)
        return now

        
        
