# Generated from Automata.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,1,1,1,3,1,33,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,47,8,3,1,4,1,4,3,4,51,8,4,1,5,1,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,
        6,73,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,85,8,8,1,9,
        1,9,1,9,1,9,1,9,1,9,3,9,93,8,9,1,10,1,10,1,11,1,11,1,11,3,11,100,
        8,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,1,2,0,1,1,3,3,
        103,0,27,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,46,1,0,0,0,8,50,1,0,
        0,0,10,52,1,0,0,0,12,72,1,0,0,0,14,74,1,0,0,0,16,84,1,0,0,0,18,92,
        1,0,0,0,20,94,1,0,0,0,22,99,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,
        26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,1,1,0,0,0,29,27,1,0,
        0,0,30,33,3,6,3,0,31,33,3,4,2,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,
        1,0,0,0,34,35,5,2,0,0,35,5,1,0,0,0,36,37,3,22,11,0,37,38,5,4,0,0,
        38,39,3,8,4,0,39,40,5,0,0,1,40,47,1,0,0,0,41,42,3,22,11,0,42,43,
        5,4,0,0,43,44,3,8,4,0,44,45,5,10,0,0,45,47,1,0,0,0,46,36,1,0,0,0,
        46,41,1,0,0,0,47,7,1,0,0,0,48,51,3,12,6,0,49,51,3,10,5,0,50,48,1,
        0,0,0,50,49,1,0,0,0,51,9,1,0,0,0,52,53,3,12,6,0,53,54,5,9,0,0,54,
        55,3,8,4,0,55,11,1,0,0,0,56,73,3,16,8,0,57,58,3,16,8,0,58,59,3,12,
        6,0,59,73,1,0,0,0,60,73,3,18,9,0,61,62,3,18,9,0,62,63,3,12,6,0,63,
        73,1,0,0,0,64,73,3,14,7,0,65,66,3,14,7,0,66,67,3,12,6,0,67,73,1,
        0,0,0,68,73,3,20,10,0,69,70,3,20,10,0,70,71,3,12,6,0,71,73,1,0,0,
        0,72,56,1,0,0,0,72,57,1,0,0,0,72,60,1,0,0,0,72,61,1,0,0,0,72,64,
        1,0,0,0,72,65,1,0,0,0,72,68,1,0,0,0,72,69,1,0,0,0,73,13,1,0,0,0,
        74,75,5,5,0,0,75,76,3,8,4,0,76,77,5,6,0,0,77,15,1,0,0,0,78,79,3,
        14,7,0,79,80,5,7,0,0,80,85,1,0,0,0,81,82,3,20,10,0,82,83,5,7,0,0,
        83,85,1,0,0,0,84,78,1,0,0,0,84,81,1,0,0,0,85,17,1,0,0,0,86,87,3,
        14,7,0,87,88,5,8,0,0,88,93,1,0,0,0,89,90,3,20,10,0,90,91,5,8,0,0,
        91,93,1,0,0,0,92,86,1,0,0,0,92,89,1,0,0,0,93,19,1,0,0,0,94,95,7,
        0,0,0,95,21,1,0,0,0,96,100,5,3,0,0,97,98,5,3,0,0,98,100,3,22,11,
        0,99,96,1,0,0,0,99,97,1,0,0,0,100,23,1,0,0,0,8,27,32,46,50,72,84,
        92,99
    ]

class AutomataParser ( Parser ):

    grammarFileName = "Automata.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "':'", "'('", "')'", "'*'", "'?'", "'|'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "STRING", "COMMENT", "CS", "COLON", "LEFT_PARENTHESIS", 
                      "RIGHT_PARENTHESIS", "STAR", "MAYBE", "ALTERANTIVE", 
                      "NEW_LINE", "WS" ]

    RULE_s = 0
    RULE_line = 1
    RULE_comment = 2
    RULE_rule = 3
    RULE_expr = 4
    RULE_alternative = 5
    RULE_non_alternative = 6
    RULE_parentheses = 7
    RULE_star = 8
    RULE_maybe = 9
    RULE_simple_expr = 10
    RULE_non_terminal_name = 11

    ruleNames =  [ "s", "line", "comment", "rule", "expr", "alternative", 
                   "non_alternative", "parentheses", "star", "maybe", "simple_expr", 
                   "non_terminal_name" ]

    EOF = Token.EOF
    STRING=1
    COMMENT=2
    CS=3
    COLON=4
    LEFT_PARENTHESIS=5
    RIGHT_PARENTHESIS=6
    STAR=7
    MAYBE=8
    ALTERANTIVE=9
    NEW_LINE=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutomataParser.LineContext)
            else:
                return self.getTypedRuleContext(AutomataParser.LineContext,i)


        def getRuleIndex(self):
            return AutomataParser.RULE_s

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS" ):
                listener.enterS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS" ):
                listener.exitS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS" ):
                return visitor.visitS(self)
            else:
                return visitor.visitChildren(self)




    def s(self):

        localctx = AutomataParser.SContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AutomataParser.COMMENT or _la==AutomataParser.CS:
                self.state = 24
                self.line()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rule_(self):
            return self.getTypedRuleContext(AutomataParser.RuleContext,0)


        def comment(self):
            return self.getTypedRuleContext(AutomataParser.CommentContext,0)


        def getRuleIndex(self):
            return AutomataParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = AutomataParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AutomataParser.CS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.rule_()
                pass
            elif token in [AutomataParser.COMMENT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.comment()
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


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(AutomataParser.COMMENT, 0)

        def getRuleIndex(self):
            return AutomataParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = AutomataParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(AutomataParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_terminal_name(self):
            return self.getTypedRuleContext(AutomataParser.Non_terminal_nameContext,0)


        def COLON(self):
            return self.getToken(AutomataParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(AutomataParser.ExprContext,0)


        def EOF(self):
            return self.getToken(AutomataParser.EOF, 0)

        def NEW_LINE(self):
            return self.getToken(AutomataParser.NEW_LINE, 0)

        def getRuleIndex(self):
            return AutomataParser.RULE_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule" ):
                listener.enterRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule" ):
                listener.exitRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule" ):
                return visitor.visitRule(self)
            else:
                return visitor.visitChildren(self)




    def rule_(self):

        localctx = AutomataParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rule)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.non_terminal_name()
                self.state = 37
                self.match(AutomataParser.COLON)
                self.state = 38
                self.expr()
                self.state = 39
                self.match(AutomataParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.non_terminal_name()
                self.state = 42
                self.match(AutomataParser.COLON)
                self.state = 43
                self.expr()
                self.state = 44
                self.match(AutomataParser.NEW_LINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_alternative(self):
            return self.getTypedRuleContext(AutomataParser.Non_alternativeContext,0)


        def alternative(self):
            return self.getTypedRuleContext(AutomataParser.AlternativeContext,0)


        def getRuleIndex(self):
            return AutomataParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = AutomataParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.non_alternative()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.alternative()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlternativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_alternative(self):
            return self.getTypedRuleContext(AutomataParser.Non_alternativeContext,0)


        def ALTERANTIVE(self):
            return self.getToken(AutomataParser.ALTERANTIVE, 0)

        def expr(self):
            return self.getTypedRuleContext(AutomataParser.ExprContext,0)


        def getRuleIndex(self):
            return AutomataParser.RULE_alternative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlternative" ):
                listener.enterAlternative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlternative" ):
                listener.exitAlternative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternative" ):
                return visitor.visitAlternative(self)
            else:
                return visitor.visitChildren(self)




    def alternative(self):

        localctx = AutomataParser.AlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_alternative)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.non_alternative()
            self.state = 53
            self.match(AutomataParser.ALTERANTIVE)
            self.state = 54
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_alternativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star(self):
            return self.getTypedRuleContext(AutomataParser.StarContext,0)


        def non_alternative(self):
            return self.getTypedRuleContext(AutomataParser.Non_alternativeContext,0)


        def maybe(self):
            return self.getTypedRuleContext(AutomataParser.MaybeContext,0)


        def parentheses(self):
            return self.getTypedRuleContext(AutomataParser.ParenthesesContext,0)


        def simple_expr(self):
            return self.getTypedRuleContext(AutomataParser.Simple_exprContext,0)


        def getRuleIndex(self):
            return AutomataParser.RULE_non_alternative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_alternative" ):
                listener.enterNon_alternative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_alternative" ):
                listener.exitNon_alternative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_alternative" ):
                return visitor.visitNon_alternative(self)
            else:
                return visitor.visitChildren(self)




    def non_alternative(self):

        localctx = AutomataParser.Non_alternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_non_alternative)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.star()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.star()
                self.state = 58
                self.non_alternative()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.maybe()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.maybe()
                self.state = 62
                self.non_alternative()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.parentheses()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.parentheses()
                self.state = 66
                self.non_alternative()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 68
                self.simple_expr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 69
                self.simple_expr()
                self.state = 70
                self.non_alternative()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenthesesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PARENTHESIS(self):
            return self.getToken(AutomataParser.LEFT_PARENTHESIS, 0)

        def expr(self):
            return self.getTypedRuleContext(AutomataParser.ExprContext,0)


        def RIGHT_PARENTHESIS(self):
            return self.getToken(AutomataParser.RIGHT_PARENTHESIS, 0)

        def getRuleIndex(self):
            return AutomataParser.RULE_parentheses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentheses" ):
                listener.enterParentheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentheses" ):
                listener.exitParentheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentheses" ):
                return visitor.visitParentheses(self)
            else:
                return visitor.visitChildren(self)




    def parentheses(self):

        localctx = AutomataParser.ParenthesesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parentheses)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(AutomataParser.LEFT_PARENTHESIS)
            self.state = 75
            self.expr()
            self.state = 76
            self.match(AutomataParser.RIGHT_PARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parentheses(self):
            return self.getTypedRuleContext(AutomataParser.ParenthesesContext,0)


        def STAR(self):
            return self.getToken(AutomataParser.STAR, 0)

        def simple_expr(self):
            return self.getTypedRuleContext(AutomataParser.Simple_exprContext,0)


        def getRuleIndex(self):
            return AutomataParser.RULE_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStar" ):
                listener.enterStar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStar" ):
                listener.exitStar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStar" ):
                return visitor.visitStar(self)
            else:
                return visitor.visitChildren(self)




    def star(self):

        localctx = AutomataParser.StarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_star)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AutomataParser.LEFT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.parentheses()
                self.state = 79
                self.match(AutomataParser.STAR)
                pass
            elif token in [AutomataParser.STRING, AutomataParser.CS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.simple_expr()
                self.state = 82
                self.match(AutomataParser.STAR)
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


    class MaybeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parentheses(self):
            return self.getTypedRuleContext(AutomataParser.ParenthesesContext,0)


        def MAYBE(self):
            return self.getToken(AutomataParser.MAYBE, 0)

        def simple_expr(self):
            return self.getTypedRuleContext(AutomataParser.Simple_exprContext,0)


        def getRuleIndex(self):
            return AutomataParser.RULE_maybe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMaybe" ):
                listener.enterMaybe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMaybe" ):
                listener.exitMaybe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMaybe" ):
                return visitor.visitMaybe(self)
            else:
                return visitor.visitChildren(self)




    def maybe(self):

        localctx = AutomataParser.MaybeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_maybe)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AutomataParser.LEFT_PARENTHESIS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.parentheses()
                self.state = 87
                self.match(AutomataParser.MAYBE)
                pass
            elif token in [AutomataParser.STRING, AutomataParser.CS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.simple_expr()
                self.state = 90
                self.match(AutomataParser.MAYBE)
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


    class Simple_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CS(self):
            return self.getToken(AutomataParser.CS, 0)

        def STRING(self):
            return self.getToken(AutomataParser.STRING, 0)

        def getRuleIndex(self):
            return AutomataParser.RULE_simple_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_expr" ):
                listener.enterSimple_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_expr" ):
                listener.exitSimple_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_expr" ):
                return visitor.visitSimple_expr(self)
            else:
                return visitor.visitChildren(self)




    def simple_expr(self):

        localctx = AutomataParser.Simple_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_simple_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not(_la==AutomataParser.STRING or _la==AutomataParser.CS):
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


    class Non_terminal_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CS(self):
            return self.getToken(AutomataParser.CS, 0)

        def non_terminal_name(self):
            return self.getTypedRuleContext(AutomataParser.Non_terminal_nameContext,0)


        def getRuleIndex(self):
            return AutomataParser.RULE_non_terminal_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_terminal_name" ):
                listener.enterNon_terminal_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_terminal_name" ):
                listener.exitNon_terminal_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_terminal_name" ):
                return visitor.visitNon_terminal_name(self)
            else:
                return visitor.visitChildren(self)




    def non_terminal_name(self):

        localctx = AutomataParser.Non_terminal_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_non_terminal_name)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(AutomataParser.CS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.match(AutomataParser.CS)
                self.state = 98
                self.non_terminal_name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





