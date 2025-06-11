
# -------------------------------------------------------------------------------------------------
# ------------------------ Ontology :: Shorthand :: Types :: Planeswalkers ------------------------
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
# ---------------------------------- Shorthand :: Planeswalkers -----------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='planeswalker', plural='planeswalkers', atom=Type)
class Planeswalkers(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Planeswalkers':

        try:
            return visitor.visit_planeswalkers(self, context)

        except AttributeError:
            return super().visit(visitor, context)
