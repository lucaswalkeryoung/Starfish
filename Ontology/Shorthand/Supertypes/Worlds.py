
# -------------------------------------------------------------------------------------------------
# ------------------------- Ontology :: Shorthand :: Supertypes :: Worlds -------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Shorthand.Abstract.Shorthand import Shorthand
from Ontology.Shorthand.Abstract.Criterand import Criterand
from Ontology.Abstract.Node import Node

from Ontology.Atoms.Supertype import Supertype

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Visitor import Visitor
    from Visitors.Context import Context

from Taxonomy import Taxonomy


# -------------------------------------------------------------------------------------------------
# -------------------------------------- Shorthand :: Worlds --------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='world', plural='worlds', atom=Supertype)
class Worlds(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Worlds':

        if visit := getattr(visitor, 'visit_worlds', None):
            return visit(self, context)

        return super().visit(visitor, context)

