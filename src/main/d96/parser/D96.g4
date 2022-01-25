/* 1852611 */ 
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: class_decl* class_init EOF;
class_init: 'Class' 'Program' LCB body RCB;
body: 'main' LP RP block_stmt;
/* Class declaration */
class_decl: CLASS classname LCB classbody RCB;
classname: IDENTIFIER (':'IDENTIFIER)?;
classbody:(attribute_decl | method_decl)*;

/* Attribute declaration */
attribute_decl: (VAL|VAR) attributename_list CL (primitive_types|array_decl) attribute_init SM;
attributename_list: IDENTIFIER (CM IDENTIFIER)*;
attribute_init: (ASSIGN expression_list)?;

/* Method declaration */
method_decl
	:((IDENTIFIER|CONSTRUCTOR) LP parameter_list? RP block_stmt)
	| (DESTRUCTOR LP RP block_stmt)
	;
parameter_list: parameter (SM parameter)*;
parameter: IDENTIFIER (','IDENTIFIER)* CL primitive_types;



/* 4.TYPE AND VALUE */
/* Primitive types */
primitive_types
	: BOOLEAN | INT | FLOAT |  STRING
	;

/* 5.EXPRESSIONS */
expression_list:expression (CM expression)*;
expression: 
	expression (STR_CONCAT | STR_CMP) expression 
	| expr_1;
expr_1: 
	expr_1 (EQ | NE | GT | LS | GE | LE) expr_1 
	| expr_2;
expr_2: 
	expr_2 (ANDAND | OROR) expr_3 
	| expr_3;
expr_3: 
	expr_3 (PLUS | MINUS) expr_4 
	| expr_4;
expr_4: 
	expr_4 (STAR | DIV | MOD) expr_5 
	| expr_5;
expr_5: 
	NOT expr_5 
	| expr_6;
expr_6: 
	MINUS expr_6 
	| expr_7;
expr_7: 
	expr_7 (LSB | RSB) 
	| expr_8;
expr_8: 
	expr_8 DOT expr_9 
	| expr_9;
expr_9: 
	expr_9 DCL expr_9 
	| expr_10; 
expr_10: 
	NEW expr_10 
	| operands;
operands
	: IDENTIFIER
	| literals
	| call_expr
	| object_create

	;
call_expr: IDENTIFIER LP expr_list? RP ;
expr_list: expression (CM expression)*;
literals
	: INT_LIT
	| FLOAT_LIT
	| bool_lit
	| STRING_LIT
	| array_lit
	;

array_lit: ARRAY LP array_list? RP;
array_list
	: arrayitemint_list
	| arrayitemfloat_list
	| arrayitembool_list
	| arrayitemstring_list
	| arrayitemarray_list
	;
arrayitemint_list: INT_LIT(','INT_LIT)*;
arrayitemfloat_list:FLOAT_LIT(','FLOAT_LIT)* ;
arrayitembool_list:bool_lit(','bool_lit)*;
arrayitemstring_list:STRING_LIT(','STRING_LIT)*;
arrayitemarray_list:array_lit(','array_lit)*;
/* Array declaration */
array_decl: ARRAY LSB element_type CM INT_LIT RSB;
element_type: (primitive_types | ARRAY);



/* Member access */

/* Object creation */
object_create: NEW IDENTIFIER LP expression_list? RP SM;



/* Self */

/* Operator precedence and associativity */

/* Type coercions */
index_expression:  expression index_op;
index_op: (LSB expression RSB) | (LSB expression RSB index_op);

/* 6.STATEMENTS */
block_stmt
	: LCB stmt_list* RCB
	;
stmt_list
	:vardecl_stmt
	|assign_stmt
	|if_stmt
	|forin_stmt
	|break_stmt
	|continue_stmt
	|return_stmt
	|methodinvocation_stmt
	|block_stmt
	;
vardecl_stmt:(VAL|VAR) varname_list CL (primitive_types | array_decl) var_init? SM;
var_init: ASSIGN expression_list;
varname_list: IDENTIFIER (CM IDENTIFIER)*;

assign_stmt: assign_lhs ASSIGN assign_tail SM;
assign_lhs: IDENTIFIER | index_expression;
assign_tail: (assign_lhs ASSIGN assign_tail) | expression;

if_stmt: IF LP expression RP block_stmt (ELSEIF LP expression RP block_stmt)* (ELSE block_stmt)?;

forin_stmt: FOREACH LP IDENTIFIER IN INT_LIT DDOT INT_LIT (BY INT_LIT)?RP block_stmt;

break_stmt: BREAK SM;

continue_stmt: CONTINUE SM;

return_stmt: RETURN expression? SM;

methodinvocation_stmt:VAL;

//LEXER

/* Keywords */
BREAK: 'Break';
CONTINUE: 'Continue';
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';
TRUE: 'True';
FALSE: 'False';
ARRAY: 'Array';
IN: 'In';
INT: 'Int';
FLOAT: 'Float';
BOOLEAN: 'Boolean';
STRING: 'String';
RETURN: 'Return';
NULL: 'Null';
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';
WRITELN: 'WriteLn' | 'writeln' | 'WRITELN';

/* Operators */
PLUS: '+';
MINUS: '-';
STAR: '*';
DIV: '/';
MOD: '%';
NOT: '!';
ANDAND: '&&';
OROR: '||';
EQ: '==';
ASSIGN: '=';
NE: '!=';
GT: '>';
GE: '>=';
LS: '<';
LE: '<=';
STR_CMP: '==.';
STR_CONCAT: '+.';
DCL: '::';
SM : ';';
CM : ',';
DOT: '.';
DDOT: '..';
CL: ':';

/* Seperators */
LP : '(';
RP : ')';
LSB : '[';
RSB : ']';
LCB : '{';
RCB : '}';

//tokens
IDENTIFIER:ID_normal| ID_static;
INT_LIT:(DECIMAL|OCTAL|HEX|BINARY){self.text = self.text.replace("_", "")};
FLOAT_LIT
	: (DECIMAL+ DOT (DECIMAL | EXPONENT)* // 1 | 1.5 | 1.e-4
	| DECIMAL+ DOT DECIMAL+ EXPONENT? // (1).5(e-4)
	| DECIMAL+ EXPONENT // 12e-5
	| DOT DECIMAL* EXPONENT?
	){self.text = self.text.replace("_", "")}
	;
bool_lit: TRUE | FALSE;

STRING_LIT:  '"' STR_CHAR* '"'{y = str(self.text)
self.text = y[1:-1]
	}
	;

//fragment
fragment ID_normal: [a-zA-Z_][a-zA-Z0-9_]*;

fragment ID_static: '$'[a-zA-Z_][a-zA-Z0-9_]*;

fragment DECIMAL: ([1-9][0-9]*('_'[0-9]+)*)| '0';

fragment OCTAL: '0'[0-7]+('_'[0-7]+)*;

fragment HEX: '0'[xX]([0-9A-F]+('_'[0-9A-F]+)*)+;

fragment BINARY: '0' [bB] [01]+('_'[01]+)*;

fragment DIGIT: [0-9];

fragment DIGITNONZERO: [1-9];

SDIGIT:  DIGIT+;

fragment EXPONENT: [eE] SIGN? DIGIT+ ;

fragment SIGN: [+-] ;

fragment ESC_SEQ: '\\' [btnfr"'\\] ;

fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ; 

fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;

//skip
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
BLOCKCOMMENT: '##' .*? '##'-> skip;


//error
ERROR_CHAR: .{raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' STR_CHAR* ([\b\t\n\f\r"'\\] | EOF){
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:]) 
};
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;