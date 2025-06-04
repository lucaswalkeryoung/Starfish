
# -------------------------------------------------------------------------------------------------
# -------------------------- Ontology :: Shorthand :: Types :: Creatures --------------------------
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
# ------------------------------------ Shorthand :: Creatures -------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='creature', plural='creatures', atom=Type)
class Creatures(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Creatures':

        if visit := getattr(visitor, 'visit_creatures', None):
            return visit(self, context)

        return super().visit(visitor, context)

