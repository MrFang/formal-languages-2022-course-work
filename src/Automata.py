from __future__ import annotations
from typing import List
from src.Graph import Graph


class Automata:
    EPSILON_LABEL = '__EPSILON__'

    def __init__(self):
        self.__graph = Graph()
        self.begin_state = None
        self.end_state = None

    def add_state(self, state_id: int) -> bool:
        return self.__graph.add_vertex(state_id)

    def add_edge(self, from_state_id: int, to_state_id: int, label: str) -> bool:
        return self.__graph.add_edge(from_state_id, to_state_id, label)

    @staticmethod
    def merge_automatons(automatons: List[Automata], new_begin_state: int, new_end_state: int) -> Automata:
        begin_states = [a.begin_state for a in automatons]
        end_states = [a.end_state for a in automatons]
        new_automata = Automata()
        new_automata.__graph = Graph.merge_graphs([a.__graph for a in automatons])
        new_automata.add_state(new_begin_state)
        new_automata.begin_state = new_begin_state

        for s in begin_states:
            new_automata.add_edge(new_begin_state, s, Automata.EPSILON_LABEL)

        new_automata.add_state(new_end_state)
        new_automata.end_state = new_end_state

        for s in end_states:
            new_automata.add_edge(s, new_end_state, Automata.EPSILON_LABEL)

        return new_automata
