# -------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Shorthand :: Explorand Mixin ----------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# --------------------------------------- ABC :: Explorand ----------------------------------------
# -------------------------------------------------------------------------------------------------
class Explorand(Node):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Explorand':

        if visit := getattr(visitor, 'visit_explorand', None):
            return visit(self, context)

        return super().visit(visitor, context)
