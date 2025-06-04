# -------------------------------------------------------------------------------------------------
# -------------------------------- Ontology :: Objects :: Zone ABC --------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Objects.Object import Object
from Ontology.Abstract.Node  import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ------------------------------------------ ABC :: Zone ------------------------------------------
# -------------------------------------------------------------------------------------------------
class Zone(Object):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Zone':

        if visit := getattr(visitor, 'visit_zone', None):
            return visit(self, context)

        return super().visit(visitor, context)
