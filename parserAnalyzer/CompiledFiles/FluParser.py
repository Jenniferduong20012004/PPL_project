# Generated from F:\\PPL\\PPL_project\\parserAnalyzer\\Flu.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("-\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\3\3\3\5\3\25\n\3\3\3\5\3\30\n\3\3\4\3\4")
        buf.write("\3\5\3\5\5\5\36\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\b\6\b)\n\b\r\b\16\b*\3\b\2\2\t\2\4\6\b\n\f\16\2\4\3\2")
        buf.write("\6\n\3\2\3\5\2)\2\20\3\2\2\2\4\22\3\2\2\2\6\31\3\2\2\2")
        buf.write("\b\35\3\2\2\2\n\37\3\2\2\2\f%\3\2\2\2\16(\3\2\2\2\20\21")
        buf.write("\5\4\3\2\21\3\3\2\2\2\22\24\5\6\4\2\23\25\5\16\b\2\24")
        buf.write("\23\3\2\2\2\24\25\3\2\2\2\25\27\3\2\2\2\26\30\5\b\5\2")
        buf.write("\27\26\3\2\2\2\27\30\3\2\2\2\30\5\3\2\2\2\31\32\t\2\2")
        buf.write("\2\32\7\3\2\2\2\33\36\5\n\6\2\34\36\5\f\7\2\35\33\3\2")
        buf.write("\2\2\35\34\3\2\2\2\36\t\3\2\2\2\37 \7\r\2\2 !\7\13\2\2")
        buf.write("!\"\7\r\2\2\"#\7\13\2\2#$\7\16\2\2$\13\3\2\2\2%&\t\3\2")
        buf.write("\2&\r\3\2\2\2\')\7\f\2\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2")
        buf.write("\2*+\3\2\2\2+\17\3\2\2\2\6\24\27\35*")
        return buf.getvalue()


class FluParser ( Parser ):

    grammarFileName = "Flu.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'tomorrow'", "'today'", "'yesterday'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "START", "END", "SHOW", "PREDICT", "ADD", "SLASH", 
                      "WORD", "DATE_MONTH", "YEAR", "INT", "WS" ]

    RULE_program = 0
    RULE_sentence = 1
    RULE_verb = 2
    RULE_date = 3
    RULE_dateInNum = 4
    RULE_dateInWord = 5
    RULE_phrase = 6

    ruleNames =  [ "program", "sentence", "verb", "date", "dateInNum", "dateInWord", 
                   "phrase" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    START=4
    END=5
    SHOW=6
    PREDICT=7
    ADD=8
    SLASH=9
    WORD=10
    DATE_MONTH=11
    YEAR=12
    INT=13
    WS=14

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




    def program(self):

        localctx = FluParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
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

        def verb(self):
            return self.getTypedRuleContext(FluParser.VerbContext,0)


        def phrase(self):
            return self.getTypedRuleContext(FluParser.PhraseContext,0)


        def date(self):
            return self.getTypedRuleContext(FluParser.DateContext,0)


        def getRuleIndex(self):
            return FluParser.RULE_sentence




    def sentence(self):

        localctx = FluParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.verb()
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FluParser.WORD:
                self.state = 17
                self.phrase()


            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FluParser.T__0) | (1 << FluParser.T__1) | (1 << FluParser.T__2) | (1 << FluParser.DATE_MONTH))) != 0):
                self.state = 20
                self.date()


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

        def PREDICT(self):
            return self.getToken(FluParser.PREDICT, 0)

        def ADD(self):
            return self.getToken(FluParser.ADD, 0)

        def getRuleIndex(self):
            return FluParser.RULE_verb




    def verb(self):

        localctx = FluParser.VerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_verb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FluParser.START) | (1 << FluParser.END) | (1 << FluParser.SHOW) | (1 << FluParser.PREDICT) | (1 << FluParser.ADD))) != 0)):
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


    class DateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dateInNum(self):
            return self.getTypedRuleContext(FluParser.DateInNumContext,0)


        def dateInWord(self):
            return self.getTypedRuleContext(FluParser.DateInWordContext,0)


        def getRuleIndex(self):
            return FluParser.RULE_date




    def date(self):

        localctx = FluParser.DateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_date)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FluParser.DATE_MONTH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.dateInNum()
                pass
            elif token in [FluParser.T__0, FluParser.T__1, FluParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.dateInWord()
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


    class DateInNumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE_MONTH(self, i:int=None):
            if i is None:
                return self.getTokens(FluParser.DATE_MONTH)
            else:
                return self.getToken(FluParser.DATE_MONTH, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(FluParser.SLASH)
            else:
                return self.getToken(FluParser.SLASH, i)

        def YEAR(self):
            return self.getToken(FluParser.YEAR, 0)

        def getRuleIndex(self):
            return FluParser.RULE_dateInNum




    def dateInNum(self):

        localctx = FluParser.DateInNumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dateInNum)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(FluParser.DATE_MONTH)
            self.state = 30
            self.match(FluParser.SLASH)
            self.state = 31
            self.match(FluParser.DATE_MONTH)
            self.state = 32
            self.match(FluParser.SLASH)
            self.state = 33
            self.match(FluParser.YEAR)
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




    def dateInWord(self):

        localctx = FluParser.DateInWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_dateInWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
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


    class PhraseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(FluParser.WORD)
            else:
                return self.getToken(FluParser.WORD, i)

        def getRuleIndex(self):
            return FluParser.RULE_phrase




    def phrase(self):

        localctx = FluParser.PhraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_phrase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 37
                self.match(FluParser.WORD)
                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==FluParser.WORD):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





