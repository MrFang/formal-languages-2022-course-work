# Generated from Automata.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,11,67,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,4,0,28,8,
        0,11,0,12,0,29,1,0,1,0,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,12,1,41,9,
        1,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,
        8,1,9,1,9,1,10,4,10,62,8,10,11,10,12,10,63,1,10,1,10,0,0,11,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,1,0,4,2,0,32,33,
        35,126,1,0,32,126,1,0,65,90,3,0,9,9,13,13,32,32,70,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,
        1,0,0,0,3,33,1,0,0,0,5,44,1,0,0,0,7,46,1,0,0,0,9,48,1,0,0,0,11,50,
        1,0,0,0,13,52,1,0,0,0,15,54,1,0,0,0,17,56,1,0,0,0,19,58,1,0,0,0,
        21,61,1,0,0,0,23,27,5,34,0,0,24,25,5,92,0,0,25,28,5,34,0,0,26,28,
        7,0,0,0,27,24,1,0,0,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,0,
        29,30,1,0,0,0,30,31,1,0,0,0,31,32,5,34,0,0,32,2,1,0,0,0,33,34,5,
        47,0,0,34,35,5,47,0,0,35,39,1,0,0,0,36,38,7,1,0,0,37,36,1,0,0,0,
        38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,42,1,0,0,0,41,39,1,
        0,0,0,42,43,5,10,0,0,43,4,1,0,0,0,44,45,7,2,0,0,45,6,1,0,0,0,46,
        47,5,58,0,0,47,8,1,0,0,0,48,49,5,40,0,0,49,10,1,0,0,0,50,51,5,41,
        0,0,51,12,1,0,0,0,52,53,5,42,0,0,53,14,1,0,0,0,54,55,5,63,0,0,55,
        16,1,0,0,0,56,57,5,124,0,0,57,18,1,0,0,0,58,59,5,10,0,0,59,20,1,
        0,0,0,60,62,7,3,0,0,61,60,1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,
        64,1,0,0,0,64,65,1,0,0,0,65,66,6,10,0,0,66,22,1,0,0,0,5,0,27,29,
        39,63,1,6,0,0
    ]

class AutomataLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRING = 1
    COMMENT = 2
    CS = 3
    COLON = 4
    LEFT_PARENTHESIS = 5
    RIGHT_PARENTHESIS = 6
    STAR = 7
    MAYBE = 8
    ALTERANTIVE = 9
    NEW_LINE = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'('", "')'", "'*'", "'?'", "'|'", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "STRING", "COMMENT", "CS", "COLON", "LEFT_PARENTHESIS", "RIGHT_PARENTHESIS", 
            "STAR", "MAYBE", "ALTERANTIVE", "NEW_LINE", "WS" ]

    ruleNames = [ "STRING", "COMMENT", "CS", "COLON", "LEFT_PARENTHESIS", 
                  "RIGHT_PARENTHESIS", "STAR", "MAYBE", "ALTERANTIVE", "NEW_LINE", 
                  "WS" ]

    grammarFileName = "Automata.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


