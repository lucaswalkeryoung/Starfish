
# -------------------------------------------------------------------------------------------------
# ----------------- Ontology :: Shorthand :: Subtypes :: Tribes :: Triskelavites ------------------
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
# ---------------------------------- Shorthand :: Triskelavites -----------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='triskelavite', plural='triskelavites', atom=Subtype)
class Triskelavites(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Triskelavites':

        try:
            return visitor.visit_triskelavites(self, context)

        except AttributeError:
            return super().visit(visitor, context)
