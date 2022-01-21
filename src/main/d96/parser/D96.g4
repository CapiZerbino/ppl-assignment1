/* 1852611 */ 
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

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
EQD: '==.';
PDOT: '+.';
DCL: '::';

/* Seperators */
LP : '(';
RP : ')';
LSB : '[';
RSB : ']';
LCB : '{';
RCB : '}';
SM : ';';
CM : ',';
fragment DOT: '.';
CL: ':';

fragment DIGIT: [0-9];

fragment DIGITNONZERO: [1-9];

SDIGIT:  DIGIT+;

fragment EXPONENT: [eE] SIGN? DIGIT+ ;

fragment SIGN: [+-] ;


/* 2. PROGRAM STRUCTURE */
program:  class_decl* class_init EOF;

class_init
	: CLASS 'Program' LCB body RCB
	;

body: 'main' LP RP LCB stmt_list* RCB;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
/* Class declaration */
class_decl
	: CLASS classname LCB classbody RCB
	;

classname
	: IDENTIFIER(':'IDENTIFIER)?
	;

classbody
	:(attribute_decl | method_decl)*
	;

/* Attribute declaration */
attribute_decl
	: attributetype attributename_list CL datatype SM
	;

datatype
	: (INT | FLOAT | BOOLEAN)
	;

attribute_init
	: (ASSIGN expression_list)?
	;

attributetype
	: VAL | VAR
	;

attributename_list
	: ID_normal (','ID_normal)*
	| ID_static (','ID_static)*
	;


/* Method declaration */
method_decl
	:(IDENTIFIER|CONSTRUCTOR) LP parameter_list? RP block_stmt
	| DESTRUCTOR LP RP block_stmt
	;

parameter_list
	: parameter (SM parameter)*
	;

parameter
	: IDENTIFIER (','IDENTIFIER)* CL datatype
	;

/* 3. LEXICAL STRUCTURE */
/* Characters set */

/* Program comment */	
BLOCKCOMMENT
	: '##' .*? '##'
	-> skip
	;
	
/* Identifiers */
/* used to name variables, constants, classes, methods and parameters */
IDENTIFIER
	: ID_normal
	| ID_static
	;

ID_normal
	: [a-zA-Z_][a-zA-Z0-9_]*
	;

ID_static
	: '$'[a-zA-Z_][a-zA-Z0-9_]*
	;




/* Literals */
literals
	: INT_LIT
	| FLOAT_LIT
	| BOOL_LIT
	| STRING_LIT
	| array_lit
	;

INT_LIT
	: (DecimalConstant
	| OctalConstant
	| HexadecimalConstant
	| BinaryConstant){self.text = self.text.replace("_", "")}
	;

DecimalConstant
	: [1-9][0-9]*('_'[0-9]+)*
    | '0'
	;

OctalConstant
	: '0' [0-7]+('_'[0-7]+)*
	;

HexadecimalConstant
	: HexadecimalPrefix HexadecimalDigit+
	;

BinaryConstant
	: '0' [bB] [01]+('_'[01]+)*
	;

HexadecimalPrefix
    : '0' [xX]
    ;

HexadecimalDigit
    : [0-9A-F]+('_'[0-9A-F]+)*
    ;

FLOAT_LIT
	: (DecimalConstant+ DOT (DecimalConstant | EXPONENT)* // 1 | 1.5 | 1.e-4
	| DecimalConstant+ DOT DecimalConstant+ EXPONENT? // (1).5(e-4)
	| DecimalConstant+ EXPONENT // 12e-5
	| DOT DecimalConstant* EXPONENT?
	){self.text = self.text.replace("_", "")}
	;

BOOL_LIT
	: TRUE | FALSE
	;

STRING_LIT:  '"' STR_CHAR* '"'{y = str(self.text)
self.text = y[1:-1]
	}
	;

array_lit
	: ARRAY LP array_list? RP
	;

array_list
	: arrayitemint_list
	| arrayitemfloat_list
	| arrayitembool_list
	| arrayitemstring_list
	| arrayitemarray_list
	;

arrayitemint_list
	: INT_LIT(','INT_LIT)*
	;

arrayitemfloat_list
	:FLOAT_LIT(','FLOAT_LIT)* 
	;

arrayitembool_list
	:BOOL_LIT(','BOOL_LIT)*
	;

arrayitemstring_list
	:STRING_LIT(','STRING_LIT)*
	;

arrayitemarray_list
	:array_lit(','array_lit)*
	;

/* 4.TYPE AND VALUE */

/* Primitive types */
primitive_types
	: BOOLEAN | INT | FLOAT |  STRING
	;

/* Array declaration */
array_decl
	: ARRAY LSB element_type CM SDIGIT RSB
	;

element_type
	: (primitive_types | ARRAY)
	;

array_element
	:ARRAY LSB SDIGIT RSB
	;



/* 5.EXPRESSIONS */
expression
	:'expr'
	;

factor
	: 
	IDENTIFIER
	| 
	;
/* Arithmetic operators */
arith_operator
	: MINUS | PLUS | STAR | MOD
	;

/* Boolean operators */
bool_operator
	: NOT | ANDAND | OROR | EQD
	;

/* String operators */
concat_operator
	: PDOT;

/* Relational operators */
rela_operator
	: EQ | NE | LS | GT | LE | GE
	;

/* Index operators */


/* Member access */

/* Object creation */
object_decl
	: NEW IDENTIFIER LP expression_list? RP SM
	;

expression_list
	:expression (CM expression)*
	;

/* Self */

/* Operator precedence and associativity */

/* Type coercions */

/* 6.STATEMENTS */
stmt_list
	:varconstdecl_stmt
	|assign_stmt
	|if_stmt
	|forin_stmt
	|break_stmt
	|continue_stmt
	|return_stmt
	|methodinvocation_stmt
	|block_stmt
	;

varconstdecl_stmt
	:attributetype varconstname_list CL datatype SM
	;
varconstname_list
	: ID_normal (','ID_normal)*
	;

assign_stmt
	: expression ASSIGN expression SM
	;

if_stmt
	: IF LP expression RP block_stmt (ELSEIF LP expression RP block_stmt)* (ELSE block_stmt)?
	;

forin_stmt
	: FOREACH LP scalar_var IN expr1 '..' expr2 (LP BY expr3 RP)?RP block_stmt
	;

scalar_var
	:VAL
	;

expr1
	:VAL
	;

expr2
	:VAL
	;

expr3
	:VAL
	;


break_stmt
	: BREAK SM
	;

continue_stmt
	: CONTINUE SM
	;

return_stmt
	: RETURN expression? SM
	;

methodinvocation_stmt
	:VAL
	;

block_stmt
	: LCB block_stmt* RCB
	;



ERROR_CHAR: .{raise ErrorToken(self.text)};
// UNCLOSE_STRING: '"' STR_CHAR* ([\b\t\n\f\r"'\\] | EOF){
// 		y = str(self.text)
// 		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
// 		if y[-1] in possible:
// 			raise UncloseString(y[1:-1])
// 		else:
// 			raise UncloseString(y[1:]) 
// };
// ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
// 	{
// 		y = str(self.text)
// 		raise IllegalEscape(y[1:])
// 	}
// 	;

STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;

fragment ESC_SEQ: '\\' [btnfr"'\\] ;

fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ; 

