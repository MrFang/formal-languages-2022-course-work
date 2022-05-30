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
        4,1,12,114,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,1,2,1,
        3,1,3,3,3,44,8,3,1,3,1,3,1,4,1,4,3,4,50,8,4,1,5,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,3,6,76,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,
        8,88,8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,96,8,9,1,10,1,10,1,10,1,10,
        1,10,1,10,3,10,104,8,10,1,11,1,11,1,11,1,11,3,11,110,8,11,1,12,1,
        12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,1,1,0,10,11,117,
        0,29,1,0,0,0,2,34,1,0,0,0,4,36,1,0,0,0,6,41,1,0,0,0,8,49,1,0,0,0,
        10,51,1,0,0,0,12,75,1,0,0,0,14,77,1,0,0,0,16,87,1,0,0,0,18,95,1,
        0,0,0,20,103,1,0,0,0,22,109,1,0,0,0,24,111,1,0,0,0,26,28,3,2,1,0,
        27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,1,1,0,
        0,0,31,29,1,0,0,0,32,35,3,4,2,0,33,35,3,6,3,0,34,32,1,0,0,0,34,33,
        1,0,0,0,35,3,1,0,0,0,36,37,5,10,0,0,37,38,5,1,0,0,38,39,3,8,4,0,
        39,40,5,2,0,0,40,5,1,0,0,0,41,43,5,3,0,0,42,44,3,22,11,0,43,42,1,
        0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,2,0,0,46,7,1,0,0,0,47,
        50,3,12,6,0,48,50,3,10,5,0,49,47,1,0,0,0,49,48,1,0,0,0,50,9,1,0,
        0,0,51,52,3,12,6,0,52,53,5,4,0,0,53,54,3,8,4,0,54,11,1,0,0,0,55,
        56,3,16,8,0,56,57,3,12,6,0,57,76,1,0,0,0,58,76,3,16,8,0,59,60,3,
        18,9,0,60,61,3,12,6,0,61,76,1,0,0,0,62,76,3,18,9,0,63,64,3,20,10,
        0,64,65,3,12,6,0,65,76,1,0,0,0,66,76,3,20,10,0,67,68,3,14,7,0,68,
        69,3,12,6,0,69,76,1,0,0,0,70,76,3,14,7,0,71,72,3,22,11,0,72,73,3,
        12,6,0,73,76,1,0,0,0,74,76,3,22,11,0,75,55,1,0,0,0,75,58,1,0,0,0,
        75,59,1,0,0,0,75,62,1,0,0,0,75,63,1,0,0,0,75,66,1,0,0,0,75,67,1,
        0,0,0,75,70,1,0,0,0,75,71,1,0,0,0,75,74,1,0,0,0,76,13,1,0,0,0,77,
        78,5,5,0,0,78,79,3,8,4,0,79,80,5,6,0,0,80,15,1,0,0,0,81,82,3,14,
        7,0,82,83,5,7,0,0,83,88,1,0,0,0,84,85,3,24,12,0,85,86,5,7,0,0,86,
        88,1,0,0,0,87,81,1,0,0,0,87,84,1,0,0,0,88,17,1,0,0,0,89,90,3,14,
        7,0,90,91,5,8,0,0,91,96,1,0,0,0,92,93,3,24,12,0,93,94,5,8,0,0,94,
        96,1,0,0,0,95,89,1,0,0,0,95,92,1,0,0,0,96,19,1,0,0,0,97,98,3,14,
        7,0,98,99,5,9,0,0,99,104,1,0,0,0,100,101,3,24,12,0,101,102,5,9,0,
        0,102,104,1,0,0,0,103,97,1,0,0,0,103,100,1,0,0,0,104,21,1,0,0,0,
        105,110,3,24,12,0,106,107,3,24,12,0,107,108,3,22,11,0,108,110,1,
        0,0,0,109,105,1,0,0,0,109,106,1,0,0,0,110,23,1,0,0,0,111,112,7,0,
        0,0,112,25,1,0,0,0,9,29,34,43,49,75,87,95,103,109
    ]

class AutomataParser ( Parser ):

    grammarFileName = "Automata.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'\\n'", "'//'", "'|'", "'('", 
                     "')'", "'+'", "'*'", "'?'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LS", "SS", "WS" ]

    RULE_s = 0
    RULE_line = 1
    RULE_rule = 2
    RULE_comment = 3
    RULE_expr = 4
    RULE_alternative = 5
    RULE_non_alternative = 6
    RULE_parentheses = 7
    RULE_plus = 8
    RULE_star = 9
    RULE_maybe = 10
    RULE_simple_expr = 11
    RULE_symbol = 12

    ruleNames =  [ "s", "line", "rule", "comment", "expr", "alternative", 
                   "non_alternative", "parentheses", "plus", "star", "maybe", 
                   "simple_expr", "symbol" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    LS=10
    SS=11
    WS=12

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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==AutomataParser.T__2 or _la==AutomataParser.LS:
                self.state = 26
                self.line()
                self.state = 31
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
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AutomataParser.LS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.rule_()
                pass
            elif token in [AutomataParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
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


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(AutomataParser.LS, 0)

        def expr(self):
            return self.getTypedRuleContext(AutomataParser.ExprContext,0)


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
        self.enterRule(localctx, 4, self.RULE_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(AutomataParser.LS)
            self.state = 37
            self.match(AutomataParser.T__0)
            self.state = 38
            self.expr()
            self.state = 39
            self.match(AutomataParser.T__1)
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

        def simple_expr(self):
            return self.getTypedRuleContext(AutomataParser.Simple_exprContext,0)


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
        self.enterRule(localctx, 6, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(AutomataParser.T__2)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==AutomataParser.LS or _la==AutomataParser.SS:
                self.state = 42
                self.simple_expr()


            self.state = 45
            self.match(AutomataParser.T__1)
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
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.non_alternative()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
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
            self.state = 51
            self.non_alternative()
            self.state = 52
            self.match(AutomataParser.T__3)
            self.state = 53
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

        def plus(self):
            return self.getTypedRuleContext(AutomataParser.PlusContext,0)


        def non_alternative(self):
            return self.getTypedRuleContext(AutomataParser.Non_alternativeContext,0)


        def star(self):
            return self.getTypedRuleContext(AutomataParser.StarContext,0)


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
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.plus()
                self.state = 56
                self.non_alternative()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.plus()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.star()
                self.state = 60
                self.non_alternative()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.star()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.maybe()
                self.state = 64
                self.non_alternative()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 66
                self.maybe()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 67
                self.parentheses()
                self.state = 68
                self.non_alternative()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 70
                self.parentheses()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 71
                self.simple_expr()
                self.state = 72
                self.non_alternative()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 74
                self.simple_expr()
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

        def expr(self):
            return self.getTypedRuleContext(AutomataParser.ExprContext,0)


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
            self.state = 77
            self.match(AutomataParser.T__4)
            self.state = 78
            self.expr()
            self.state = 79
            self.match(AutomataParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parentheses(self):
            return self.getTypedRuleContext(AutomataParser.ParenthesesContext,0)


        def symbol(self):
            return self.getTypedRuleContext(AutomataParser.SymbolContext,0)


        def getRuleIndex(self):
            return AutomataParser.RULE_plus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlus" ):
                listener.enterPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlus" ):
                listener.exitPlus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlus" ):
                return visitor.visitPlus(self)
            else:
                return visitor.visitChildren(self)




    def plus(self):

        localctx = AutomataParser.PlusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_plus)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AutomataParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.parentheses()
                self.state = 82
                self.match(AutomataParser.T__6)
                pass
            elif token in [AutomataParser.LS, AutomataParser.SS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.symbol()
                self.state = 85
                self.match(AutomataParser.T__6)
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


    class StarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parentheses(self):
            return self.getTypedRuleContext(AutomataParser.ParenthesesContext,0)


        def symbol(self):
            return self.getTypedRuleContext(AutomataParser.SymbolContext,0)


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
        self.enterRule(localctx, 18, self.RULE_star)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AutomataParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.parentheses()
                self.state = 90
                self.match(AutomataParser.T__7)
                pass
            elif token in [AutomataParser.LS, AutomataParser.SS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.symbol()
                self.state = 93
                self.match(AutomataParser.T__7)
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


        def symbol(self):
            return self.getTypedRuleContext(AutomataParser.SymbolContext,0)


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
        self.enterRule(localctx, 20, self.RULE_maybe)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AutomataParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.parentheses()
                self.state = 98
                self.match(AutomataParser.T__8)
                pass
            elif token in [AutomataParser.LS, AutomataParser.SS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.symbol()
                self.state = 101
                self.match(AutomataParser.T__8)
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

        def symbol(self):
            return self.getTypedRuleContext(AutomataParser.SymbolContext,0)


        def simple_expr(self):
            return self.getTypedRuleContext(AutomataParser.Simple_exprContext,0)


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
        self.enterRule(localctx, 22, self.RULE_simple_expr)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.symbol()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.symbol()
                self.state = 107
                self.simple_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(AutomataParser.LS, 0)

        def SS(self):
            return self.getToken(AutomataParser.SS, 0)

        def getRuleIndex(self):
            return AutomataParser.RULE_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbol" ):
                listener.enterSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbol" ):
                listener.exitSymbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbol" ):
                return visitor.visitSymbol(self)
            else:
                return visitor.visitChildren(self)




    def symbol(self):

        localctx = AutomataParser.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_symbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            _la = self._input.LA(1)
            if not(_la==AutomataParser.LS or _la==AutomataParser.SS):
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





