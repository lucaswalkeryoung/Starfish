
# -------------------------------------------------------------------------------------------------
# --------------------------- Ontology :: Shorthand :: Types :: Tribals ---------------------------
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
# ------------------------------------- Shorthand :: Tribals --------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='tribal', plural='tribals', atom=Type)
class Tribals(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Tribals':

        try:
            return visitor.visit_tribals(self, context)

        except AttributeError:
            return super().visit(visitor, context)
