
# -------------------------------------------------------------------------------------------------
# ------------------------ Ontology :: Shorthand :: Types :: Conspiracies -------------------------
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
# ----------------------------------- Shorthand :: Conspiracies -----------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='conspiracy', plural='conspiracies', atom=Type)
class Conspiracies(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Conspiracies':

        if visit := getattr(visitor, 'visit_conspiracies', None):
            return visit(self, context)

        return super().visit(visitor, context)

