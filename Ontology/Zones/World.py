# -------------------------------------------------------------------------------------------------
# ---------------------------------- Ontology :: Zones :: World -----------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Zones.Battlefield import Battlefield
from Ontology.Zones.Exile import Exile
from Ontology.Zones.Outside import Outside
from Ontology.Zones.Clock import Clock
from Ontology.Zones.Stack import Stack
from Ontology.Zones.Heap import Heap

from Ontology.Objects.Zone import Zone

from Ontology.Abstract.Node import Node

from Taxonomy.Taxonomy import sort_multiple
from Taxonomy.Taxonomy import sort_singular

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ----------------------------------------- Zone :: World -----------------------------------------
# -------------------------------------------------------------------------------------------------
class World(Zone):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

        singular = sort_singular(components)
        multiple = sort_multiple(components)

        self.battlefield = singular.get(Battlefield)
        self.exile       = singular.get(Exile)
        self.outside     = singular.get(Outside)
        self.clock       = singular.get(Clock)
        self.stack       = singular.get(Stack)
        self.heap        = singular.get(Heap)

        self.players     = list(components[6:])


    def visit(self, visitor: 'Visitor', context: 'Context') -> 'World':

        try:
            return visitor.visit_world(self, context)

        except AttributeError:
            return super().visit(visitor, context)