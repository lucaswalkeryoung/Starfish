
# -------------------------------------------------------------------------------------------------
# ---------------------- Ontology :: Shorthand :: Subtypes :: Tribes :: Cats ----------------------
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
# --------------------------------------- Shorthand :: Cats ---------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='cat', plural='cats', atom=Subtype)
class Cats(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Cats':

        if visit := getattr(visitor, 'visit_cats', None):
            return visit(self, context)

        return super().visit(visitor, context)

