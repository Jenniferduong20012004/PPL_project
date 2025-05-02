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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\66\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\5\3\27\n\3\3\3\5\3\32\n")
        buf.write("\3\3\4\3\4\3\5\3\5\3\5\5\5!\n\5\3\6\3\6\3\6\5\6&\n\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7-\n\7\3\b\3\b\3\t\6\t\62\n\t\r\t")
        buf.write("\16\t\63\3\t\2\2\n\2\4\6\b\n\f\16\20\2\4\3\2\6\n\3\2\3")
        buf.write("\5\2\64\2\22\3\2\2\2\4\24\3\2\2\2\6\33\3\2\2\2\b \3\2")
        buf.write("\2\2\n\"\3\2\2\2\f\'\3\2\2\2\16.\3\2\2\2\20\61\3\2\2\2")
        buf.write("\22\23\5\4\3\2\23\3\3\2\2\2\24\26\5\6\4\2\25\27\5\20\t")
        buf.write("\2\26\25\3\2\2\2\26\27\3\2\2\2\27\31\3\2\2\2\30\32\5\b")
        buf.write("\5\2\31\30\3\2\2\2\31\32\3\2\2\2\32\5\3\2\2\2\33\34\t")
        buf.write("\2\2\2\34\7\3\2\2\2\35!\5\f\7\2\36!\5\16\b\2\37!\5\n\6")
        buf.write("\2 \35\3\2\2\2 \36\3\2\2\2 \37\3\2\2\2!\t\3\2\2\2\"#\7")
        buf.write("\16\2\2#%\7\13\2\2$&\7\17\2\2%$\3\2\2\2%&\3\2\2\2&\13")
        buf.write("\3\2\2\2\'(\7\16\2\2()\7\f\2\2),\7\16\2\2*+\7\f\2\2+-")
        buf.write("\7\17\2\2,*\3\2\2\2,-\3\2\2\2-\r\3\2\2\2./\t\3\2\2/\17")
        buf.write("\3\2\2\2\60\62\7\r\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63")
        buf.write("\61\3\2\2\2\63\64\3\2\2\2\64\21\3\2\2\2\b\26\31 %,\63")
        return buf.getvalue()


class FluParser ( Parser ):

    grammarFileName = "Flu.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'tomorrow'", "'today'", "'yesterday'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "START", "END", "SHOW", "PREDICT", "ADD", "MONTH", 
                      "SLASH", "WORD", "DATE_MONTH", "YEAR", "INT", "WS" ]

    RULE_program = 0
    RULE_sentence = 1
    RULE_verb = 2
    RULE_date = 3
    RULE_dateNumAndWord = 4
    RULE_dateInNum = 5
    RULE_dateInWord = 6
    RULE_phrase = 7

    ruleNames =  [ "program", "sentence", "verb", "date", "dateNumAndWord", 
                   "dateInNum", "dateInWord", "phrase" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    START=4
    END=5
    SHOW=6
    PREDICT=7
    ADD=8
    MONTH=9
    SLASH=10
    WORD=11
    DATE_MONTH=12
    YEAR=13
    INT=14
    WS=15

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
            self.state = 16
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
            self.state = 18
            self.verb()
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FluParser.WORD:
                self.state = 19
                self.phrase()


            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FluParser.T__0) | (1 << FluParser.T__1) | (1 << FluParser.T__2) | (1 << FluParser.DATE_MONTH))) != 0):
                self.state = 22
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
            self.state = 25
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


        def dateNumAndWord(self):
            return self.getTypedRuleContext(FluParser.DateNumAndWordContext,0)


        def getRuleIndex(self):
            return FluParser.RULE_date




    def date(self):

        localctx = FluParser.DateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_date)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.dateInNum()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.dateInWord()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.dateNumAndWord()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DateNumAndWordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATE_MONTH(self):
            return self.getToken(FluParser.DATE_MONTH, 0)

        def MONTH(self):
            return self.getToken(FluParser.MONTH, 0)

        def YEAR(self):
            return self.getToken(FluParser.YEAR, 0)

        def getRuleIndex(self):
            return FluParser.RULE_dateNumAndWord




    def dateNumAndWord(self):

        localctx = FluParser.DateNumAndWordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dateNumAndWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(FluParser.DATE_MONTH)
            self.state = 33
            self.match(FluParser.MONTH)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FluParser.YEAR:
                self.state = 34
                self.match(FluParser.YEAR)


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
        self.enterRule(localctx, 10, self.RULE_dateInNum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(FluParser.DATE_MONTH)
            self.state = 38
            self.match(FluParser.SLASH)
            self.state = 39
            self.match(FluParser.DATE_MONTH)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==FluParser.SLASH:
                self.state = 40
                self.match(FluParser.SLASH)
                self.state = 41
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
        self.enterRule(localctx, 12, self.RULE_dateInWord)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
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
        self.enterRule(localctx, 14, self.RULE_phrase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.match(FluParser.WORD)
                self.state = 49 
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





