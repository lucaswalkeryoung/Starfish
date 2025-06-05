# -------------------------------------------------------------------------------------------------
# --------------------------------- Ontology :: Objects :: Player ---------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Objects.Object import Object
from Ontology.Abstract.Node  import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# --------------------------------------- Object :: Player ----------------------------------------
# -------------------------------------------------------------------------------------------------
class Player(Object):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Player':

        try:
            return visitor.visit_player(self, context)

        except AttributeError:
            return super().visit(self, context)