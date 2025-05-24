# Generated from D:\PPL_prj\PPL_project\parserAnalyzer\Flu.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("o\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\5\3%\n\3\3\4\3")
        buf.write("\4\5\4)\n\4\3\4\5\4,\n\4\3\4\5\4/\n\4\3\5\3\5\5\5\63\n")
        buf.write("\5\3\5\5\5\66\n\5\3\5\3\5\5\5:\n\5\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\5\bF\n\b\3\b\3\b\3\t\3\t\5\tL\n\t")
        buf.write("\3\t\5\tO\n\t\3\t\3\t\3\n\3\n\3\n\5\nV\n\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\5")
        buf.write("\16f\n\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\2\2")
        buf.write("\21\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36\2\6\3\2\34")
        buf.write("\35\3\2\31\33\3\2\24\27\3\2\3\5\2l\2 \3\2\2\2\4$\3\2\2")
        buf.write("\2\6&\3\2\2\2\b\60\3\2\2\2\n=\3\2\2\2\f?\3\2\2\2\16B\3")
        buf.write("\2\2\2\20I\3\2\2\2\22U\3\2\2\2\24W\3\2\2\2\26]\3\2\2\2")
        buf.write("\30_\3\2\2\2\32e\3\2\2\2\34g\3\2\2\2\36j\3\2\2\2 !\5\4")
        buf.write("\3\2!\3\3\2\2\2\"%\5\6\4\2#%\5\b\5\2$\"\3\2\2\2$#\3\2")
        buf.write("\2\2%\5\3\2\2\2&(\5\n\6\2\')\5\f\7\2(\'\3\2\2\2()\3\2")
        buf.write("\2\2)+\3\2\2\2*,\t\2\2\2+*\3\2\2\2+,\3\2\2\2,.\3\2\2\2")
        buf.write("-/\5\22\n\2.-\3\2\2\2./\3\2\2\2/\7\3\2\2\2\60\62\7\6\2")
        buf.write("\2\61\63\7\b\2\2\62\61\3\2\2\2\62\63\3\2\2\2\63\65\3\2")
        buf.write("\2\2\64\66\7\7\2\2\65\64\3\2\2\2\65\66\3\2\2\2\669\3\2")
        buf.write("\2\2\67:\5\16\b\28:\5\20\t\29\67\3\2\2\298\3\2\2\2:;\3")
        buf.write("\2\2\2;<\7\23\2\2<\t\3\2\2\2=>\t\3\2\2>\13\3\2\2\2?@\t")
        buf.write("\4\2\2@A\7\30\2\2A\r\3\2\2\2BC\7\30\2\2CE\7\13\2\2DF\t")
        buf.write("\2\2\2ED\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\5\22\n\2H\17\3")
        buf.write("\2\2\2IK\t\4\2\2JL\7\22\2\2KJ\3\2\2\2KL\3\2\2\2LN\3\2")
        buf.write("\2\2MO\t\2\2\2NM\3\2\2\2NO\3\2\2\2OP\3\2\2\2PQ\5\32\16")
        buf.write("\2Q\21\3\2\2\2RV\5\30\r\2SV\5\24\13\2TV\5\26\f\2UR\3\2")
        buf.write("\2\2US\3\2\2\2UT\3\2\2\2V\23\3\2\2\2WX\7\20\2\2XY\7\17")
        buf.write("\2\2YZ\7\20\2\2Z[\7\17\2\2[\\\7\20\2\2\\\25\3\2\2\2]^")
        buf.write("\t\5\2\2^\27\3\2\2\2_`\7\20\2\2`a\7\22\2\2ab\7\f\2\2b")
        buf.write("\31\3\2\2\2cf\5\34\17\2df\5\36\20\2ec\3\2\2\2ed\3\2\2")
        buf.write("\2f\33\3\2\2\2gh\7\36\2\2hi\7\21\2\2i\35\3\2\2\2jk\7\20")
        buf.write("\2\2kl\7\21\2\2lm\7\f\2\2m\37\3\2\2\2\16$(+.\62\659EK")
        buf.write("NUe")
        return buf.getvalue()


class FluParser ( Parser ):

    grammarFileName = "Flu.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'tomorrow'", "'today'", "'yesterday'", 
                     "<INVALID>", "<INVALID>", "'is'", "'the'", "'my'", 
                     "'status'", "<INVALID>", "'before'", "'later'", "'-'", 
                     "<INVALID>", "<INVALID>", "'days'", "'?'", "'period'", 
                     "'ovulation'", "'fertile'", "'non-fertile'", "'cycle'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'on'", "'in'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WHAT", "TM", "IS", "THE", "MY", "STATUS", "BeforeAfter", 
                      "BEFORE", "AFTER", "SLASH", "NUMBER", "MO", "DAYS", 
                      "QUESTIONMARK", "PER", "OVU", "FER", "NONF", "CYCLE", 
                      "START", "END", "SHOW", "ON", "IN", "WHEN", "WORD", 
                      "WS" ]

    RULE_program = 0
    RULE_sentence = 1
    RULE_require = 2
    RULE_ask = 3
    RULE_verb = 4
    RULE_phrase = 5
    RULE_cycleStatus = 6
    RULE_specificPharse = 7
    RULE_date = 8
    RULE_dateInNum = 9
    RULE_dateInWord = 10
    RULE_dateCompare = 11
    RULE_dateMonth = 12
    RULE_monthWord = 13
    RULE_monthCompare = 14

    ruleNames =  [ "program", "sentence", "require", "ask", "verb", "phrase", 
                   "cycleStatus", "specificPharse", "date", "dateInNum", 
                   "dateInWord", "dateCompare", "dateMonth", "monthWord", 
                   "monthCompare" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WHAT=4
    TM=5
    IS=6
    THE=7
    MY=8
    STATUS=9
    BeforeAfter=10
    BEFORE=11
    AFTER=12
    SLASH=13
    NUMBER=14
    MO=15
    DAYS=16
    QUESTIONMARK=17
    PER=18
    OVU=19
    FER=20
    NONF=21
    CYCLE=22
    START=23
    END=24
    SHOW=25
    ON=26
    IN=27
    WHEN=28
    WORD=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentence(self):
            return self.getTypedRuleContext(FluParser.SentenceContext,0)


        def getRuleIndex(self):
            return FluParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = FluParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.sentence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def require(self):
            return self.getTypedRuleContext(FluParser.RequireContext,0)


        def ask(self):
            return self.getTypedRuleContext(FluParser.AskContext,0)


        def getRuleIndex(self):
            return FluParser.RULE_sentence

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentence" ):
                return visitor.visitSentence(self)
            else:
                return visitor.visitChildren(self)




    def sentence(self):

        localctx = FluParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FluParser.START, FluParser.END, FluParser.SHOW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.require()
                pass
            elif token in [FluParser.WHAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.ask()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RequireContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def verb(self):
            return self.getTypedRuleContext(FluParser.VerbContext,0)


        def phrase(self):
            return self.getTypedRuleContext(FluParser.PhraseContext,0)


        def date(self):
            return self.getTypedRuleContext(FluParser.DateContext,0)


        def ON(self):
            return self.getToken(FluParser.ON, 0)

        def IN(self):
            return self.getToken(FluParser.IN, 0)

        def getRuleIndex(self):
            return FluParser.RULE_require

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequire" ):
                return visitor.visitRequire(self)
            else:
                return visitor.visitChildren(self)




    def require(self):

        localctx = FluParser.RequireContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_require)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.verb()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FluParser.PER) | (1 << FluParser.OVU) | (1 << FluParser.FER) | (1 << FluParser.NONF))) != 0):
                self.state = 37
                self.phrase()


            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FluParser.ON or _la==FluParser.IN:
                self.state = 40
                _la = self._input.LA(1)
                if not(_la==FluParser.ON or _la==FluParser.IN):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FluParser.T__0) | (1 << FluParser.T__1) | (1 << FluParser.T__2) | (1 << FluParser.NUMBER))) != 0):
                self.state = 43
                self.date()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AskContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHAT(self):
            return self.getToken(FluParser.WHAT, 0)

        def QUESTIONMARK(self):
            return self.getToken(FluParser.QUESTIONMARK, 0)

        def cycleStatus(self):
            return self.getTypedRuleContext(FluParser.CycleStatusContext,0)


        def specificPharse(self):
            return self.getTypedRuleContext(FluParser.SpecificPharseContext,0)


        def IS(self):
            return self.getToken(FluParser.IS, 0)

        def TM(self):
            return self.getToken(FluParser.TM, 0)

        def getRuleIndex(self):
            return FluParser.RULE_ask

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsk" ):
                return visitor.visitAsk(self)
            else:
                return visitor.visitChildren(self)




    def ask(self):

        localctx = FluParser.AskContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ask)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(FluParser.WHAT)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FluParser.IS:
                self.state = 47
                self.match(FluParser.IS)


            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FluParser.TM:
                self.state = 50
                self.match(FluParser.TM)


            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FluParser.CYCLE]:
                self.state = 53
                self.cycleStatus()
                pass
            elif token in [FluParser.PER, FluParser.OVU, FluParser.FER, FluParser.NONF]:
                self.state = 54
                self.specificPharse()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 57
            self.match(FluParser.QUESTIONMARK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(FluParser.START, 0)

        def END(self):
            return self.getToken(FluParser.END, 0)

        def SHOW(self):
            return self.getToken(FluParser.SHOW, 0)

        def getRuleIndex(self):
            return FluParser.RULE_verb

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVerb" ):
                return visitor.visitVerb(self)
            else:
                return visitor.visitChildren(self)




    def verb(self):

        localctx = FluParser.VerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_verb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FluParser.START) | (1 << FluParser.END) | (1 << FluParser.SHOW))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PhraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CYCLE(self):
            return self.getToken(FluParser.CYCLE, 0)

        def OVU(self):
            return self.getToken(FluParser.OVU, 0)

        def PER(self):
            return self.getToken(FluParser.PER, 0)

        def FER(self):
            return self.getToken(FluParser.FER, 0)

        def NONF(self):
            return self.getToken(FluParser.NONF, 0)

        def getRuleIndex(self):
            return FluParser.RULE_phrase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPhrase" ):
                return visitor.visitPhrase(self)
            else:
                return visitor.visitChildren(self)




    def phrase(self):

        localctx = FluParser.PhraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_phrase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FluParser.PER) | (1 << FluParser.OVU) | (1 << FluParser.FER) | (1 << FluParser.NONF))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 62
            self.match(FluParser.CYCLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleStatusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CYCLE(self):
            return self.getToken(FluParser.CYCLE, 0)

        def STATUS(self):
            return self.getToken(FluParser.STATUS, 0)

        def date(self):
            return self.getTypedRuleContext(FluParser.DateContext,0)


        def ON(self):
            return self.getToken(FluParser.ON, 0)

        def IN(self):
            return self.getToken(FluParser.IN, 0)

        def getRuleIndex(self):
            return FluParser.RULE_cycleStatus

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCycleStatus" ):
                return visitor.visitCycleStatus(self)
            else:
                return visitor.visitChildren(self)




    def cycleStatus(self):

        localctx = FluParser.CycleStatusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cycleStatus)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(FluParser.CYCLE)
            self.state = 65
            self.match(FluParser.STATUS)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FluParser.ON or _la==FluParser.IN:
                self.state = 66
                _la = self._input.LA(1)
                if not(_la==FluParser.ON or _la==FluParser.IN):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 69
            self.date()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecificPharseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dateMonth(self):
            return self.getTypedRuleContext(FluParser.DateMonthContext,0)


        def OVU(self):
            return self.getToken(FluParser.OVU, 0)

        def PER(self):
            return self.getToken(FluParser.PER, 0)

        def FER(self):
            return self.getToken(FluParser.FER, 0)

        def NONF(self):
            return self.getToken(FluParser.NONF, 0)

        def DAYS(self):
            return self.getToken(FluParser.DAYS, 0)

        def ON(self):
            return self.getToken(FluParser.ON, 0)

        def IN(self):
            return self.getToken(FluParser.IN, 0)

        def getRuleIndex(self):
            return FluParser.RULE_specificPharse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecificPharse" ):
                return visitor.visitSpecificPharse(self)
            else:
                return visitor.visitChildren(self)




    def specificPharse(self):

        localctx = FluParser.SpecificPharseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_specificPharse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FluParser.PER) | (1 << FluParser.OVU) | (1 << FluParser.FER) | (1 << FluParser.NONF))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FluParser.DAYS:
                self.state = 72
                self.match(FluParser.DAYS)


            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FluParser.ON or _la==FluParser.IN:
                self.state = 75
                _la = self._input.LA(1)
                if not(_la==FluParser.ON or _la==FluParser.IN):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 78
            self.dateMonth()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dateCompare(self):
            return self.getTypedRuleContext(FluParser.DateCompareContext,0)


        def dateInNum(self):
            return self.getTypedRuleContext(FluParser.DateInNumContext,0)


        def dateInWord(self):
            return self.getTypedRuleContext(FluParser.DateInWordContext,0)


        def getRuleIndex(self):
            return FluParser.RULE_date

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDate" ):
                return visitor.visitDate(self)
            else:
                return visitor.visitChildren(self)




    def date(self):

        localctx = FluParser.DateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 80
                self.dateCompare()
                pass

            elif la_ == 2:
                self.state = 81
                self.dateInNum()
                pass

            elif la_ == 3:
                self.state = 82
                self.dateInWord()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateInNumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(FluParser.NUMBER)
            else:
                return self.getToken(FluParser.NUMBER, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(FluParser.SLASH)
            else:
                return self.getToken(FluParser.SLASH, i)

        def getRuleIndex(self):
            return FluParser.RULE_dateInNum

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDateInNum" ):
                return visitor.visitDateInNum(self)
            else:
                return visitor.visitChildren(self)




    def dateInNum(self):

        localctx = FluParser.DateInNumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dateInNum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(FluParser.NUMBER)
            self.state = 86
            self.match(FluParser.SLASH)
            self.state = 87
            self.match(FluParser.NUMBER)
            self.state = 88
            self.match(FluParser.SLASH)
            self.state = 89
            self.match(FluParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateInWordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FluParser.RULE_dateInWord

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDateInWord" ):
                return visitor.visitDateInWord(self)
            else:
                return visitor.visitChildren(self)




    def dateInWord(self):

        localctx = FluParser.DateInWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dateInWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FluParser.T__0) | (1 << FluParser.T__1) | (1 << FluParser.T__2))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateCompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(FluParser.NUMBER, 0)

        def DAYS(self):
            return self.getToken(FluParser.DAYS, 0)

        def BeforeAfter(self):
            return self.getToken(FluParser.BeforeAfter, 0)

        def getRuleIndex(self):
            return FluParser.RULE_dateCompare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDateCompare" ):
                return visitor.visitDateCompare(self)
            else:
                return visitor.visitChildren(self)




    def dateCompare(self):

        localctx = FluParser.DateCompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_dateCompare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(FluParser.NUMBER)
            self.state = 94
            self.match(FluParser.DAYS)
            self.state = 95
            self.match(FluParser.BeforeAfter)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateMonthContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def monthWord(self):
            return self.getTypedRuleContext(FluParser.MonthWordContext,0)


        def monthCompare(self):
            return self.getTypedRuleContext(FluParser.MonthCompareContext,0)


        def getRuleIndex(self):
            return FluParser.RULE_dateMonth

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDateMonth" ):
                return visitor.visitDateMonth(self)
            else:
                return visitor.visitChildren(self)




    def dateMonth(self):

        localctx = FluParser.DateMonthContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dateMonth)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FluParser.WHEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.monthWord()
                pass
            elif token in [FluParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.monthCompare()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MonthWordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(FluParser.WHEN, 0)

        def MO(self):
            return self.getToken(FluParser.MO, 0)

        def getRuleIndex(self):
            return FluParser.RULE_monthWord

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMonthWord" ):
                return visitor.visitMonthWord(self)
            else:
                return visitor.visitChildren(self)




    def monthWord(self):

        localctx = FluParser.MonthWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_monthWord)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(FluParser.WHEN)
            self.state = 102
            self.match(FluParser.MO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MonthCompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(FluParser.NUMBER, 0)

        def MO(self):
            return self.getToken(FluParser.MO, 0)

        def BeforeAfter(self):
            return self.getToken(FluParser.BeforeAfter, 0)

        def getRuleIndex(self):
            return FluParser.RULE_monthCompare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMonthCompare" ):
                return visitor.visitMonthCompare(self)
            else:
                return visitor.visitChildren(self)




    def monthCompare(self):

        localctx = FluParser.MonthCompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_monthCompare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(FluParser.NUMBER)
            self.state = 105
            self.match(FluParser.MO)
            self.state = 106
            self.match(FluParser.BeforeAfter)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





