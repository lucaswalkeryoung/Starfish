# -------------------------------------------------------------------------------------------------
# ----------------------------------- Ontology :: Atoms :: Type -----------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node import Node
from Ontology.Atoms.Atom    import Atom

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ----------------------------------------- Atom :: Type ------------------------------------------
# -------------------------------------------------------------------------------------------------
class Type(Atom):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

        self.artifact     = attributes.get('artifact')
        self.battle       = attributes.get('battle')
        self.conspiracy   = attributes.get('conspiracy')
        self.creature     = attributes.get('creature')
        self.dungeon      = attributes.get('dungeon')
        self.enchantment  = attributes.get('enchantment')
        self.instant      = attributes.get('instant')
        self.land         = attributes.get('land')
        self.phenomenon   = attributes.get('phenomenon')
        self.plane        = attributes.get('plane')
        self.planeswalker = attributes.get('planeswalker')
        self.scheme       = attributes.get('scheme')
        self.sorcery      = attributes.get('sorcery')
        self.tribal       = attributes.get('tribal')
        self.vanguard     = attributes.get('vanguard')


    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Type':

        if visit := getattr(visitor, 'visit_type', None):
            return visit(self, context)

        return super().visit(visitor, context)
