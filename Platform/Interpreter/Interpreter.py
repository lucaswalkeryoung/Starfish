# -------------------------------------------------------------------------------------------------
# -------------------------- Platform :: Interpreter :: The Interpreter ---------------------------
# -------------------------------------------------------------------------------------------------
from Platform.Interface.Sockets.Server import Server
from Platform.Interface.Python.Auditor import Auditor

from Platform.Interpreter.Enforcer import Enforcer
from Platform.Compiler.Recompiler  import Recompiler
from Platform.Compiler.Compiler    import Compiler
from Platform.Compiler.Linker      import Linker

from Visitors.Context import Context
from Visitors.Visitor import Visitor

from Taxonomy.Taxonomy import *

from collections import deque

import webbrowser
import time


# -------------------------------------------------------------------------------------------------
# ---------------------------------- Visitor :: The Interpreter -----------------------------------
# -------------------------------------------------------------------------------------------------
class Interpreter(Visitor):

    def visit_node(self, node: Node, context: Context) -> None:
        ...

    @staticmethod
    def interpret(world: World) -> None:

        server = Server(host='127.0.0.1', port=5000, debug=True)
        server.start()

        webbrowser.open(f'http://{server.host}:{server.port}')

        while True:
            ...

        # world = Compiler.compile(world)
        # world = Linker.link(world)
        #
        # for player in world.players:
        #     player.shuffle()
        #     player.draw()
        #
        # clock  = world.clock
        # stack  = world.stack
        # heap   = world.heap
        #
        # step   = clock.now
        # phase  = step.parent
        # turn   = phase.parent
        #
        # player = step.player