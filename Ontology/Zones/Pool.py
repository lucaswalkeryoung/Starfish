# -------------------------------------------------------------------------------------------------
# ----------------------------------- Ontology :: Zones :: Pool -----------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node import Node
from Ontology.Objects.Zone  import Zone

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ----------------------------------------- Zone :: Pool ------------------------------------------
# -------------------------------------------------------------------------------------------------
class Pool(Zone):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

        if components:
            self.role, *X = components

        else:
            self.role, *X = None,

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Pool':

        if visit := getattr(visitor, 'visit_pool', None):
            return visit(self, context)

        return super().visit(visitor, context)

    @property
    def name(self) -> str:
        return list(self.role.attributes.keys()).pop()
