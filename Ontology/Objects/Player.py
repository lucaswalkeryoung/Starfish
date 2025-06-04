# -------------------------------------------------------------------------------------------------
# --------------------------------- Ontology :: Objects :: Player ---------------------------------
# -------------------------------------------------------------------------------------------------
from Platform.Exceptions.EmptyLibrary import EmptyLibraryException

from Ontology.Zones.CommandZone import CommandZone
from Ontology.Zones.Graveyard   import Graveyard
from Ontology.Zones.Library     import Library
from Ontology.Zones.Hand        import Hand
from Ontology.Zones.Pool        import Pool

from Ontology.Objects.Object import Object
from Ontology.Objects.Card   import Card

from Ontology.Abstract.Node  import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor

from Taxonomy import Taxonomy


# -------------------------------------------------------------------------------------------------
# --------------------------------------- Object :: Player ----------------------------------------
# -------------------------------------------------------------------------------------------------
class Player(Object):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

        listed = Taxonomy.sort_plural(components)
        popped = Taxonomy.sort_single(components)

        pools = {pool.name: pool for pool in listed.get(Pool, [])}

        self.command_zone = popped.get(CommandZone)
        self.library = popped.get(Library)
        self.hand = popped.get(Hand)
        self.graveyard = popped.get(Graveyard)

        self.mana_pool = pools.get('mana')
        self.damage_pool = pools.get('damage')
        self.life_pool = pools.get('life')


    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Player':

        if visit := getattr(visitor, 'visit_player', None):
            return visit(self, context)

        return super().visit(visitor, context)

    def shuffle(self) -> Library:
        return self.library.shuffle()

    def draw(self) -> Card:

        try:

            card = self.library.components.pop()
            self.hand.components.append(card)

            return card

        except IndexError:
            raise EmptyLibraryException()
