# -------------------------------------------------------------------------------------------------
# -------------------------------- Ontology :: Logic :: Logic ABC ---------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ----------------------------------------- ABC :: Logic ------------------------------------------
# -------------------------------------------------------------------------------------------------
class Logic(Node):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Logic':

        if visit := getattr(visitor, 'visit_logic', None):
            return visit(self, context)

        return super().visit(visitor, context)
