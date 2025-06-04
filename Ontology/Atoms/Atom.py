# -------------------------------------------------------------------------------------------------
# --------------------------------- Ontology :: Atoms :: Atom ABC ---------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ------------------------------------------ ABC :: Atom ------------------------------------------
# -------------------------------------------------------------------------------------------------
class Atom(Node):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Node':

        if visit := getattr(visitor, 'visit_atom', None):
            return visit(self, context)

        return super().visit(visitor, context)
