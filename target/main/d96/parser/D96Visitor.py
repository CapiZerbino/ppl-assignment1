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


    # Visit a parse tree produced by D96Parser#attributename_list.
    def visitAttributename_list(self, ctx:D96Parser.Attributename_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute_init.
    def visitAttribute_init(self, ctx:D96Parser.Attribute_initContext):
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


    # Visit a parse tree produced by D96Parser#primitive_types.
    def visitPrimitive_types(self, ctx:D96Parser.Primitive_typesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression_list.
    def visitExpression_list(self, ctx:D96Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_1.
    def visitExpr_1(self, ctx:D96Parser.Expr_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_2.
    def visitExpr_2(self, ctx:D96Parser.Expr_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_3.
    def visitExpr_3(self, ctx:D96Parser.Expr_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_4.
    def visitExpr_4(self, ctx:D96Parser.Expr_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_5.
    def visitExpr_5(self, ctx:D96Parser.Expr_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_6.
    def visitExpr_6(self, ctx:D96Parser.Expr_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_7.
    def visitExpr_7(self, ctx:D96Parser.Expr_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_8.
    def visitExpr_8(self, ctx:D96Parser.Expr_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_9.
    def visitExpr_9(self, ctx:D96Parser.Expr_9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_10.
    def visitExpr_10(self, ctx:D96Parser.Expr_10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_11.
    def visitExpr_11(self, ctx:D96Parser.Expr_11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#operands.
    def visitOperands(self, ctx:D96Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#call_expr.
    def visitCall_expr(self, ctx:D96Parser.Call_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ctx:D96Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#postfix.
    def visitPostfix(self, ctx:D96Parser.PostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#postfix_array.
    def visitPostfix_array(self, ctx:D96Parser.Postfix_arrayContext):
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


    # Visit a parse tree produced by D96Parser#array_decl.
    def visitArray_decl(self, ctx:D96Parser.Array_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#element_type.
    def visitElement_type(self, ctx:D96Parser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_expression.
    def visitIndex_expression(self, ctx:D96Parser.Index_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_op.
    def visitIndex_op(self, ctx:D96Parser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_list.
    def visitStmt_list(self, ctx:D96Parser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl_stmt.
    def visitVardecl_stmt(self, ctx:D96Parser.Vardecl_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_init.
    def visitVar_init(self, ctx:D96Parser.Var_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varname_list.
    def visitVarname_list(self, ctx:D96Parser.Varname_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:D96Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_lhs.
    def visitAssign_lhs(self, ctx:D96Parser.Assign_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assign_tail.
    def visitAssign_tail(self, ctx:D96Parser.Assign_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forin_stmt.
    def visitForin_stmt(self, ctx:D96Parser.Forin_stmtContext):
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


    # Visit a parse tree produced by D96Parser#bool_lit.
    def visitBool_lit(self, ctx:D96Parser.Bool_litContext):
        return self.visitChildren(ctx)



del D96Parser