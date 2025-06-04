
# -------------------------------------------------------------------------------------------------
# -------------------------- Ontology :: Shorthand :: Types :: Artifacts --------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Shorthand.Abstract.Shorthand import Shorthand
from Ontology.Shorthand.Abstract.Criterand import Criterand
from Ontology.Abstract.Node import Node

from Ontology.Atoms.Type import Type

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Visitor import Visitor
    from Visitors.Context import Context

from Taxonomy import Taxonomy


# -------------------------------------------------------------------------------------------------
# ------------------------------------ Shorthand :: Artifacts -------------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='artifact', plural='artifacts', atom=Type)
class Artifacts(Criterand, Shorthand):

    def __init__(self, *components: Node, **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Artifacts':

        if visit := getattr(visitor, 'visit_artifacts', None):
            return visit(self, context)

        return super().visit(visitor, context)

