
# -------------------------------------------------------------------------------------------------
# ------------------------- Ontology :: Shorthand :: Archetypes :: Damage -------------------------
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
# -------------------------------------- Shorthand :: Damage --------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='damage', plural='damage', atom=Archetype)
class Damage(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Damage':

        try:
            return visitor.visit_damage(self, context)

        except AttributeError:
            return super().visit(visitor, context)
