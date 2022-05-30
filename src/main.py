import sys
from antlr4 import InputStream, CommonTokenStream
from antlr_files.AutomataLexer import AutomataLexer
from antlr_files.AutomataParser import AutomataParser
from src.ExprVisitor import ExprVisitor


def main():
    # Read file
    with open(sys.argv[1], 'r') as file:
        data = file.read()

    data_stream = InputStream(data)
    # lexer
    lexer = AutomataLexer(data_stream)
    stream = CommonTokenStream(lexer)
    # parser
    parser = AutomataParser(stream)
    # Run parser
    tree = parser.s()

    visitor = ExprVisitor()
    automatons = visitor.visit(tree)
    for a in automatons:
        a.visualise()


if __name__ == "__main__":
    main()
