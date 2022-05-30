grammar Automata;

s: line*;

line: rule | comment;

comment:
    COMMENT;

rule:
    non_terminal_name COLON expr EOF |
    non_terminal_name COLON expr NEW_LINE;

expr:
    non_alternative | alternative;

alternative:
    non_alternative ALTERANTIVE expr;

non_alternative:
    star | star non_alternative |
    maybe | maybe non_alternative |
    parentheses | parentheses non_alternative |
    simple_expr | simple_expr non_alternative;

parentheses:
    LEFT_PARENTHESIS expr RIGHT_PARENTHESIS;

star:
    parentheses STAR | simple_expr STAR;

maybe:
    parentheses MAYBE | simple_expr MAYBE;

simple_expr:
    CS | STRING;

non_terminal_name:
    CS | CS non_terminal_name;


// String of terminal ASCII symbols. Double quote should be used with escape symbol \
STRING      : '"' ('\\"' | [ !#-~])+ '"';
// Comment line
COMMENT     : '//' [ -~]* '\n';

CS                  : [A-Z];                // Capital symbols for non-terminal names
COLON               : ':';
LEFT_PARENTHESIS    : '(';
RIGHT_PARENTHESIS   : ')';
STAR                : '*';
MAYBE               : '?';
ALTERANTIVE         : '|';
NEW_LINE            : '\n';
WS                  : [\t\r ]+ -> skip;     // Spaces and tabs outside string (double quotes) are ignored
