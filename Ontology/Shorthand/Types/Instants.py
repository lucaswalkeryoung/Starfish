
# -------------------------------------------------------------------------------------------------
# -------------------------- Ontology :: Shorthand :: Types :: Instants ---------------------------
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
# ------------------------------------- Shorthand :: Instants -------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='instant', plural='instants', atom=Type)
class Instants(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Instants':

        try:
            return visitor.visit_instants(self, context)

        except AttributeError:
            return super().visit(visitor, context)
