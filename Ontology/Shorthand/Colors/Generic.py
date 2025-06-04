
# -------------------------------------------------------------------------------------------------
# -------------------------- Ontology :: Shorthand :: Colors :: Generic ---------------------------
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
# ------------------------------------- Shorthand :: Generic --------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='generic', plural='generic', atom=Color)
class Generic(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Generic':

        if visit := getattr(visitor, 'visit_generic', None):
            return visit(self, context)

        return super().visit(visitor, context)

