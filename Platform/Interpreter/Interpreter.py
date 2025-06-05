# -------------------------------------------------------------------------------------------------
# -------------------------- Platform :: Interpreter :: The Interpreter ---------------------------
# -------------------------------------------------------------------------------------------------
from Visitors.Context import Context
from Visitors.Visitor import Visitor

from Taxonomy.Taxonomy import *


# -------------------------------------------------------------------------------------------------
# ---------------------------------- Visitor :: The Interpreter -----------------------------------
# -------------------------------------------------------------------------------------------------
class Interpreter(Visitor):

    def visit_node(self, node: Node, context: Context) -> None:
        ...

    @staticmethod
    def interpret(world: World) -> None:
        ...