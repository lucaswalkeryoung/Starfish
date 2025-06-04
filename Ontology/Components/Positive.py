# -------------------------------------------------------------------------------------------------
# ------------------------------ Ontology :: Components :: Positive -------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Components.Component import Component
from Ontology.Abstract.Node import Node

from Ontology.Atoms.Archetype import Archetype
from Ontology.Atoms.Supertype import Supertype
from Ontology.Atoms.Type      import Type
from Ontology.Atoms.Subtype   import Subtype
from Ontology.Atoms.Color     import Color

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor

import itertools


# -------------------------------------------------------------------------------------------------
# ------------------------------------- Component :: Positive -------------------------------------
# -------------------------------------------------------------------------------------------------
class Positive(Component):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Positive':

        if visit := getattr(visitor, 'visit_positive', None):
            return visit(self, context)

        return super().visit(visitor, context)