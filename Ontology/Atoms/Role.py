# -------------------------------------------------------------------------------------------------
# ----------------------------------- Ontology :: Atoms :: Role -----------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node import Node
from Ontology.Atoms.Atom    import Atom

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ----------------------------------------- Atom :: Role ------------------------------------------
# -------------------------------------------------------------------------------------------------
class Role(Atom):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Role':

        try:
            return visitor.visit_role(self, context)

        except AttributeError:
            return super().visit(visitor, context)