grammar ZCode;

@lexer::header {
from lexererr import *
}

@lexer::members {

}

options {
	language=Python3;
}

program: line* EOF;

line: (stm NEWLINE | COMMENT | NEWLINE);

// statement rule

stm: expr | decl | ass | block | func | r_break | r_continue | r_return;

r_break: 'break';

r_continue: 'continue';

r_return: 'return' expr;

r_if: 'if' '('expr')' block ('elif' '('expr')' block)*? ('else' block)?;

r_for: 'for' expr 'until' expr 'by' expr expr;

block: 'begin' NEWLINE line* NEWLINE 'end';

func: 'func' IDENTIFIER args (r_return | block);
args: '(' (TYPE IDENTIFIER type_index? (',' TYPE IDENTIFIER type_index?)*)? ')';
type_index: '[' (NUMBER (',' NUMBER)*)? ']';

ass: expr '<-' expr;

decl: TYPE expr '<-' expr
	| 'var' expr '<-' expr
	| 'dynamic' expr;

expr: '(' expr ')'
	| array=expr'['indexer=expr(','indexer=expr)*']'
	| callee=expr'('(param=expr(','param=expr)*)?')'
	| '-'expr
	| 'not'expr
	| left=expr op=('*' | '/' | '%') right=expr
	| left=expr op=('+' | '-') right=expr
	| left=expr op=('=' | '==' | '!=' | '<' | '>' | '<=' | '>=') right=expr
	| '...'expr
	| left=expr op=('and' | 'or') right=expr
	| '['(expr(','expr)*)?']'
	| NUMBER
	| STRING
	| IDENTIFIER;

// TYPE token
TYPE: 'number' | 'string' | 'bool';

// IDENTIFIER token

IDENTIFIER: [a-z] [a-z0-9]*;

// NUMBER token
NUMBER: INTEGRAL DECIMAL? EXPONENT?;

fragment
INTEGRAL: [0-9]+;

fragment
DECIMAL: '.'[0-9]*;

fragment
EXPONENT: 'e'('+'|'-')?[0-9]+;

// STRING token
ILLEGAL_ESCAPE: '"' (~["] | '\'"')* INVALID_ESCAPED_SEQUENCE+ (~["] | '\'"')* '"';
UNCLOSE_STRING: '"' (~["] | '\'"')*? NEWLINE {raise UncloseString(self.text)};
STRING: '"' (~["\n] | '\'"')* '"';

fragment
INVALID_ESCAPED_SEQUENCE: '\\'~[bfrnt'\\];

// COMMENT token
COMMENT: '##' .*? NEWLINE;

// Misc tokens
WS : [ \t\f]+ -> skip ; // skip spaces, tabs, newlineso
NEWLINE: '\r'? '\n';
ERROR_CHAR: . {raise ErrorToken(self.text)};