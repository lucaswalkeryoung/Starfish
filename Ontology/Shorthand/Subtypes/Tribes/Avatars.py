
# -------------------------------------------------------------------------------------------------
# -------------------- Ontology :: Shorthand :: Subtypes :: Tribes :: Avatars ---------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Shorthand.Abstract.Shorthand import Shorthand
from Ontology.Shorthand.Abstract.Criterand import Criterand
from Ontology.Abstract.Node import Node

from Ontology.Atoms.Subtype import Subtype

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Visitor import Visitor
    from Visitors.Context import Context

from Taxonomy import Taxonomy


# -------------------------------------------------------------------------------------------------
# ------------------------------------- Shorthand :: Avatars --------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='avatar', plural='avatars', atom=Subtype)
class Avatars(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Avatars':

        try:
            return visitor.visit_avatars(self, context)

        except AttributeError:
            return super().visit(visitor, context)
