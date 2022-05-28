import unittest

from src.ASTNode import ASTNode, ASTNodeType
from src.main import traverse_ast


class TestTraverse(unittest.TestCase):
    def test_traverse_primitive(self):
        a = traverse_ast(ASTNode(
            ASTNodeType.PRIMITIVE,
            [],
            'S'
        ))
        self.assertFalse(a.add_edge(a.begin_state, a.end_state, 'S'))

    '''
    Нормальных тестов, пока, больше не будет, т.к. у автоматов неудобный API для тестирования
    '''


if __name__ == '__main__':
    unittest.main()
