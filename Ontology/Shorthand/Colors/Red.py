
# -------------------------------------------------------------------------------------------------
# ---------------------------- Ontology :: Shorthand :: Colors :: Red -----------------------------
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
# --------------------------------------- Shorthand :: Red ----------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='red', plural='red', atom=Color)
class Red(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Red':

        if visit := getattr(visitor, 'visit_red', None):
            return visit(self, context)

        return super().visit(visitor, context)

