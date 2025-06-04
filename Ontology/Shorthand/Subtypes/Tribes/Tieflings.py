
# -------------------------------------------------------------------------------------------------
# ------------------- Ontology :: Shorthand :: Subtypes :: Tribes :: Tieflings --------------------
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
# ------------------------------------ Shorthand :: Tieflings -------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='tiefling', plural='tieflings', atom=Subtype)
class Tieflings(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Tieflings':

        if visit := getattr(visitor, 'visit_tieflings', None):
            return visit(self, context)

        return super().visit(visitor, context)

