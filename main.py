from Platform.Interpreter.Interpreter import Interpreter
from Ontology.Zones.World import World
from Ontology.Zones.Library import Library
from Ontology.Objects.Player import Player

Interpreter.interpret(
    World(
        Player(
            Library(decklist='Archives/Decks/Deck.xml'),
        ),
    ),
)