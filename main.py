from ASTNode import ASTNode, ASTNodeType
from Automata import Automata


def id_generator() -> int:
    _id = 0

    while True:
        yield _id
        _id += 1


def traverse_ast(tree: ASTNode) -> Automata:
    automatons = [traverse_ast(child) for child in tree.children]

    if tree.node_type == ASTNodeType.PRIMITIVE:
        assert len(automatons) == 0

        auto = Automata()
        new_id = id_generator()
        auto.add_state(new_id)
        auto.begin_state = new_id

        for char in tree.data:
            last_id = new_id
            new_id = id_generator()
            auto.add_edge(last_id, new_id, char)

        auto.end_state = new_id

        return auto
    elif tree.node_type == ASTNodeType.BRACKETS:
        assert len(automatons) == 1
        return automatons[0]
    elif tree.node_type == ASTNodeType.MAYBE:
        assert len(automatons) == 1

        auto = automatons[0]
        start_id = id_generator()
        end_id = id_generator()

        auto.add_state(start_id)
        auto.add_edge(start_id, auto.begin_state, Automata.EPSILON_LABEL)
        auto.add_state(end_id)
        auto.add_edge(auto.end_state, end_id, Automata.EPSILON_LABEL)
        auto.add_edge(start_id, end_id, Automata.EPSILON_LABEL)

        return auto
    elif tree.node_type == ASTNodeType.MULTIPLE:
        assert len(automatons) == 1

        auto = automatons[0]
        start_id = id_generator()
        end_id = id_generator()

        auto.add_state(start_id)
        auto.add_edge(start_id, auto.begin_state, Automata.EPSILON_LABEL)
        auto.add_state(end_id)
        auto.add_edge(auto.end_state, end_id, Automata.EPSILON_LABEL)
        auto.add_edge(end_id, start_id, Automata.EPSILON_LABEL)

        return auto
    elif tree.node_type == ASTNodeType.ALTERNATIVE:
        new_begin = id_generator()
        new_end = id_generator()
        return Automata.merge_automatons(automatons, new_begin, new_end)
