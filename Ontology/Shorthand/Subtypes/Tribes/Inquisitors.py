
# -------------------------------------------------------------------------------------------------
# ------------------ Ontology :: Shorthand :: Subtypes :: Tribes :: Inquisitors -------------------
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
# ----------------------------------- Shorthand :: Inquisitors ------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='inquisitor', plural='inquisitors', atom=Subtype)
class Inquisitors(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Inquisitors':

        try:
            return visitor.visit_inquisitors(self, context)

        except AttributeError:
            return super().visit(visitor, context)
