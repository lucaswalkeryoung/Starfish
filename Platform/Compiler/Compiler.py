# -------------------------------------------------------------------------------------------------
# ------------------------------- Platform :: Compiler :: Compiler --------------------------------
# -------------------------------------------------------------------------------------------------
from Taxonomy.Taxonomy import sort_multiple
from Taxonomy.Taxonomy import sort_singular
from Taxonomy.Taxonomy import partition

from Taxonomy.Taxonomy import *

from Visitors.Context  import Context
from Visitors.Visitor  import Visitor

from typing import TYPE_CHECKING
from typing import Optional
from typing import overload

from pathlib import Path


# -------------------------------------------------------------------------------------------------
# -------------------------------------- Visitor :: Compiler --------------------------------------
# -------------------------------------------------------------------------------------------------
class Compiler(Visitor):

    # -----------------------------------------------------------------------------------------
    # ------------------------ COMPILER :: Default Compilation Method -------------------------
    # -----------------------------------------------------------------------------------------
    def visit_node(self, node: Node, context: Context) -> Node:

        components = []

        for component in node.components:
            components.append(component.visit(self, context.descend()))

        return type(node)(*component, **node.attributes)


    # -----------------------------------------------------------------------------------------
    # ---------------------- ENTRY :: Dual Entry-Points to the Compiler -----------------------
    # -----------------------------------------------------------------------------------------
    @staticmethod
    @overload
    def compile(world: World) -> World:
        ...

    @staticmethod
    @overload
    def compile(card: Path) -> Card:
        ...

    @staticmethod
    def compile(node: World | Path) -> Card | World:
        return node.visit(Compiler(), Context())