
# -------------------------------------------------------------------------------------------------
# ----------------------- Ontology :: Shorthand :: Archetypes :: Permanents -----------------------
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
# ------------------------------------ Shorthand :: Permanents ------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='permanent', plural='permanents', atom=Archetype)
class Permanents(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Permanents':

        if visit := getattr(visitor, 'visit_permanents', None):
            return visit(self, context)

        return super().visit(visitor, context)

