
# -------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Shorthand :: Types :: Kindred ---------------------------
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
# -------------------------------------- Shorthand :: Lands ---------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='kindred', plural='kindred', atom=Type)
class Kindred(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Kindred':

        if visit := getattr(visitor, 'visit_kindred', None):
            return visit(self, context)

        return super().visit(visitor, context)

