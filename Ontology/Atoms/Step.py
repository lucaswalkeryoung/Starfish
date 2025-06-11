# -------------------------------------------------------------------------------------------------
# -------------------------------- Ontology :: Components :: Step ---------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Components.Component import Component
from Ontology.Abstract.Node import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Ontology.Objects.Player import Player
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# --------------------------------------- Component :: Step ---------------------------------------
# -------------------------------------------------------------------------------------------------
class Step(Component):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Step':

        try:
            return visitor.visit_step(self, context)

        except AttributeError:
            return super().visit(visitor, context)

    @property
    def player(self) -> 'Player':
        return self.edges['possessor'][0]