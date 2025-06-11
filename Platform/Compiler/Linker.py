# -------------------------------------------------------------------------------------------------
# -------------------------------- Platform :: Compiler :: Linker ---------------------------------
# -------------------------------------------------------------------------------------------------
from Visitors.Context  import Context
from Visitors.Visitor  import Visitor
from Taxonomy.Taxonomy import *


# -------------------------------------------------------------------------------------------------
# --------------------------------------- Visitor :: Linker ---------------------------------------
# -------------------------------------------------------------------------------------------------
class Linker(Visitor):

    # -----------------------------------------------------------------------------------------
    # ---------------------------- LINKER :: Default Linker Method ----------------------------
    # -----------------------------------------------------------------------------------------
    def visit_node(self, node: Node, context: Context) -> Node:

        for component in node.components:

            component.visit(self, context.descend())

            component.edges['parent'].append(node)
            node.edges['children'].append(component)

        return node


    # -----------------------------------------------------------------------------------------
    # ---------------------------- LINKER :: Default Linker Method ----------------------------
    # -----------------------------------------------------------------------------------------
    def visit_zone(self, node: Zone, context: Context) -> Zone:

        for component in node.components:

            component.edges['within'].append(node)
            node.edges['contains'].append(component)

        return self.visit_node(node, context)


    # -----------------------------------------------------------------------------------------
    # -------------------------- LINKER :: Link the Clock to Players --------------------------
    # -----------------------------------------------------------------------------------------
    def visit_world(self, node: World, context: Context) -> Zone:

        players = node.players
        turns   = node.clock.components

        for player, turn in zip(players, turns):

            for phase in turn.components:

                for step in phase.components:

                    step.edges['possessor'].append(player)
                    player.edges['possessed'].append(step)

                    if not node.clock.edges['now']:
                        node.clock.edges['now'].append(step)

                phase.edges['possessor'].append(player)
                player.edges['possessed'].append(phase)

            turn.edges['possessor'].append(player)
            player.edges['possessed'].append(turn)

        return self.visit_zone(node, context)

    # -----------------------------------------------------------------------------------------
    # ------------------------------ ENTRY :: Linker Entry Point ------------------------------
    # -----------------------------------------------------------------------------------------
    @staticmethod
    def link(node: World) -> World:
        return node.visit(Linker(), Context())