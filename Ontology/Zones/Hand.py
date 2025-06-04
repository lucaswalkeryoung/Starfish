# -------------------------------------------------------------------------------------------------
# ----------------------------------- Ontology :: Zones :: Hand -----------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node import Node
from Ontology.Objects.Zone  import Zone

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ----------------------------------------- Zone :: Heap ------------------------------------------
# -------------------------------------------------------------------------------------------------
class Hand(Zone):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Hand':

        if visit := getattr(visitor, 'visit_hand', None):
            return visit(self, context)

        return super().visit(visitor, context)
