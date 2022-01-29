/* 1852611 */ 
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: class_decl+  EOF;
/* Class declaration */
class_decl: CLASS classname LCB classbody RCB;
classname: ID_NORMAL (':'ID_NORMAL)?;
classbody:(attribute_decl | method_decl)*;

type_decl: primitive_types|array_decl | ID_NORMAL; 
/* Attribute declaration */
// attribute_decl: (VAL|VAR) attributename_list CL type_decl attribute_init SM;
// attributename_list: (ID_NORMAL | ID_STATIC) (CM (ID_NORMAL | ID_STATIC))*;
// attribute_init: (ASSIGN expression_list)?;
attribute_decl: (VAL|VAR) (attribute_init_stmt|attribute_stmt) SM;
attribute_init_stmt: 
	(ID_NORMAL | ID_STATIC) CL type_decl ASSIGN expression
	| (ID_NORMAL | ID_STATIC) CM attribute_init_stmt CM expression
  	;
attribute_stmt: attributename_list CL type_decl ;
attributename_list: (ID_NORMAL | ID_STATIC) (CM (ID_NORMAL | ID_STATIC))*;

// attributename_list: (ID_NORMAL | ID_STATIC) (CM (ID_NORMAL | ID_STATIC))*;
// attribute_init: (ASSIGN expression_list)?;

/* Method declaration */
method_decl
	:((ID_NORMAL| ID_STATIC |CONSTRUCTOR) LP parameter_list? RP block_stmt)
	| (DESTRUCTOR LP RP block_stmt)
	;
parameter_list: parameter (SM parameter)*;
parameter: ID_NORMAL (','ID_NORMAL)* CL type_decl;



/* 4.TYPE AND VALUE */
/* Primitive types */
primitive_types
	: BOOLEAN | INT | FLOAT |  STRING
	;

/* 5.EXPRESSIONS */
expression_list:expression (CM expression)*;
expression: 
	expr_1 (STR_CONCAT | STR_CMP) expr_1 
	| expr_1;
expr_1: 
	expr_2 (EQ | NE | GT | LS | GE | LE) expr_2 
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
	expr_8 DOT ID_NORMAL postfix? (DOT ID_NORMAL postfix?)*
	| expr_9;
expr_9: 
	expr_10 DCL ID_STATIC postfix? (DOT ID_NORMAL postfix?)*
	| expr_10; 
expr_10: 
	NEW expr_10 
	| expr_11;
expr_11:
	operands
	| LP expression RP;
operands
	: ID_NORMAL
	// | ID_STATIC
	| literals
	| call_expr
	| postfix
	| operands postfix_array
	| SELF
	| NULL
	;
 call_expr: ID_NORMAL LP expression_list? RP ;
// expr_list: expression (CM expression)*;
postfix: LP expression_list? RP ;
postfix_array: LSB expression RSB;
literals
	: INT_LIT
	| FLOAT_LIT
	| bool_lit
	| STRING_LIT
	| array_lit
	;

array_lit: ARRAY LP array_list? RP;
array_list
	: expression_list
	| array_lit (CM array_lit)*
	;
// arrayitemint_list: INT_LIT(','INT_LIT)*;
// arrayitemfloat_list:FLOAT_LIT(','FLOAT_LIT)* ;
// arrayitembool_list:bool_lit(','bool_lit)*;
// arrayitemstring_list:STRING_LIT(','STRING_LIT)*;
// arrayitemarray_list:array_lit(','array_lit)*;
/* Array declaration */
array_decl: ARRAY LSB element_type CM INT_LIT RSB{
print($INT_LIT.text)
if(int($INT_LIT.text) < 1 or not(is_integer($INT_LIT.text))):
	raise ErrorToken($INT_LIT.text)
};
element_type: (primitive_types | ARRAY | array_decl);



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
	// |block_stmt
	;
vardecl_stmt:(VAL|VAR) varname_list CL type_decl var_init? SM;
var_init: ASSIGN expression_list;
varname_list: ID_NORMAL (CM ID_NORMAL)*;

assign_stmt: assign_lhs ASSIGN assign_tail SM;
assign_lhs: expression | index_expression;
assign_tail: (assign_lhs ASSIGN assign_tail) | expression;

if_stmt: IF LP expression RP block_stmt (ELSEIF LP expression RP block_stmt)* (ELSE block_stmt)?;

forin_stmt: FOREACH LP ID_NORMAL IN expression DDOT expression (BY expression)?RP block_stmt;

break_stmt: BREAK SM;

continue_stmt: CONTINUE SM;

return_stmt: RETURN expression? SM;

methodinvocation_stmt: (methodinvo_instance | methodinvo_static);
// methodinvo_static: DCL ID_STATIC; 
// methodinvo_instance: DOT ID_NORMAL;
methodinvo_instance: expression DOT ID_NORMAL postfix? methodpostfix* SM;
methodinvo_static: ID_NORMAL DCL ID_STATIC postfix? methodpostfix* SM;

methodpostfix: DOT ID_NORMAL postfix?;

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
SELF: 'Self';

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
DDOT: '..';
DOT: '.';
CL: ':';

/* Seperators */
LP : '(';
RP : ')';
LSB : '[';
RSB : ']';
LCB : '{';
RCB : '}';

//tokens
// IDENTIFIER:ID_normal| ID_static;
ID_NORMAL: ID_normal;
ID_STATIC: ID_static;


// FLOAT_LIT
// 	: (DECIMAL+ DOT (DECIMAL | EXPONENT)* // 1 | 1.5 | 1.e-4
// 	| DECIMAL+ DOT DECIMAL+ EXPONENT? // (1).5(e-4)
// 	| DECIMAL+ EXPONENT // 12e-5
// 	| DOT DECIMAL* EXPONENT?
// 	){self.text = self.text.replace("_", "")}
// 	;
INT_LIT:(DECIMAL|OCTAL|HEX|BINARY|'0'){self.text = self.text.replace("_","")
	};
FLOAT_LIT
	// :  (DECIMAL DECIMAL_FLOAT EXPONENT?
	// | DECIMAL? DECIMAL_FLOAT EXPONENT
	// | DECIMAL DECIMAL_FLOAT? EXPONENT){self.text = self.text.replace("_", "")}
	:(DIGIT(DIGIT|'_')* DOT DIGIT+ EXPONENT?
	| DIGIT(DIGIT|'_')*  EXPONENT
	| DOT DIGIT?(DIGIT|'_')*  EXPONENT
	){self.text = self.text.replace("_", "")}
	;

bool_lit: TRUE | FALSE;

STRING_LIT: '"' STR_CHAR* '"'{ self.text = self.text[1:-1] };

//fragment
fragment ID_normal: [a-zA-Z_][a-zA-Z0-9_]*;

fragment ID_static: '$'[a-zA-Z0-9_][a-zA-Z0-9_]*;

// fragment OCTAL: '0'[0-7][_0-7]*;
fragment OCTAL: '0'[0-7]('_'?[0-7]+)*;

// fragment HEX: '0'[xX][0-9A-F][_0-9A-F]*;
fragment HEX: '0'[xX][0-9A-F]('_'?[0-9A-F]+)*;

// fragment BINARY: '0'[bB][01][_01]*;
fragment BINARY: '0'[bB][01]('_'?[01]+)*;


fragment DECIMAL: [1-9]('_'?[0-9]+)*;

fragment DECIMAL_FLOAT: DOT DECIMAL?;

fragment DIGIT: [0-9];

fragment DIGITNONZERO: [1-9];

fragment EXPONENT: [eE] SIGN? DECIMAL ;

fragment SIGN: [+-] ;


//skip
WS: [ \t\b\f\r\n]+ -> skip; // skip spaces, tabs, newlines
BLOCKCOMMENT: '##' .*? '##'-> skip;


//error
UNCLOSE_STRING: '"' STR_CHAR* 
	{
		y = str(self.text)
		possible = ['\n', '\r']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	;
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;
fragment STR_CHAR: ~[\n\r"\\EOF] | ESC_ACCEPT | '\'"' ;
fragment ESC_ACCEPT: '\\' [btnfr'\\] ;
fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] ;
ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;
