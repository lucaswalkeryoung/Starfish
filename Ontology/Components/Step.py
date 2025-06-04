# -------------------------------------------------------------------------------------------------
# -------------------------------- Ontology :: Components :: Step ---------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Components.Component import Component
from Ontology.Abstract.Node  import Node

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

        if visit := getattr(visitor, 'visit_step', None):
            return visit(self, context)

        return super().visit(visitor, context)

    @property
    def player(self) -> 'Player':
        return self.edges['possessor'][0]

    @property
    def prev(self) -> str:
        return self.edges['prev'][0]

    @property
    def next(self) -> str:
        return self.edges['next'][0]

    @property
    def name(self) -> str:
        return list(self.attributes.keys())[0]