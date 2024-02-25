from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return Program(ctx.stms().accept(self))

    # Visit a parse tree produced by ZCodeParser#stms.
    def visitStms(self, ctx:ZCodeParser.StmsContext):
        if ctx.getChildCount() == 0:
            return []
        return ctx.stm_lists().accept(self)

    # Visit a parse tree produced by ZCodeParser#stm_lists.
    def visitStm_lists(self, ctx:ZCodeParser.Stm_listsContext):
        if not ctx.null_lines():
            return [ctx.stm().accept(self)]
        return [ctx.stm().accept(self)] + ctx.stm_lists().accept(self)

    # Visit a parse tree produced by ZCodeParser#stm.
    def visitStm(self, ctx:ZCodeParser.StmContext):
        return ctx.getChild(0).accept(self)

    # Visit a parse tree produced by ZCodeParser#r_break.
    def visitR_break(self, ctx:ZCodeParser.R_breakContext):
        return Break()

    # Visit a parse tree produced by ZCodeParser#r_continue.
    def visitR_continue(self, ctx:ZCodeParser.R_continueContext):
        return Continue()

    # Visit a parse tree produced by ZCodeParser#r_return.
    def visitR_return(self, ctx:ZCodeParser.R_returnContext):
        if ctx.expr():
            return Return(ctx.expr().accept(self))
        return Return(None)

    # Visit a parse tree produced by ZCodeParser#r_if.
    def visitR_if(self, ctx:ZCodeParser.R_ifContext):
        expr = ctx.expr().accept(self)
        then = ctx.stm().accept(self)
        elifs = []
        if ctx.r_elifs():
            elifs = ctx.r_elifs().accept(self)
        elseStm = None
        if ctx.r_else():
            elseStm = ctx.r_else().accept(self)
        return If(expr, then, elifs, elseStm)

    # Visit a parse tree produced by ZCodeParser#r_elifs.
    def visitR_elifs(self, ctx:ZCodeParser.R_elifsContext):
        if not ctx.r_elifs():
            return [ctx.r_elif().accept(self)]
        return [ctx.r_elif().accept(self)] + ctx.r_elifs().accept(self)

    # Visit a parse tree produced by ZCodeParser#r_elif.
    def visitR_elif(self, ctx:ZCodeParser.R_elifContext):
        return (ctx.expr().accept(self), ctx.stm().accept(self))

    # Visit a parse tree produced by ZCodeParser#r_else.
    def visitR_else(self, ctx:ZCodeParser.R_elseContext):
        return ctx.stm().accept(self)

    # Visit a parse tree produced by ZCodeParser#r_for.
    def visitR_for(self, ctx:ZCodeParser.R_forContext):
        name = Id(ctx.IDENTIFIER().getText())
        condExpr = ctx.expr()[0].accept(self)
        updExpr = ctx.expr()[1].accept(self)
        body = ctx.stm().accept(self)
        return For(name, condExpr, updExpr, body)

    # Visit a parse tree produced by ZCodeParser#block.
    def visitBlock(self, ctx:ZCodeParser.BlockContext):
        if ctx.block_stms():
            return Block(ctx.block_stms().accept(self))
        return Block([])

    # Visit a parse tree produced by ZCodeParser#block_stms.
    def visitBlock_stms(self, ctx:ZCodeParser.Block_stmsContext):
        if not ctx.block_stms():
            return [ctx.stm().accept(self)]
        return [ctx.stm().accept(self)] + ctx.block_stms().accept(self)

    # Visit a parse tree produced by ZCodeParser#func.
    def visitFunc(self, ctx:ZCodeParser.FuncContext):
        name = Id(ctx.IDENTIFIER().getText())
        param = ctx.arg_group().accept(self)
        body = None
        if ctx.r_return():
            body = ctx.r_return().accept(self)
        elif ctx.block():
            body = ctx.block().accept(self)
        return FuncDecl(name, param, body)

    # Visit a parse tree produced by ZCodeParser#arg_group.
    def visitArg_group(self, ctx:ZCodeParser.Arg_groupContext):
        return ctx.args().accept(self)

    # Visit a parse tree produced by ZCodeParser#args.
    def visitArgs(self, ctx:ZCodeParser.ArgsContext):
        if ctx.getChildCount() == 0:
            return []
        return ctx.arg_list().accept(self)

    # Visit a parse tree produced by ZCodeParser#arg_list.
    def visitArg_list(self, ctx:ZCodeParser.Arg_listContext):
        if ctx.COMMA():
            return [ctx.arg().accept(self)]
        return [ctx.arg().accept(self)] + ctx.arg_list().accept(self)

    # Visit a parse tree produced by ZCodeParser#arg.
    def visitArg(self, ctx:ZCodeParser.ArgContext):
        name = ctx.IDENTIFIER().getText()
        varType = None
        if ctx.TYPE():
            _type = ctx.TYPE().getText()
            if _type == 'number':
                varType = NumberType()
            elif _type == 'string':
                varType = StringType()
            else:
                varType = BoolType()
        if ctx.type_index():
            varType = ArrayType(ctx.type_index().accept(self), varType)
        modifier = (ctx.DYN() and ctx.DYN().getText()) or (ctx.VAR() and ctx.VAR().getText())
        varInit = ctx.expr() and ctx.expr().accept(self)
        return VarDecl(name, varType, modifier, varInit)

    # Visit a parse tree produced by ZCodeParser#type_index.
    def visitType_index(self, ctx:ZCodeParser.Type_indexContext):
        return ctx.type_index_nums().accept(self)

    # Visit a parse tree produced by ZCodeParser#type_index_nums.
    def visitType_index_nums(self, ctx:ZCodeParser.Type_index_numsContext):
        if ctx.getChildCount() == 0:
            return []
        return ctx.type_index_num_list().accept(self)

    # Visit a parse tree produced by ZCodeParser#type_index_num_list.
    def visitType_index_num_list(self, ctx:ZCodeParser.Type_index_num_listContext):
        if not ctx.COMMA():
            return [float(ctx.NUMBER().getText())]
        return [float(ctx.NUMBER().getText())] + ctx.type_index_num_list().accept(self)

    # Visit a parse tree produced by ZCodeParser#ass.
    def visitAss(self, ctx:ZCodeParser.AssContext):
        return Assign(ctx.expr()[0].accept(self), ctx.expr()[1].accept(self))

    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        name = Id(ctx.IDENTIFIER().getText())
        varType = None
        if ctx.TYPE():
            _type = ctx.TYPE().getText()
            if _type == 'number':
                varType = NumberType()
            elif _type == 'string':
                varType = StringType()
            else:
                varType = BoolType()
        if ctx.type_index():
            varType = ArrayType(ctx.type_index().accept(self), varType)
        modifier = (ctx.DYN() and ctx.DYN().getText()) or (ctx.VAR() and ctx.VAR().getText())
        varInit = ctx.expr() and ctx.expr().accept(self)
        return VarDecl(name, varType, modifier, varInit)

    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        if ctx.op:
            return BinaryOp(ctx.op.text, ctx.expr1()[0].accept(self), ctx.expr1()[1].accept(self))
        return ctx.expr1()[0].accept(self)

    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        if ctx.op:
            return BinaryOp(ctx.op.text, ctx.expr2()[0].accept(self), ctx.expr2()[1].accept(self))
        return ctx.expr2()[0].accept(self)

    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        if ctx.op:
            return BinaryOp(ctx.op.text, ctx.expr2().accept(self), ctx.expr3().accept(self))
        return ctx.expr3().accept(self)

    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        if ctx.op:
            return BinaryOp(ctx.op.text, ctx.expr3().accept(self), ctx.expr4().accept(self))
        return ctx.expr4().accept(self)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        if ctx.op:
            return BinaryOp(ctx.op.text, ctx.expr4().accept(self), ctx.expr5().accept(self))
        return ctx.expr5().accept(self)

    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        if ctx.SUB():
            return UnaryOp('-', ctx.expr5().accept(self))
        if ctx.NOT():
            return UnaryOp('not', ctx.expr5().accept(self))
        return ctx.expr6().accept(self)

    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        if ctx.LB():
            return ArrayCell(ctx.expr6().accept(self), ctx.expr_list().accept(self))
        if ctx.LP():
            return CallExpr(ctx.expr6().accept(self), ctx.expr_list().accept(self))
        if ctx.term():
            return ctx.term().accept(self)


    # Visit a parse tree produced by ZCodeParser#term.
    def visitTerm(self, ctx:ZCodeParser.TermContext):
        if ctx.NUMBER():
            return NumberLiteral(float(ctx.NUMBER().getText()))
        if ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        if ctx.BOOLEAN():
            return BooleanLiteral(True if ctx.BOOLEAN().getText() == 'true' else False)
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        if ctx.LB():
            return ArrayLiteral(ctx.expr_list().accept(self))
        if ctx.LP():
            return ctx.expr().accept(self)


    # Visit a parse tree produced by ZCodeParser#expr_list.
    def visitExpr_list(self, ctx:ZCodeParser.Expr_listContext):
        if ctx.getChildCount() == 0:
            return []
        return ctx.exprs().accept(self)


    # Visit a parse tree produced by ZCodeParser#exprs.
    def visitExprs(self, ctx:ZCodeParser.ExprsContext):
        if not ctx.COMMA():
            return [ctx.expr().accept(self)]
        return [ctx.expr().accept(self)] + ctx.exprs().accept(self)


    # Visit a parse tree produced by ZCodeParser#null_lines.
    def visitNull_lines(self, ctx:ZCodeParser.Null_linesContext):
        return None

