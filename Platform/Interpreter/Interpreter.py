# -------------------------------------------------------------------------------------------------
# ---------------------------- Platform :: Interpreter :: Interpreter -----------------------------
# -------------------------------------------------------------------------------------------------
from Platform.Interpreter.Compiler import Compiler
from Platform.Interpreter.Linker   import Linker

from Platform.Visitors.Auditor import Auditor
from Platform.Visitors.Printer import Printer

from Visitors.Context import Context
from Visitors.Visitor import Visitor

from Ontology.Zones.World import World

import random


# -------------------------------------------------------------------------------------------------
# ---------------------------------------- The Interpreter ----------------------------------------
# -------------------------------------------------------------------------------------------------
class Interpreter(object):

    @staticmethod
    def run(world: World) -> None:

        world = Compiler.compile(world)
        world = Linker.link(world)

        count = 0

        for player in world.players:

            player.shuffle()
            player.draw()

        players = world.players
        clock   = world.clock
        stack   = world.stack

        step    = clock.now
        phase   = step.parent
        turn    = step.parent.parent
        player  = step.player

        while True:

            if step.name == 'untap':
                count += 1

            if step.name == 'upkeep':
                ...

            if step.name == 'draw_step':
                ...

            if step.name == 'main':

                if step.attributes.get('precombat'):
                    ...

                else:
                    ...

            if step.name == 'begin_combat':
                ...

            if step.name == 'declare_attackers':
                ...

            if step.name == 'declare_blockers':
                ...

            if step.name == 'first_strike_damage':
                ...

            if step.name == 'strike_damage':
                ...

            if step.name == 'last_strike_damage':
                ...

            if step.name == 'end_combat':
                ...

            if step.name == 'end_step':
                ...

            if step.name == 'cleanup_step':
                ...

            step  = clock.tick()
            phase = step.parent
            turn  = step.parent.parent

            player = step.player

            Auditor.audit(world, player)