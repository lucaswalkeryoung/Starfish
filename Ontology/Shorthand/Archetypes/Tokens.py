
# -------------------------------------------------------------------------------------------------
# ------------------------- Ontology :: Shorthand :: Archetypes :: Tokens -------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Shorthand.Abstract.Shorthand import Shorthand
from Ontology.Shorthand.Abstract.Criterand import Criterand
from Ontology.Abstract.Node import Node

from Ontology.Atoms.Archetype import Archetype

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Visitor import Visitor
    from Visitors.Context import Context

from Taxonomy import Taxonomy


# -------------------------------------------------------------------------------------------------
# -------------------------------------- Shorthand :: Tokens --------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='token', plural='tokens', atom=Archetype)
class Tokens(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Tokens':

        if visit := getattr(visitor, 'visit_tokens', None):
            return visit(self, context)

        return super().visit(visitor, context)

