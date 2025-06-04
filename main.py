from Platform.Interpreter.Interpreter import Interpreter

from Ontology.Objects.Player import Player
from Ontology.Zones.World    import World
from Ontology.Zones.Library  import Library

Interpreter.run(
    World(
        Player(
            Library(decklist='Archives/Decks/Test.xml'),
        ),
    ),
)