from antlr4 import *
from antlr_files.AutomataLexer import AutomataLexer
from antlr_files.AutomataParser import AutomataParser
from antlr_files.AutomataVisitor import AutomataVisitor

from antlr4.tree.Trees import Trees


def main():
    # Пробуем разобрать правильный автомат
    with open("examples/example1.txt", 'r') as correct_file:
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
    # visitor = MyAutomataVisitor()
    # visitor.visitS(tree)
    # node = visitor.visit(tree)

    # print("---" * 30)
    # print("Built-in print:")
    print(Trees.toStringTree(tree, None, parser))


if __name__ == "__main__":
    main()
