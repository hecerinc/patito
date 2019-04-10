# Generated from Postfix.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PostfixParser import PostfixParser
else:
    from PostfixParser import PostfixParser

# This class defines a complete listener for a parse tree produced by PostfixParser.
class PostfixListener(ParseTreeListener):

    # Enter a parse tree produced by PostfixParser#prog.
    def enterProg(self, ctx:PostfixParser.ProgContext):
        pass

    # Exit a parse tree produced by PostfixParser#prog.
    def exitProg(self, ctx:PostfixParser.ProgContext):
        pass


    # Enter a parse tree produced by PostfixParser#expr.
    def enterExpr(self, ctx:PostfixParser.ExprContext):
        pass

    # Exit a parse tree produced by PostfixParser#expr.
    def exitExpr(self, ctx:PostfixParser.ExprContext):
        pass


    # Enter a parse tree produced by PostfixParser#rest.
    def enterRest(self, ctx:PostfixParser.RestContext):
        pass

    # Exit a parse tree produced by PostfixParser#rest.
    def exitRest(self, ctx:PostfixParser.RestContext):
        pass


    # Enter a parse tree produced by PostfixParser#term.
    def enterTerm(self, ctx:PostfixParser.TermContext):
        pass

    # Exit a parse tree produced by PostfixParser#term.
    def exitTerm(self, ctx:PostfixParser.TermContext):
        pass


