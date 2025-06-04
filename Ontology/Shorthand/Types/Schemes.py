
# -------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Shorthand :: Types :: Schemes ---------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Shorthand.Abstract.Shorthand import Shorthand
from Ontology.Shorthand.Abstract.Criterand import Criterand
from Ontology.Abstract.Node import Node

from Ontology.Atoms.Type import Type

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Visitor import Visitor
    from Visitors.Context import Context

from Taxonomy import Taxonomy


# -------------------------------------------------------------------------------------------------
# ------------------------------------- Shorthand :: Schemes --------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='scheme', plural='schemes', atom=Type)
class Schemes(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Schemes':

        if visit := getattr(visitor, 'visit_schemes', None):
            return visit(self, context)

        return super().visit(visitor, context)

