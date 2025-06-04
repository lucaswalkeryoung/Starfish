# -------------------------------------------------------------------------------------------------
# ---------------------------- Ontology :: Mechanics :: Cast Mechanic -----------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Mechanics.Mechanic import Mechanic
from Ontology.Abstract.Node import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# --------------------------------------- Mechanic :: Cast ----------------------------------------
# -------------------------------------------------------------------------------------------------
class Cast(Mechanic):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Cast':

        if visit := getattr(visitor, 'visit_cast', None):
            return visit(self, context)

        return super().visit(visitor, context)
