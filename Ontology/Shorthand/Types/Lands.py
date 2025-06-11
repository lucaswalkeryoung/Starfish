
# -------------------------------------------------------------------------------------------------
# ---------------------------- Ontology :: Shorthand :: Types :: Lands ----------------------------
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
@Taxonomy.register(singular='land', plural='lands', atom=Type)
class Lands(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Lands':

        try:
            return visitor.visit_lands(self, context)

        except AttributeError:
            return super().visit(visitor, context)
