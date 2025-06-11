# -------------------------------------------------------------------------------------------------
# ------------------------------ Ontology :: Components :: Condition ------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Components.Component import Component
from Ontology.Abstract.Node import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ------------------------------------ Component :: Condition -------------------------------------
# -------------------------------------------------------------------------------------------------
class Condition(Component):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Condition':

        try:
            return visitor.visit_condition(self, context)

        except AttributeError:
            return super().visit(visitor, context)