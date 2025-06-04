# -------------------------------------------------------------------------------------------------
# --------------------------------- Ontology :: Zones :: Library ----------------------------------
# -------------------------------------------------------------------------------------------------
import random

from Platform.Interpreter.Compiler import Compiler

from Ontology.Abstract.Node import Node
from Ontology.Objects.Zone  import Zone
from Ontology.Objects.Card  import Card

from typing import TYPE_CHECKING
from typing import Generator

if TYPE_CHECKING:
    from Visitors.Context import Context
    from Visitors.Visitor import Visitor

from xml.etree import ElementTree
from pathlib   import Path
from random    import shuffle


# -------------------------------------------------------------------------------------------------
# ---------------------------------------- Zone :: Library ----------------------------------------
# -------------------------------------------------------------------------------------------------
class Library(Zone):

    def __init__(self, decklist: str = '', *components: 'Node', **attributes: int) -> None:

        tree = ElementTree.parse(decklist)
        root = tree.getroot()

        def compile(card) -> Card:

            path = Path(card.get('path'))
            text = path.read_text()

            return Compiler.compile(text)

        super().__init__(*map(compile, root), **attributes)

    def visit(self, visitor: 'Visitor', context: 'Context') -> 'Library':

        if visit := getattr(visitor, 'visit_library', None):
            return visit(self, context)

        return super().visit(visitor, context)

    def shuffle(self) -> 'Library':

        random.shuffle(self.components)

        return self