grammar Automata;

s: line*;

line: rule | comment;

rule:
    LS ':' expr '\n';

comment:
    '//' simple_expr? '\n';

expr:
    non_alternative | alternative;

alternative:
    non_alternative '|' expr;

non_alternative:
    plus non_alternative | plus |
    star non_alternative | star |
    maybe non_alternative | maybe |
    parentheses non_alternative | parentheses |
    simple_expr non_alternative | simple_expr;

parentheses:
    '(' expr ')';

plus:
    parentheses '+' | symbol '+';

star:
    parentheses '*' | symbol '*';

maybe:
    parentheses '?' | symbol '?';

simple_expr:
    symbol | symbol simple_expr;

symbol:
    LS | SS;


LS      : [A-Z];
SS      : [a-z0-9];
WS      : [\t\r ]+ -> skip;
