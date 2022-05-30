from __future__ import annotations
from typing import List, Optional
import numpy as np
from matplotlib.lines import Line2D
from src.Graph import Graph
import networkx as nx
import matplotlib.pyplot as plt


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
    def concat_automatons(automatons: List[Automata]) -> Automata:
        assert len(automatons) > 0

        auto = Automata()
        last_end_state: Optional[int] = None

        for a in automatons:
            for s in a.__graph.vertexes():
                auto.add_state(s)
            for k, v in a.__graph.edges().items():
                auto.add_edge(k[0], k[1], v)

            if last_end_state is not None:
                auto.add_edge(last_end_state, a.begin_state, Automata.EPSILON_LABEL)

            last_end_state = a.end_state

        auto.begin_state = automatons[0].begin_state
        auto.end_state = automatons[-1].end_state

        return auto

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

    def visualise(self):
        vertexes = self.__graph.vertexes()
        edges = {
            k: v if v != Automata.EPSILON_LABEL else chr(949)
            for k, v in self.__graph.edges().items()
        }

        plt.figure(figsize=(12, 12), dpi=100)

        g = nx.MultiDiGraph()
        g.add_nodes_from(vertexes)
        g.add_edges_from(edges.keys())
        position = nx.planar_layout(g)
        begin_state_idx, end_state_idx = \
            (vertexes.index(self.begin_state), vertexes.index(self.end_state))

        colors = [
            1 if idx == begin_state_idx
            else 0.7 if idx == end_state_idx
            else 0.4
            for idx in range(len(vertexes))
        ]

        radius = 0.2

        nx.draw_networkx(
            g,
            pos=position,
            nodelist=vertexes,
            node_color=colors,
            cmap=plt.get_cmap('spring'),
            connectionstyle=f'arc3, rad = {radius}'
        )

        Automata.__draw_labels(g, pos=position, edge_labels=edges, rad=radius)

        legend_elements = [
            Line2D([0], [0], marker='o', color='green', label='Желтый - начальное состояние',
                   markerfacecolor='yellow', markersize=13),
            Line2D([0], [0], marker='o', color='green', label='Красный - терминальное состояние',
                   markerfacecolor='red', markersize=13),
            Line2D([0], [0], marker='o', color='green', label='Розовый - остальные состояния',
                   markerfacecolor='magenta', markersize=13)
        ]
        plt.legend(handles=legend_elements)
        plt.savefig(f'auto_{self.begin_state}.png', dpi=100)

    @staticmethod
    def __draw_labels(g, pos, edge_labels=None, label_pos=0.5, font_size=10, font_color="k",
                      font_family="sans-serif", font_weight="normal", alpha=None, bbox=None,
                      horizontalalignment="center", verticalalignment="center", ax=None, rotate=True,
                      clip_on=True, rad=0.0):
        if ax is None:
            ax = plt.gca()
        if edge_labels is None:
            labels = {(u, v): d for u, v, d in g.edges(data=True)}
        else:
            labels = edge_labels
        text_items = {}

        for (n1, n2), label in labels.items():
            (x1, y1) = pos[n1]
            (x2, y2) = pos[n2]
            (x, y) = (
                x1 * label_pos + x2 * (1.0 - label_pos),
                y1 * label_pos + y2 * (1.0 - label_pos),
            )
            pos_1 = ax.transData.transform(np.array(pos[n1]))
            pos_2 = ax.transData.transform(np.array(pos[n2]))
            linear_mid = 0.5 * pos_1 + 0.5 * pos_2
            d_pos = pos_2 - pos_1
            rotation_matrix = np.array([(0, 1), (-1, 0)])
            ctrl_1 = linear_mid + rad * rotation_matrix @ d_pos
            ctrl_mid_1 = 0.5 * pos_1 + 0.5 * ctrl_1
            ctrl_mid_2 = 0.5 * pos_2 + 0.5 * ctrl_1
            bezier_mid = 0.5 * ctrl_mid_1 + 0.5 * ctrl_mid_2
            (x, y) = ax.transData.inverted().transform(bezier_mid)

            if rotate:
                # in degrees
                angle = np.arctan2(y2 - y1, x2 - x1) / (2.0 * np.pi) * 360
                # make label orientation "right-side-up"
                if angle > 90:
                    angle -= 180
                if angle < -90:
                    angle += 180
                # transform data coordinate angle to screen coordinate angle
                xy = np.array((x, y))
                trans_angle = ax.transData.transform_angles(
                    np.array((angle,)), xy.reshape((1, 2))
                )[0]
            else:
                trans_angle = 0.0
            # use default box of white with white border
            if bbox is None:
                bbox = dict(boxstyle="round", ec=(1.0, 1.0, 1.0), fc=(1.0, 1.0, 1.0))
            if not isinstance(label, str):
                label = str(label)  # this makes "1" and 1 labeled the same

            t = ax.text(x, y, label, size=font_size, color=font_color, family=font_family, weight=font_weight,
                        alpha=alpha, horizontalalignment=horizontalalignment, verticalalignment=verticalalignment,
                        rotation=trans_angle, transform=ax.transData, bbox=bbox, zorder=1, clip_on=clip_on)
            text_items[(n1, n2)] = t

        ax.tick_params(axis="both", which="both", bottom=False, left=False, labelbottom=False, labelleft=False)

        return text_items


