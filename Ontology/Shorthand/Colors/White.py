
# -------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Shorthand :: Colors :: White ----------------------------
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
# -------------------------------------- Shorthand :: White ---------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='white', plural='white', atom=Color)
class White(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'White':

        try:
            return visitor.visit_white(self, context)

        except AttributeError:
            return super().visit(visitor, context)
