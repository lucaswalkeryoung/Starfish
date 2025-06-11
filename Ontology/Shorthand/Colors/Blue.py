
# -------------------------------------------------------------------------------------------------
# ---------------------------- Ontology :: Shorthand :: Colors :: Blue ----------------------------
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
# --------------------------------------- Shorthand :: Blue ---------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='blue', plural='blue', atom=Color)
class Blue(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Blue':

        try:
            return visitor.visit_blue(self, context)

        except AttributeError:
            return super().visit(visitor, context)
