# Generated from Automata.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AutomataParser import AutomataParser
else:
    from AutomataParser import AutomataParser

# This class defines a complete listener for a parse tree produced by AutomataParser.
class AutomataListener(ParseTreeListener):

    # Enter a parse tree produced by AutomataParser#s.
    def enterS(self, ctx:AutomataParser.SContext):
        pass

    # Exit a parse tree produced by AutomataParser#s.
    def exitS(self, ctx:AutomataParser.SContext):
        pass


    # Enter a parse tree produced by AutomataParser#line.
    def enterLine(self, ctx:AutomataParser.LineContext):
        pass

    # Exit a parse tree produced by AutomataParser#line.
    def exitLine(self, ctx:AutomataParser.LineContext):
        pass


    # Enter a parse tree produced by AutomataParser#rule.
    def enterRule(self, ctx:AutomataParser.RuleContext):
        pass

    # Exit a parse tree produced by AutomataParser#rule.
    def exitRule(self, ctx:AutomataParser.RuleContext):
        pass


    # Enter a parse tree produced by AutomataParser#comment.
    def enterComment(self, ctx:AutomataParser.CommentContext):
        pass

    # Exit a parse tree produced by AutomataParser#comment.
    def exitComment(self, ctx:AutomataParser.CommentContext):
        pass


    # Enter a parse tree produced by AutomataParser#expr.
    def enterExpr(self, ctx:AutomataParser.ExprContext):
        pass

    # Exit a parse tree produced by AutomataParser#expr.
    def exitExpr(self, ctx:AutomataParser.ExprContext):
        pass


    # Enter a parse tree produced by AutomataParser#alternative.
    def enterAlternative(self, ctx:AutomataParser.AlternativeContext):
        pass

    # Exit a parse tree produced by AutomataParser#alternative.
    def exitAlternative(self, ctx:AutomataParser.AlternativeContext):
        pass


    # Enter a parse tree produced by AutomataParser#non_alternative.
    def enterNon_alternative(self, ctx:AutomataParser.Non_alternativeContext):
        pass

    # Exit a parse tree produced by AutomataParser#non_alternative.
    def exitNon_alternative(self, ctx:AutomataParser.Non_alternativeContext):
        pass


    # Enter a parse tree produced by AutomataParser#parentheses.
    def enterParentheses(self, ctx:AutomataParser.ParenthesesContext):
        pass

    # Exit a parse tree produced by AutomataParser#parentheses.
    def exitParentheses(self, ctx:AutomataParser.ParenthesesContext):
        pass


    # Enter a parse tree produced by AutomataParser#plus.
    def enterPlus(self, ctx:AutomataParser.PlusContext):
        pass

    # Exit a parse tree produced by AutomataParser#plus.
    def exitPlus(self, ctx:AutomataParser.PlusContext):
        pass


    # Enter a parse tree produced by AutomataParser#star.
    def enterStar(self, ctx:AutomataParser.StarContext):
        pass

    # Exit a parse tree produced by AutomataParser#star.
    def exitStar(self, ctx:AutomataParser.StarContext):
        pass


    # Enter a parse tree produced by AutomataParser#maybe.
    def enterMaybe(self, ctx:AutomataParser.MaybeContext):
        pass

    # Exit a parse tree produced by AutomataParser#maybe.
    def exitMaybe(self, ctx:AutomataParser.MaybeContext):
        pass


    # Enter a parse tree produced by AutomataParser#simple_expr.
    def enterSimple_expr(self, ctx:AutomataParser.Simple_exprContext):
        pass

    # Exit a parse tree produced by AutomataParser#simple_expr.
    def exitSimple_expr(self, ctx:AutomataParser.Simple_exprContext):
        pass


    # Enter a parse tree produced by AutomataParser#symbol.
    def enterSymbol(self, ctx:AutomataParser.SymbolContext):
        pass

    # Exit a parse tree produced by AutomataParser#symbol.
    def exitSymbol(self, ctx:AutomataParser.SymbolContext):
        pass



del AutomataParser