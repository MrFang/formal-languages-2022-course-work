import unittest

from src.Graph import Graph


class GraphTest(unittest.TestCase):
    def test_merge(self):
        graph_a = Graph()
        graph_a.add_vertex(1)
        graph_a.add_vertex(2)
        graph_a.add_edge(1, 2, 'a')

        graph_b = Graph()
        graph_b.add_vertex(1)
        graph_b.add_vertex(3)
        graph_b.add_edge(1, 3, 'b')

        merged = Graph.merge_graphs([graph_a, graph_b])

        self.assertFalse(merged.add_vertex(1))
        self.assertFalse(merged.add_vertex(2))
        self.assertFalse(merged.add_vertex(3))
        self.assertFalse(merged.add_edge(1, 2, 'a'))
        self.assertFalse(merged.add_edge(1, 3, 'b'))


if __name__ == '__main__':
    unittest.main()
