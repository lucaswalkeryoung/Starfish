
# -------------------------------------------------------------------------------------------------
# ------------------------- Ontology :: Shorthand :: Supertypes :: Snows --------------------------
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
# -------------------------------------- Shorthand :: Snows ---------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='snow', plural='snows', atom=Supertype)
class Snows(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Snows':

        try:
            return visitor.visit_snows(self, context)

        except AttributeError:
            return super().visit(visitor, context)
