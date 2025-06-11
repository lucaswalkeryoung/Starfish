# -------------------------------------------------------------------------------------------------
# --------------------------------- Ontology :: Zones :: Outside ----------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node import Node
from Ontology.Objects.Zone  import Zone

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ---------------------------------------- Zone :: Outside ----------------------------------------
# -------------------------------------------------------------------------------------------------
class Outside(Zone):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Outside':

        try:
            return visitor.visit_outside(self, context)

        except AttributeError:
            return super().visit(visitor, context)