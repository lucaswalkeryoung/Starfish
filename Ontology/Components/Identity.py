# -------------------------------------------------------------------------------------------------
# ------------------------------ Ontology :: Components :: Identity -------------------------------
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
# ------------------------------------- Component :: Identity -------------------------------------
# -------------------------------------------------------------------------------------------------
class Identity(Component):

    def __init__(self, *components: 'Node', **attributes: int) -> None:
        super().__init__(*components, **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Identity':

        if visit := getattr(visitor, 'visit_identity', None):
            return visit(self, context)

        return super().visit(visitor, context)

    @property
    def archetypes(self) -> bool:

        groups = {k: list(g) for k, g in itertools.groupby(self.components, type)}
        output = []

        for component in groups.get(Archetype):
            output.extend(component.attributes.keys())

        return output

    @property
    def supertypes(self) -> bool:

        groups = {k: list(g) for k, g in itertools.groupby(self.components, type)}
        output = []

        for component in groups.get(Supertype):
            output.extend(component.attributes.keys())

        return output

    @property
    def types(self) -> bool:

        groups = {k: list(g) for k, g in itertools.groupby(self.components, type)}
        output = []

        for component in groups.get(Type):
            output.extend(component.attributes.keys())

        return output

    @property
    def subtypes(self) -> bool:

        groups = {k: list(g) for k, g in itertools.groupby(self.components, type)}
        output = []

        for component in groups.get(Type):
            output.extend(component.attributes.keys())

        return output

    @property
    def colors(self) -> bool:

        groups = {k: list(g) for k, g in itertools.groupby(self.components, type)}
        output = []

        for component in groups.get(Color):
            output.extend(component.attributes.keys())

        return output