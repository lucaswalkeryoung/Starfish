# -------------------------------------------------------------------------------------------------
# -------------------------------- Ontology :: Atoms :: Supertype ---------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node import Node
from Ontology.Atoms.Atom    import Atom

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# --------------------------------------- Atom :: Supertype ---------------------------------------
# -------------------------------------------------------------------------------------------------
class Supertype(Atom):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Supertype':

        try:
            return visitor.visit_supertype(self, context)

        except AttributeError:
            return super().visit(visitor, context)