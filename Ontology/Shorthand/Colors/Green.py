
# -------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Shorthand :: Colors :: Green ----------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Shorthand.Abstract.Shorthand import Shorthand
from Ontology.Shorthand.Abstract.Criterand import Criterand
from Ontology.Abstract.Node import Node

from Ontology.Atoms.Color import Color

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Visitor import Visitor
    from Visitors.Context import Context

from Taxonomy import Taxonomy


# -------------------------------------------------------------------------------------------------
# -------------------------------------- Shorthand :: Green ---------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='green', plural='green', atom=Color)
class Green(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Green':

        if visit := getattr(visitor, 'visit_green', None):
            return visit(self, context)

        return super().visit(visitor, context)

