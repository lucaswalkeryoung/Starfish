# -------------------------------------------------------------------------------------------------
# ----------------------------- Ontology :: Components :: Eligibility -----------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Components.Component import Component
from Ontology.Abstract.Node import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ----------------------------------- Component :: Eligibility ------------------------------------
# -------------------------------------------------------------------------------------------------
class Eligibility(Component):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Eligibility':

        try:
            return visitor.visit_eligibility(self, context)

        except AttributeError:
            return super().visit(visitor, context)