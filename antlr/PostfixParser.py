# Generated from Postfix.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\7\2\r\n\2\f")
        buf.write("\2\16\2\20\13\2\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4)\n\4\3\5\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\2")
        buf.write("-\2\25\3\2\2\2\4\32\3\2\2\2\6(\3\2\2\2\b*\3\2\2\2\n\16")
        buf.write("\5\4\3\2\13\r\7\6\2\2\f\13\3\2\2\2\r\20\3\2\2\2\16\f\3")
        buf.write("\2\2\2\16\17\3\2\2\2\17\21\3\2\2\2\20\16\3\2\2\2\21\22")
        buf.write("\b\2\1\2\22\24\3\2\2\2\23\n\3\2\2\2\24\27\3\2\2\2\25\23")
        buf.write("\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2\2\27\25\3\2\2\2\30")
        buf.write("\31\7\2\2\3\31\3\3\2\2\2\32\33\5\b\5\2\33\34\5\6\4\2\34")
        buf.write("\5\3\2\2\2\35\36\7\3\2\2\36\37\5\b\5\2\37 \b\4\1\2 !\5")
        buf.write("\6\4\2!)\3\2\2\2\"#\7\4\2\2#$\5\b\5\2$%\b\4\1\2%&\5\6")
        buf.write("\4\2&)\3\2\2\2\')\3\2\2\2(\35\3\2\2\2(\"\3\2\2\2(\'\3")
        buf.write("\2\2\2)\7\3\2\2\2*+\7\5\2\2+,\b\5\1\2,\t\3\2\2\2\5\16")
        buf.write("\25(")
        return buf.getvalue()


class PostfixParser ( Parser ):

    grammarFileName = "Postfix.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "DIGIT", "NL" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_rest = 2
    RULE_term = 3

    ruleNames =  [ "prog", "expr", "rest", "term" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    DIGIT=3
    NL=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PostfixParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PostfixParser.ExprContext)
            else:
                return self.getTypedRuleContext(PostfixParser.ExprContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(PostfixParser.NL)
            else:
                return self.getToken(PostfixParser.NL, i)

        def getRuleIndex(self):
            return PostfixParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = PostfixParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PostfixParser.DIGIT:
                self.state = 8
                self.expr()
                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PostfixParser.NL:
                    self.state = 9
                    self.match(PostfixParser.NL)
                    self.state = 14
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                print()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(PostfixParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(PostfixParser.TermContext,0)


        def rest(self):
            return self.getTypedRuleContext(PostfixParser.RestContext,0)


        def getRuleIndex(self):
            return PostfixParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = PostfixParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.term()
            self.state = 25
            self.rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(PostfixParser.TermContext,0)


        def rest(self):
            return self.getTypedRuleContext(PostfixParser.RestContext,0)


        def getRuleIndex(self):
            return PostfixParser.RULE_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRest" ):
                listener.enterRest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRest" ):
                listener.exitRest(self)




    def rest(self):

        localctx = PostfixParser.RestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_rest)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PostfixParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(PostfixParser.T__0)
                self.state = 28
                self.term()
                print('+', end='')
                self.state = 30
                self.rest()
                pass
            elif token in [PostfixParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(PostfixParser.T__1)
                self.state = 33
                self.term()
                print('-', end='')
                self.state = 35
                self.rest()
                pass
            elif token in [PostfixParser.EOF, PostfixParser.DIGIT, PostfixParser.NL]:
                self.enterOuterAlt(localctx, 3)

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


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._DIGIT = None # Token

        def DIGIT(self):
            return self.getToken(PostfixParser.DIGIT, 0)

        def getRuleIndex(self):
            return PostfixParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = PostfixParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            localctx._DIGIT = self.match(PostfixParser.DIGIT)
            print((0 if localctx._DIGIT is None else int(localctx._DIGIT.text)), end='')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





