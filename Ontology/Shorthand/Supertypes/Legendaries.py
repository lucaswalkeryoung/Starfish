
# -------------------------------------------------------------------------------------------------
# ---------------------- Ontology :: Shorthand :: Supertypes :: Legendaries -----------------------
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
# ----------------------------------- Shorthand :: Legendaries ------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='legendary', plural='legendaries', atom=Supertype)
class Legendaries(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Legendaries':

        if visit := getattr(visitor, 'visit_legendaries', None):
            return visit(self, context)

        return super().visit(visitor, context)

