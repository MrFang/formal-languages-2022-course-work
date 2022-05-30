from antlr4 import *
from antlr_files.AutomataLexer import AutomataLexer
from antlr_files.AutomataParser import AutomataParser
from antlr_files.AutomataVisitor import AutomataVisitor

from antlr4.tree.Trees import Trees




class MyAutomataVisitor(AutomataVisitor):

    # Visit a parse tree produced by AutomataParser#s.
    def visitS(self, ctx:AutomataParser.SContext):
        return ctx


    # Visit a parse tree produced by AutomataParser#line.
    def visitLine(self, ctx:AutomataParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#expr.
    def visitExpr(self, ctx:AutomataParser.ExprContext):
        return self


    # Visit a parse tree produced by AutomataParser#alternative.
    def visitAlternative(self, ctx:AutomataParser.AlternativeContext):
        return self


    # Visit a parse tree produced by AutomataParser#non_alternative.
    def visitNon_alternative(self, ctx:AutomataParser.Non_alternativeContext):
        return self


    # Visit a parse tree produced by AutomataParser#parentheses.
    def visitParentheses(self, ctx:AutomataParser.ParenthesesContext):
        return self


    # Visit a parse tree produced by AutomataParser#plus.
    def visitPlus(self, ctx:AutomataParser.PlusContext):
        return self


    # Visit a parse tree produced by AutomataParser#star.
    def visitStar(self, ctx:AutomataParser.StarContext):
        return self


    # Visit a parse tree produced by AutomataParser#maybe.
    def visitMaybe(self, ctx:AutomataParser.MaybeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#simple_expr.
    def visitSimple_expr(self, ctx:AutomataParser.Simple_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AutomataParser#symbol.
    def visitSymbol(self, ctx:AutomataParser.SymbolContext):
        return self.visitChildren(ctx)





def main():
    # Пробуем разобрать правильный автомат
    with open("examples/example2.txt", 'r') as correct_file:
        data = correct_file.read()

    data_stream = InputStream(data)
    # lexer
    lexer = AutomataLexer(data_stream)
    stream = CommonTokenStream(lexer)
    # parser
    parser = AutomataParser(stream)
    tree = parser.s()

    # evaluator

    # children = tree.getChildren()
    # for child in children:
    #     print(child.getSymbol())
    #     print(child.getText())

    # print(tree.line())
    # print(tree.getText())
    visitor = MyAutomataVisitor()
    # visitor.visitS(tree)
    node = visitor.visit(tree)

    # print("---" * 30)
    # print("Built-in print:")
    print(Trees.toStringTree(tree, None, parser))


if __name__ == "__main__":
    main()
