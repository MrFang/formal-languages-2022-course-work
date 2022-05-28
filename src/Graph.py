from __future__ import annotations
from typing import List


class Graph:
    def __init__(self):
        self.__data = {}

    def add_vertex(self, vertex_id: int) -> bool:
        if self.__data.get(vertex_id) is not None:
            return False

        self.__data[vertex_id] = []
        return True

    def add_edge(self, from_id: int, to_id: int, label: str) -> bool:
        if self.__data.get(from_id) is None or self.__data.get(to_id) is None:
            return False

        for pair in self.__data[from_id]:
            if pair[0] == to_id and pair[1] == label:
                return False

        self.__data[from_id].append((to_id, label))
        return True

    @staticmethod
    def merge_graphs(graphs: List[Graph]) -> Graph:
        new_g = Graph()

        for g in graphs:
            for v in g.__data.keys():
                new_g.add_vertex(v)

        for g in graphs:
            for v in g.__data.keys():
                for e in g.__data[v]:
                    new_g.add_edge(v, e[0], e[1])
        return new_g
