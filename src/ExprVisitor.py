from typing import List

from src.Automata import Automata
from src.IdGenerator import IdGenerator
from src.antlr_files.AutomataParser import AutomataParser
from src.antlr_files.AutomataVisitor import AutomataVisitor


class ExprVisitor(AutomataVisitor):
    def __init__(self):
        super(ExprVisitor, self).__init__()
        self.__gen = IdGenerator.instance()

    def defaultResult(self) -> List[Automata]:
        return []

    def aggregateResult(self, aggregate, next_result) -> List[Automata]:
        if isinstance(next_result, list):
            return aggregate + next_result
        else:
            return aggregate + [next_result]

    def visitExpr(self, ctx: AutomataParser.ExprContext) -> Automata:
        return Automata.concat_automatons(self.visitChildren(ctx))

    def visitNon_alternative(self, ctx:AutomataParser.Non_alternativeContext):
        return Automata.concat_automatons(self.visitChildren(ctx))

    def visitAlternative(self, ctx: AutomataParser.AlternativeContext) -> Automata:
        automatons = self.visitChildren(ctx)

        new_begin = next(self.__gen)
        new_end = next(self.__gen)
        return Automata.merge_automatons(automatons, new_begin, new_end)

    def visitStar(self, ctx: AutomataParser.StarContext) -> Automata:
        automatons = self.visitChildren(ctx)

        auto = automatons[0]
        start_id = next(self.__gen)
        end_id = next(self.__gen)

        auto.add_state(start_id)
        auto.add_edge(start_id, auto.begin_state, Automata.EPSILON_LABEL)
        auto.add_state(end_id)
        auto.add_edge(auto.end_state, end_id, Automata.EPSILON_LABEL)
        auto.add_edge(end_id, start_id, Automata.EPSILON_LABEL)
        auto.add_edge(start_id, end_id, Automata.EPSILON_LABEL)
        auto.begin_state = start_id
        auto.end_state = end_id

        return auto

    def visitMaybe(self, ctx: AutomataParser.MaybeContext) -> Automata:
        automatons = self.visitChildren(ctx)

        auto = automatons[0]
        start_id = next(self.__gen)
        end_id = next(self.__gen)

        auto.add_state(start_id)
        auto.add_edge(start_id, auto.begin_state, Automata.EPSILON_LABEL)
        auto.add_state(end_id)
        auto.add_edge(auto.end_state, end_id, Automata.EPSILON_LABEL)
        auto.add_edge(start_id, end_id, Automata.EPSILON_LABEL)
        auto.begin_state = start_id
        auto.end_state = end_id

        return auto

    def visitSimple_expr(self, ctx: AutomataParser.Simple_exprContext) -> Automata:
        text = ctx.getText()
        text = text[1:-1] if text.startswith('"') else text
        text = text.replace('\\', '')

        auto = Automata()
        new_id = next(self.__gen)
        auto.add_state(new_id)
        auto.begin_state = new_id

        for char in text:
            last_id = new_id
            new_id = next(self.__gen)
            auto.add_state(new_id)
            auto.add_edge(last_id, new_id, char)

        auto.end_state = new_id

        return auto



