grammar ZCode;

@lexer::header {
from lexererr import *
}

@lexer::members {

}

options {
	language=Python3;
}

program: NULL_LINES? (stm (NULL_LINES? stm)*)? EOF;

// statement rule

stm: expr | decl | ass | block | func | r_break | r_continue | r_return | r_if | r_for | print;

print: 'print' expr;

r_break: 'break';

r_continue: 'continue';

r_return: 'return' expr;

r_if: 'if' expr NULL_LINES* stm
	| 'if' expr NULL_LINES* stm (NULL_LINES* 'elif' expr NULL_LINES* stm)*? (NULL_LINES* 'else' NULL_LINES* stm)?;

r_for: 'for' expr 'until' expr 'by' expr NULL_LINES* stm;

block: 'begin' NULL_LINES (stm (NULL_LINES stm)*)? NULL_LINES 'end';

func: 'func' IDENTIFIER args (NULL_LINES* (r_return | block))?;
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
	| expr op=('*' | '/' | '%') expr
	| expr op=('+' | '-') expr
	| concat_expr op=('=' | '==' | '!=' | '<' | '>' | '<=' | '>=') concat_expr
	| concat_expr
	| expr op=('and' | 'or') expr;
concat_expr: operand'...'operand
	| operand;
operand: r_list
	| NUMBER
	| STRING
	| IDENTIFIER
	| '(' expr ')';

r_list: '[' (expr(','expr)*)? ']';

// TYPE token
TYPE: 'number' | 'string' | 'bool';

// IDENTIFIER token

IDENTIFIER: [a-zA-Z_] [a-zA-Z_0-9]*;

// NUMBER token
NUMBER: INTEGRAL DECIMAL? EXPONENT?;

fragment
INTEGRAL: [0-9]+;

fragment
DECIMAL: '.'[0-9]*;

fragment
EXPONENT: 'e'('+'|'-')?[0-9]+;

// STRING token
ILLEGAL_ESCAPE: '"' (~["] | '\'"')* INVALID_ESCAPED_SEQUENCE+ (~["] | '\'"')* '"' {raise IllegalEscape(self.text)} ;
UNCLOSE_STRING: '"' (~["] | '\'"')*? (NEWLINE | EOF) {raise UncloseString(self.text)};
STRING: '"' (~["\n] | '\'"')* '"';

fragment
INVALID_ESCAPED_SEQUENCE: '\\'~[bfrnt'\\];

// NULL_LINES token
NULL_LINES: NEWLINE (NEWLINE | COMMENT)*;

// COMMENT token
COMMENT: '##' .*? (NEWLINE | EOF) { self.text = self.text.rstrip() };

// Misc tokens
WS : [ \t\f]+ -> skip ; // skip spaces, tabs, newlineso
NEWLINE: '\r'? '\n';
ERROR_CHAR: . {raise ErrorToken(self.text)};