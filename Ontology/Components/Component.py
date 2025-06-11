# -------------------------------------------------------------------------------------------------
# ---------------------------- Ontology :: Components :: Component ABC ----------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# --------------------------------------- ABC :: Component ----------------------------------------
# -------------------------------------------------------------------------------------------------
class Component(Node):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Component':

        try:
            return visitor.visit_component(self, context)

        except AttributeError:
            return super().visit(visitor, context)