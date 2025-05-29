import sys
import os
from functools import reduce
from datetime import datetime, timedelta

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from module.ASTutils import *
from parserAnalyzer.CompiledFiles.FluLexer import FluLexer
from parserAnalyzer.CompiledFiles.FluParser import FluParser
from parserAnalyzer.CompiledFiles.FluVisitor import FluVisitor
from dateutil.relativedelta import relativedelta


class ASTGeneration(FluVisitor):
    def visitProgram(self, ctx: FluParser.ProgramContext):
        return ctx.sentence().accept(self)

    def visitSentence(self, ctx: FluParser.SentenceContext):
        if ctx.ask():
            return ctx.ask().accept(self)
        elif ctx.require():
            return ctx.require().accept(self)

    def visitAsk(self, ctx: FluParser.AskContext):
        if ctx.cycleStatus():
            return ctx.cycleStatus().accept(self)
        elif ctx.specificPharse():
            return ctx.specificPharse().accept(self)

    def visitSpecificPharse(self, ctx: FluParser.SpecificPharseContext):
        phrase = None
        if ctx.OVU():
            phrase = "ovulation"
        elif ctx.FER():
            phrase = "fertile"
        elif ctx.PER():
            phrase = "period"
        elif ctx.NONF():
            phrase = "non-fertile"
        date = ctx.dateMonth().accept(self)
        specific = SpecificPhraseOp(phrase, date)
        specific.action()
        return specific.to_dict()

    def visitDateMonth(self, ctx: FluParser.DateMonthContext):
        if ctx.monthCompare():
            return ctx.monthCompare().accept(self)
        elif ctx.monthWord():
            return ctx.monthWord().accept(self)

    def visitMonthWord(self, ctx: FluParser.MonthWordContext):
        month = ctx.WHEN().getText().lower
        now = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        if month == "previous":
            now = now - relativedelta(months=1)
        elif month == "next":
            now = now + relativedelta(months=1)
        print (now)
        return now

    def visitMonthCompare(self, ctx: FluParser.MonthCompareContext):
        beforeAfter = ctx.BeforeAfter().getText().lower()
        print(beforeAfter)
        now = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        number_of_months = int(ctx.NUMBER().getText())
        if beforeAfter == "before":
            now = now - relativedelta(months=number_of_months)
        elif beforeAfter == "later":
            now = now + relativedelta(months=number_of_months)
        return now

    def visitCycleStatus(self, ctx: FluParser.CycleStatusContext):
        date = ctx.date().accept(self) if ctx.date() else None
        cycOp = CycleStatusOp(date)
        cycOp.action()
        return cycOp.to_dict()

    def visitStatus(self, ctx: FluParser.CycleStatusContext):
        return ctx.date().accept(self)

    def visitRequire(self, ctx: FluParser.RequireContext):
        verb = ctx.verb().accept(self)
        date = ctx.date().accept(self) if ctx.date() else None
        require = RequireOp(verb, date)
        require.action()
        result = require.to_dict()
        return result

    def visitVerb(self, ctx: FluParser.VerbContext):
        if ctx.START():
            return "start"
        elif ctx.END():
            return "end"
        elif ctx.SHOW():
            return "show"

    def visitDate(self, ctx: FluParser.DateContext):
        if ctx.dateCompare():
            return ctx.dateCompare().accept(self)
        elif ctx.dateInNum():
            return ctx.dateInNum().accept(self)
        elif ctx.dateInWord():
            return ctx.dateInWord().accept(self)

    def visitDateInNum(self, ctx: FluParser.DateInNumContext):
        day = int(ctx.NUMBER(0).getText())
        month = int(ctx.NUMBER(1).getText())
        year = int(ctx.NUMBER(2).getText())
        return datetime(year, month, day)

    def visitDateCompare(self, ctx: FluParser.DateCompareContext):
        beforeAfter = ctx.BeforeAfter().getText().lower()
        now = datetime.today()
        if beforeAfter == "before":
            now = now - timedelta(int(ctx.NUMBER().getText()))
        elif beforeAfter == "later":
            now = now + timedelta(int(ctx.NUMBER().getText()))
        return now

    def visitDateInWord(self, ctx: FluParser.DateInWordContext):
        time = ctx.getText()
        now = datetime.today()
        if time == "yesterday":
            now = now - timedelta(1)
        elif time == "tomorrow":
            now = now + timedelta(1)
        return now 
