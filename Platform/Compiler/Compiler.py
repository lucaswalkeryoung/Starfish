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

if TYPE_CHECKING:
    from Ontology.Zones.Library  import Library
    from Ontology.Objects.Player import Player

from pathlib import Path

import random


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

        return type(node)(*components, **node.attributes)


    # -----------------------------------------------------------------------------------------
    # ---------------------------- COMPILER :: Compile an Identity ----------------------------
    # -----------------------------------------------------------------------------------------
    def visit_identity(self, node: Identity, context: Context) -> Identity:

        attributes = partition(node.attributes)
        components = []

        for type, attributes in attributes.items():
            for attribute, value in attributes.items():
                components.append(type(**{attribute: value}))

        return Identity(*components)


    # -----------------------------------------------------------------------------------------
    # ------------------------------ COMPILER :: Compile a Card -------------------------------
    # -----------------------------------------------------------------------------------------
    def visit_card(self, node: Card, context: Context) -> Card:

        components = [c.visit(self, context.descend()) for c in node.components]

        singulars = sort_singular(components)
        multiples = sort_multiple(components)

        identity = singulars.get(Identity)
        play = multiples.get(Play)
        cast = multiples.get(Cast)

        if not play and not cast:

            if identity.isinstance(land=True):
                multiples[Play].append(Play())

            else:
                multiples[Cast].append(Cast(Cost()))

        return node


    # -----------------------------------------------------------------------------------------
    # ----------------------------- COMPILER :: Compile a Player ------------------------------
    # -----------------------------------------------------------------------------------------
    def visit_player(self, node: 'Player', context: Context) -> 'Player':

        return type(node)(
            node.library,
            Hand(),
            Graveyard(),
            Pool(Role(mana=True)),
            Pool(Role(life=True)),
            Pool(Role(damage=True)),
        )


    # -----------------------------------------------------------------------------------------
    # ------------------------ COMPILER :: Bypass Library Compilation -------------------------
    # -----------------------------------------------------------------------------------------
    def visit_clock(self, node: 'Library', context: Context) -> 'Library':

        return Clock(
            Turn(
                Phase(
                    Step(untap_step=True),
                    Step(upkeep=True),
                    Step(draw_step=True),
                ),
                Phase(
                    Step(main=True, precombat=True),
                ),
                Phase(
                    Step(begin_combat=True),
                    Step(declare_attackers=True),
                    Step(declare_blockers=True),
                    Step(first_strike_damage=True),
                    Step(strike_damage=True),
                    Step(last_strike_damage=True),
                    Step(end_combat=True),
                ),
                Phase(
                    Step(main=True, postcombat=True),
                ),
                Phase(
                    Step(end_step=True),
                    Step(cleanup_step=True),
                ),
            ),
        )


    # -----------------------------------------------------------------------------------------
    # ------------------------ COMPILER :: Bypass Library Compilation -------------------------
    # -----------------------------------------------------------------------------------------
    def visit_library(self, node: 'Library', context: Context) -> 'Library':
        return node


    # -----------------------------------------------------------------------------------------
    # ------------------------------ COMPILER :: Compile a Card -------------------------------
    # -----------------------------------------------------------------------------------------
    def visit_world(self, node: World, context: Context) -> World:

        random.shuffle(node.components)

        context['players'] = node.components
        context['world']   = node

        components = [component.visit(self, context.descend()) for component in [
            Battlefield(),
            Exile(),
            Outside(),
            Clock(),
            Stack(),
            Heap(),
           *node.components,
        ]]

        return World(*components)


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
    def compile(root: World | Path) -> Card | World:

        if isinstance(root, Path):
            return eval(root.read_text()).visit(Compiler(), Context())

        return root.visit(Compiler(), Context())