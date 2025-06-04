# -------------------------------------------------------------------------------------------------
# ---------------------------------- Ontology :: Objects :: Card ----------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Components.Identity import Identity
from Ontology.Objects.Object import Object
from Ontology.Abstract.Node  import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor

import itertools


# -------------------------------------------------------------------------------------------------
# ---------------------------------------- Object :: Card -----------------------------------------
# -------------------------------------------------------------------------------------------------
class Card(Object):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

        groups = {k: list(g) for k, g in itertools.groupby(self.components, type)}
        popped = {k: l.pop() for k, l in groups.items() if len(l) == 1}

        self.identity = popped.get(Identity)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Card':

        if visit := getattr(visitor, 'visit_card', None):
            return visit(self, context)

        return super().visit(visitor, context)