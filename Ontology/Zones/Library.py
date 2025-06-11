# -------------------------------------------------------------------------------------------------
# --------------------------------- Ontology :: Zones :: Library ----------------------------------
# -------------------------------------------------------------------------------------------------
from Platform.Compiler.Compiler import Compiler

from Ontology.Abstract.Node import Node
from Ontology.Objects.Zone  import Zone

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor

from xml.etree import ElementTree
from pathlib   import Path

import random


# -------------------------------------------------------------------------------------------------
# ---------------------------------------- Zone :: Library ----------------------------------------
# -------------------------------------------------------------------------------------------------
class Library(Zone):

    def __init__(self, decklist: str, *components: 'Node', **attributes: int) -> None:

        tree = ElementTree.parse(decklist)
        root = tree.getroot()

        super().__init__(*(
            Compiler.compile(Path(card.get('path'))) for card in root
        ))


    def visit(self, visitor: 'Visitor', context: 'Context') -> 'World':

        try:
            return visitor.visit_library(self, context)

        except AttributeError:
            return super().visit(visitor, context)

    def shuffle(self) -> None:
        random.shuffle(self.components)