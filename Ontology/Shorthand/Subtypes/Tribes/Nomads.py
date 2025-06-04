
# -------------------------------------------------------------------------------------------------
# --------------------- Ontology :: Shorthand :: Subtypes :: Tribes :: Nomads ---------------------
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
# -------------------------------------- Shorthand :: Nomads --------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='nomad', plural='nomads', atom=Subtype)
class Nomads(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Nomads':

        if visit := getattr(visitor, 'visit_nomads', None):
            return visit(self, context)

        return super().visit(visitor, context)

