
# -------------------------------------------------------------------------------------------------
# ---------------------- Ontology :: Shorthand :: Subtypes :: Titles :: Will ----------------------
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
# --------------------------------------- Shorthand :: Will ---------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='will', plural='will', atom=Subtype)
class Will(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Will':

        if visit := getattr(visitor, 'visit_will', None):
            return visit(self, context)

        return super().visit(visitor, context)

