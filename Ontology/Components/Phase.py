# -------------------------------------------------------------------------------------------------
# -------------------------------- Ontology :: Components :: Phase --------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Components.Component import Component
from Ontology.Abstract.Node import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# -------------------------------------- Component :: Phase ---------------------------------------
# -------------------------------------------------------------------------------------------------
class Phase(Component):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Phase':

        if visit := getattr(visitor, 'visit_phase', None):
            return visit(self, context)

        return super().visit(visitor, context)
