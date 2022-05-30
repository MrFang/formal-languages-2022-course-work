# Generated from Automata.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AutomataParser import AutomataParser
else:
    from AutomataParser import AutomataParser

# This class defines a complete generic visitor for a parse tree produced by AutomataParser.

class AutomataVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AutomataParser#s.
    def visitS(self, ctx:AutomataParser.SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#line.
    def visitLine(self, ctx:AutomataParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#comment.
    def visitComment(self, ctx:AutomataParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#rule.
    def visitRule(self, ctx:AutomataParser.RuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#expr.
    def visitExpr(self, ctx:AutomataParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#alternative.
    def visitAlternative(self, ctx:AutomataParser.AlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#non_alternative.
    def visitNon_alternative(self, ctx:AutomataParser.Non_alternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#parentheses.
    def visitParentheses(self, ctx:AutomataParser.ParenthesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#star.
    def visitStar(self, ctx:AutomataParser.StarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#maybe.
    def visitMaybe(self, ctx:AutomataParser.MaybeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#simple_expr.
    def visitSimple_expr(self, ctx:AutomataParser.Simple_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#non_terminal_name.
    def visitNon_terminal_name(self, ctx:AutomataParser.Non_terminal_nameContext):
        return self.visitChildren(ctx)



del AutomataParser