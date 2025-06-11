# -------------------------------------------------------------------------------------------------
# ---------------------------- Ontology :: Objects :: Zone Object ABC -----------------------------
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

        try:
            return visitor.visit_zone(self, context)

        except AttributeError:
            return super().visit(visitor, context)