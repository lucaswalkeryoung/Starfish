# -------------------------------------------------------------------------------------------------
# ---------------------- Ontology :: Shorthand :: Abstract :: Shorthand ABC -----------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# --------------------------------------- ABC :: Shorthand ----------------------------------------
# -------------------------------------------------------------------------------------------------
class Shorthand(Node):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Shorthand':

        try:
            return visitor.visit_shorthand(self, context)

        except AttributeError:
            return super().visit(visitor, context)