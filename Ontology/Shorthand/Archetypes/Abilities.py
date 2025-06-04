
# -------------------------------------------------------------------------------------------------
# ----------------------- Ontology :: Shorthand :: Archetypes :: Abilities ------------------------
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
# ------------------------------------ Shorthand :: Abilities -------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='ability', plural='abilities', atom=Archetype)
class Abilities(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Abilities':

        if visit := getattr(visitor, 'visit_abilities', None):
            return visit(self, context)

        return super().visit(visitor, context)

