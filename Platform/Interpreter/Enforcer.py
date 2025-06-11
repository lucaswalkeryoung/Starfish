# -------------------------------------------------------------------------------------------------
# -------------------------- Platform :: Interpreter :: The Interpreter ---------------------------
# -------------------------------------------------------------------------------------------------
from Platform.Compiler.Recompiler import Recompiler
from Platform.Compiler.Compiler import Compiler
from Platform.Compiler.Linker import Linker

from Visitors.Context import Context
from Visitors.Visitor import Visitor

from Taxonomy.Taxonomy import *


# -------------------------------------------------------------------------------------------------
# ----------------------------- Visitor :: State-Based Rules Enforcer -----------------------------
# -------------------------------------------------------------------------------------------------
class Enforcer(Visitor):

    def visit_node(self, node: Node, context: Context) -> None:
        ...

    @staticmethod
    def enforce(world: World) -> None:
        ...
