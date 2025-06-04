
# -------------------------------------------------------------------------------------------------
# ------------------ Ontology :: Shorthand :: Subtypes :: Tribes :: Salamanders -------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Shorthand.Abstract.Shorthand import Shorthand
from Ontology.Shorthand.Abstract.Criterand import Criterand
from Ontology.Abstract.Node import Node

from Ontology.Atoms.Subtype import Subtype

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Visitor import Visitor
    from Visitors.Context import Context

from Taxonomy import Taxonomy


# -------------------------------------------------------------------------------------------------
# ----------------------------------- Shorthand :: Salamanders ------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='salamander', plural='salamanders', atom=Subtype)
class Salamanders(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Salamanders':

        if visit := getattr(visitor, 'visit_salamanders', None):
            return visit(self, context)

        return super().visit(visitor, context)

