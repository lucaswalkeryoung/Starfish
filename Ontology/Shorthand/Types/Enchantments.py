
# -------------------------------------------------------------------------------------------------
# ------------------------ Ontology :: Shorthand :: Types :: Enchantments -------------------------
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
# ----------------------------------- Shorthand :: Enchantments -----------------------------------
# -------------------------------------------------------------------------------------------------
@Taxonomy.register(singular='enchantment', plural='enchantments', atom=Type)
class Enchantments(Criterand, Shorthand):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Enchantments':

        try:
            return visitor.visit_enchantments(self, context)

        except AttributeError:
            return super().visit(visitor, context)
