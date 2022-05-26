from __future__ import annotations
from enum import Enum
from typing import List


class ASTNodeType(Enum):
    PRIMITIVE = 'primitive'
    MAYBE = 'maybe'
    ALTERNATIVE = 'alternative'
    MULTIPLE = 'multiple'
    BRACKETS = 'brackets'


class ASTNode:
    def __int__(self, node_type: ASTNodeType, children: List[ASTNode] = [], data=''):
        self.children = children
        self.node_type = node_type
        self.data = data
