# -------------------------------------------------------------------------------------------------
# ---------------------------------- Ontology :: Zones :: World -----------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Zones.Battlefield import Battlefield
from Ontology.Zones.Clock       import Clock
from Ontology.Zones.Exile       import Exile
from Ontology.Zones.Heap        import Heap
from Ontology.Zones.Outside     import Outside
from Ontology.Zones.Stack       import Stack

from Ontology.Abstract.Node import Node

from Ontology.Objects.Player import Player
from Ontology.Objects.Zone   import Zone

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor

import itertools


# -------------------------------------------------------------------------------------------------
# ----------------------------------------- Zone :: World -----------------------------------------
# -------------------------------------------------------------------------------------------------
class World(Zone):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

        components = {k: list(g) for k, g in itertools.groupby(components, type)}

        if len(components) > 1: # uncompiled Worlds contain only a single grouper, Player

            self.battlefield = components.get(Battlefield).pop()
            self.exile       = components.get(Exile).pop()
            self.outside     = components.get(Outside).pop()
            self.clock       = components.get(Clock).pop()
            self.stack       = components.get(Stack).pop()
            self.heap        = components.get(Heap).pop()
            self.players     = components.get(Player)

        else:

            self.battlefield = None
            self.exile       = None
            self.outside     = None
            self.clock       = None
            self.stack       = None
            self.heap        = None
            self.players     = None

            self.players = components.get(Player)


    def visit(self, visitor: 'Visitor', context: 'Context') -> 'World':

        if visit := getattr(visitor, 'visit_world', None):
            return visit(self, context)

        return super().visit(visitor, context)
