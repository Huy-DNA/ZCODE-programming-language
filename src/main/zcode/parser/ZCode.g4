grammar ZCode;

@lexer::header {
from lexererr import *
}

@lexer::members {

}

options {
	language=Python3;
}

program: (stm (NEWLINE stm)* | NEWLINE* | COMMENT) EOF;

// statement rule

stm: expr | decl | ass | block | func | r_break | r_continue | r_return | r_if | r_for;

r_break: 'break';

r_continue: 'continue';

r_return: 'return' expr;

r_if: 'if' '('expr')' NEWLINE* stm
	| 'if' '('expr')' NEWLINE* stm ('elif' '('expr')' NEWLINE* stm)*? ('else' NEWLINE* stm)?;

r_for: 'for' expr 'until' expr 'by' expr NEWLINE* stm;

block: 'begin' NEWLINE (stm (NEWLINE stm)* | NEWLINE* | COMMENT) NEWLINE 'end';

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
	| expr op=('*' | '/' | '%') expr
	| expr op=('+' | '-') expr
	| expr_without_rel op=('=' | '==' | '!=' | '<' | '>' | '<=' | '>=') expr_without_rel
	| expr_without_rel;
expr_without_rel: expr_without_str_concat'...'expr_without_str_concat
	| expr_without_str_concat;
expr_without_str_concat: expr_without_str_concat op=('and' | 'or') expr_without_str_concat
	| '['(expr(','expr)*)?']'
	| NUMBER
	| STRING
	| IDENTIFIER
	| '(' expr ')';

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

// COMMENT token
COMMENT: '##' .*? (NEWLINE | EOF) { self.text = self.text.rstrip() };

// Misc tokens
WS : [ \t\f]+ -> skip ; // skip spaces, tabs, newlineso
NEWLINE: '\r'? '\n';
ERROR_CHAR: . {raise ErrorToken(self.text)};