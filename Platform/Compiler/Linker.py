# -------------------------------------------------------------------------------------------------
# -------------------------------- Platform :: Compiler :: Linker ---------------------------------
# -------------------------------------------------------------------------------------------------
from Visitors.Context  import Context
from Visitors.Visitor  import Visitor
from Taxonomy.Taxonomy import *


# -------------------------------------------------------------------------------------------------
# --------------------------------------- Visitor :: Linker ---------------------------------------
# -------------------------------------------------------------------------------------------------
class Assembler(Visitor):

    # -----------------------------------------------------------------------------------------
    # --------------------------- COMPILER :: Default Linker Method ---------------------------
    # -----------------------------------------------------------------------------------------
    def visit_node(self, node: Node, context: Context) -> Node:

        for component in node.components:
            component.visit(self, context.descend())


    # -----------------------------------------------------------------------------------------
    # ------------------------------ ENTRY :: Linker Entry Point ------------------------------
    # -----------------------------------------------------------------------------------------
    @staticmethod
    def link(node: World) -> World:
        return node.visit(Linker(), Context())