# -------------------------------------------------------------------------------------------------
# ------------------------------ Ontology :: Components :: Identity -------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Components.Component import Component
from Ontology.Abstract.Node import Node

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor


# -------------------------------------------------------------------------------------------------
# ------------------------------------- Component :: Identity -------------------------------------
# -------------------------------------------------------------------------------------------------
class Identity(Component):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Identity':

        try:
            return visitor.visit_identity(self, context)

        except AttributeError:
            return super().visit(visitor, context)

    def isinstance(self, **query: bool) -> bool:

        result = {key: False for key in query}

        for component in self.components:

            for key in query:

                if key in component.attributes:
                    result[key] = component.attributes[key]

        return all(result.values())