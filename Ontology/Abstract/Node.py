# -------------------------------------------------------------------------------------------------
# ------------------------------- Ontology :: Abstract :: Node ABC --------------------------------
# -------------------------------------------------------------------------------------------------
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor

import collections


# -------------------------------------------------------------------------------------------------
# ------------------------------------------ ABC :: Node ------------------------------------------
# -------------------------------------------------------------------------------------------------
class Node(object):

    def __init__(self, *components: 'Node', **attributes: int) -> None:

        self.edges = collections.defaultdict(list)

        self.components = list(components)
        self.attributes = dict(attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Node':
        return visitor.visit_node(self, context)