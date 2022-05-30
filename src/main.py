import sys
from antlr4 import InputStream, CommonTokenStream
from antlr_files.AutomataLexer import AutomataLexer
from antlr_files.AutomataParser import AutomataParser
from antlr4.tree.Trees import Trees
from src.ExprVisitor import ExprVisitor


def main():
    # Пробуем разобрать правильный автомат
    with open(sys.argv[1], 'r') as correct_file:
        data = correct_file.read()

    data_stream = InputStream(data)
    # lexer
    lexer = AutomataLexer(data_stream)
    stream = CommonTokenStream(lexer)
    # parser
    parser = AutomataParser(stream)
    tree = parser.s()

    visitor = ExprVisitor()
    automatons = visitor.visit(tree)
    for a in automatons:
        a.visualise()


if __name__ == "__main__":
    main()
