# -------------------------------------------------------------------------------------------------
# --------------------------------- Ontology :: Objects :: Player ---------------------------------
# -------------------------------------------------------------------------------------------------
from Taxonomy.Taxonomy import sort_multiple
from Taxonomy.Taxonomy import sort_singular

from Ontology.Zones.Library import Library
from Ontology.Zones.Hand import Hand
from Ontology.Zones.Graveyard import Graveyard
from Ontology.Zones.Pool import Pool

from Ontology.Objects.Object import Object
from Ontology.Objects.Card   import Card

from Ontology.Abstract.Node  import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# --------------------------------------- Object :: Player ----------------------------------------
# -------------------------------------------------------------------------------------------------
class Player(Object):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

        singular = sort_singular(components)
        multiple = sort_multiple(components)

        self.library = singular.get(Library)
        self.hand = singular.get(Hand)
        self.graveyard = singular.get(Graveyard)

        if pools := multiple.get(Pool):
            self.mana_pool, self.life_pool, self.damage_pool = pools

        else:
            self.mana_pool, self.life_pool, self.damage_pool = None, None, None

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Player':

        try:
            return visitor.visit_player(self, context)

        except AttributeError:
            return super().visit(visitor, context)

    def shuffle(self) -> None:
        self.library.shuffle()

    def draw(self) -> Card:

        card = self.library.components.pop()
        self.hand.components.append(card)

        return card