# -------------------------------------------------------------------------------------------------
# ------------------------------- Ontology :: Abstract :: Node ABC --------------------------------
# -------------------------------------------------------------------------------------------------
from Platform.Visitors.Printer import Printer

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor

from collections import defaultdict

# -------------------------------------------------------------------------------------------------
# ------------------------------------------ ABC :: Node ------------------------------------------
# -------------------------------------------------------------------------------------------------
class Node(object):

    def __init__(self, *components: 'Node', **attributes: int) -> None:

        self.components = list(components)
        self.attributes = dict(attributes)

        self.edges = defaultdict(list)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Node':
        return visitor.visit_node(self, context)

    def __str__(self) -> str:
        return Printer.print(self)

    @property
    def children(self) -> list['Node']:
        return self.edges['child']

    @property
    def parent(self) -> 'Node':
        return self.edges['parent'][0]