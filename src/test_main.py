from antlr4 import *
from antlr_files.AutomataLexer import AutomataLexer
from antlr_files.AutomataParser import AutomataParser
from antlr4.tree.Trees import Trees


def main():
    # Read example file content
    with open("examples/example1.txt", 'r') as file:
        data = file.read()

    data_stream = InputStream(data)
    # lexer
    lexer = AutomataLexer(data_stream)
    stream = CommonTokenStream(lexer)
    # parser
    parser = AutomataParser(stream)
    # Run parser
    tree = parser.s()
    # Print tree
    print(Trees.toStringTree(tree, None, parser))


if __name__ == "__main__":
    main()
