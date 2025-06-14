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

        try:
            return visitor.visit_phase(self, context)

        except AttributeError:
            return super().visit(visitor, context)