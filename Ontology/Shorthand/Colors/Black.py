
# -------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Shorthand :: Colors :: Black ----------------------------
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
# -------------------------------------- Shorthand :: Black ---------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='black', plural='black', atom=Color)
class Black(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Black':

        try:
            return visitor.visit_black(self, context)

        except AttributeError:
            return super().visit(visitor, context)
