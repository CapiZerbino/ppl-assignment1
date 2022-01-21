# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_init.
    def visitClass_init(self, ctx:D96Parser.Class_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#body.
    def visitBody(self, ctx:D96Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_decl.
    def visitClass_decl(self, ctx:D96Parser.Class_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classname.
    def visitClassname(self, ctx:D96Parser.ClassnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classbody.
    def visitClassbody(self, ctx:D96Parser.ClassbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_decl.
    def visitAttribute_decl(self, ctx:D96Parser.Attribute_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#datatype.
    def visitDatatype(self, ctx:D96Parser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_init.
    def visitAttribute_init(self, ctx:D96Parser.Attribute_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attributetype.
    def visitAttributetype(self, ctx:D96Parser.AttributetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attributename_list.
    def visitAttributename_list(self, ctx:D96Parser.Attributename_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_decl.
    def visitMethod_decl(self, ctx:D96Parser.Method_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter_list.
    def visitParameter_list(self, ctx:D96Parser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#parameter.
    def visitParameter(self, ctx:D96Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literals.
    def visitLiterals(self, ctx:D96Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_lit.
    def visitArray_lit(self, ctx:D96Parser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_list.
    def visitArray_list(self, ctx:D96Parser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayitemint_list.
    def visitArrayitemint_list(self, ctx:D96Parser.Arrayitemint_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayitemfloat_list.
    def visitArrayitemfloat_list(self, ctx:D96Parser.Arrayitemfloat_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayitembool_list.
    def visitArrayitembool_list(self, ctx:D96Parser.Arrayitembool_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayitemstring_list.
    def visitArrayitemstring_list(self, ctx:D96Parser.Arrayitemstring_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayitemarray_list.
    def visitArrayitemarray_list(self, ctx:D96Parser.Arrayitemarray_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#primitive_types.
    def visitPrimitive_types(self, ctx:D96Parser.Primitive_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_decl.
    def visitArray_decl(self, ctx:D96Parser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_type.
    def visitElement_type(self, ctx:D96Parser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_element.
    def visitArray_element(self, ctx:D96Parser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#factor.
    def visitFactor(self, ctx:D96Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arith_operator.
    def visitArith_operator(self, ctx:D96Parser.Arith_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bool_operator.
    def visitBool_operator(self, ctx:D96Parser.Bool_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#concat_operator.
    def visitConcat_operator(self, ctx:D96Parser.Concat_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#rela_operator.
    def visitRela_operator(self, ctx:D96Parser.Rela_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#object_decl.
    def visitObject_decl(self, ctx:D96Parser.Object_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression_list.
    def visitExpression_list(self, ctx:D96Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_list.
    def visitStmt_list(self, ctx:D96Parser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varconstdecl_stmt.
    def visitVarconstdecl_stmt(self, ctx:D96Parser.Varconstdecl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forin_stmt.
    def visitForin_stmt(self, ctx:D96Parser.Forin_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_var.
    def visitScalar_var(self, ctx:D96Parser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr1.
    def visitExpr1(self, ctx:D96Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr2.
    def visitExpr2(self, ctx:D96Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr3.
    def visitExpr3(self, ctx:D96Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D96Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodinvocation_stmt.
    def visitMethodinvocation_stmt(self, ctx:D96Parser.Methodinvocation_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)



del D96Parser