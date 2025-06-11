# -------------------------------------------------------------------------------------------------
# ---------------------------------- Ontology :: Zones :: Clock -----------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Components.Turn  import Turn
from Ontology.Components.Phase import Phase
from Ontology.Atoms.Step       import Step

from Ontology.Abstract.Node import Node
from Ontology.Objects.Zone  import Zone

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ----------------------------------------- Zone :: Clock -----------------------------------------
# -------------------------------------------------------------------------------------------------
class Clock(Zone):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Clock':

        try:
            return visitor.visit_clock(self, context)

        except AttributeError:
            return super().visit(visitor, context)

    @property
    def now(self) -> Step:
        return self.edges['now'][0]