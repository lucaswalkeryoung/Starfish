
# -------------------------------------------------------------------------------------------------
# ----------------- Ontology :: Shorthand :: Subtypes :: Tribes :: Nightstalkers ------------------
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
# ---------------------------------- Shorthand :: Nightstalkers -----------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='nightstalker', plural='nightstalkers', atom=Subtype)
class Nightstalkers(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Nightstalkers':

        try:
            return visitor.visit_nightstalkers(self, context)

        except AttributeError:
            return super().visit(visitor, context)
