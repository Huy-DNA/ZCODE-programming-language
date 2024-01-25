grammar ZCode;

@lexer::header {
from lexererr import *
}

@lexer::members {

}

options {
	language=Python3;
}

// program rule

program: stms EOF;

stms: (NULL_LINES | ) stm_lists (NULL_LINES | ) | ;

stm_lists: stm | stm NULL_LINES stm_lists;

// statement rule

stm: expr | decl | ass | block | func | r_break | r_continue | r_return | r_if | r_for | r_print;

r_print: PRINT expr;

r_break: BREAK;

r_continue: CONTINUE;

r_return: RETURN expr;

// if statement

r_if: IF expr (NULL_LINES | ) stm
	| IF expr (NULL_LINES | ) stm r_elif_list r_else;

r_elif_list: r_elifs | ;

r_elifs: r_elif | r_elif r_elifs;

r_elif: (NULL_LINES | ) ELIF expr (NULL_LINES | ) stm;

r_else: (NULL_LINES | ) ELSE (NULL_LINES | ) stm | ;

// for statement

r_for: FOR expr UNTIL expr BY expr (NULL_LINES | ) stm;

// block statement

block: BEGIN (NULL_LINES block_stms NULL_LINES | NULL_LINES) END;

block_stms: stm | stm NULL_LINES block_stms;

// function statement

func: FUNC IDENTIFIER arg_group (((NULL_LINES | ) (r_return | block)) | );

arg_group: LP args RP;
args: arg_list | ;
arg_list: arg | arg COMMA arg_list;
arg: TYPE IDENTIFIER (type_index | );

type_index: LB type_index_nums RB;
type_index_nums: type_index_num_list | ;
type_index_num_list: NUMBER | NUMBER COMMA type_index_num_list;

// assignment statement

ass: expr ASSIGN expr;

decl: TYPE IDENTIFIER (type_index | ) ASSIGN expr
	| VAR expr ASSIGN expr
	| DYN expr;
 
expr: expr1 op=CONCAT expr1 | expr1;
expr1: expr2 op=(EQ | DEQ | NEQ | LT | GT | LE | GE) expr2 | expr2;
expr2: expr2 op=(AND | OR) expr3 | expr3;
expr3: expr3 op=(ADD | SUB) expr4 | expr4;
expr4: expr4 op=(MUL | DIV | MOD) expr5 | expr5;
expr5: SUB expr5
	| NOT expr5
	| expr6;
expr6: array=expr6 LB indexer=expr_list RB
	| callee=expr6 LP params=expr_list RP
	| term;

term: LB expr_list RB
	| NUMBER
	| STRING
	| BOOLEAN
	| IDENTIFIER	
	| LB expr_list RB
	| LP expr RP;

expr_list: exprs | ;
exprs: expr | expr COMMA exprs;

// TYPE token
TYPE: 'number' | 'string' | 'bool';

// KEYWORDS
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
FOR: 'for';
SUB: '-';
ADD: '+';
MUL: '*';
DIV: '/';
AND: 'and';
OR: 'or';
CONCAT: '...';
ASSIGN: '<-';
EQ: '=';
DEQ: '==';
GE: '>=';
GT: '>';
LE: '<=';
LT: '<';
LP: '(';
RP: ')';
LB: '[';
RB: ']';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
NEQ: '!=';
VAR: 'var';
DYN: 'dynamic';
COMMA: ',';
PRINT: 'print';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';
FUNC: 'func';
MOD: '%';
UNTIL: 'until';
BY: 'by';

// BOOLEAN token
BOOLEAN: 'true' | 'false';

// IDENTIFIER token

IDENTIFIER: [a-zA-Z_] [a-zA-Z_0-9]*;

// NUMBER token
NUMBER: INTEGRAL DECIMAL? EXPONENT?;

fragment
INTEGRAL: [0-9]+;

fragment
DECIMAL: '.'[0-9]*;

fragment
EXPONENT: 'e'(ADD|SUB)?[0-9]+;

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