# -------------------------------------------------------------------------------------------------
# --------------- Taxonomy :: Taxonomic Node Classification and Reference Utilities ---------------
# -------------------------------------------------------------------------------------------------
from typing import TYPE_CHECKING
from typing import Callable
from typing import Literal
from typing import overload

if TYPE_CHECKING:
    from Ontology.Abstract.Node import Node

from collections import defaultdict


# -------------------------------------------------------------------------------------------------
# --------------------------------- Taxonomic Container Cnnstants ---------------------------------
# -------------------------------------------------------------------------------------------------
SINGULAR_TO_PLURAL  = {}
PLURAL_TO_SINGULAR  = {}
SINGULAR_TO_SPECIES = {}
PLURAL_TO_SPECIES   = {}
SPECIES_TO_SINGULAR = {}
SPECIES_TO_PLURAL   = {}
SINGULAR_TO_ATOM    = {}
PLURAL_TO_ATOM      = {}


# -------------------------------------------------------------------------------------------------
# ------------------------------- UTILITY :: Register a Node Class --------------------------------
# -------------------------------------------------------------------------------------------------
def register(singular: str = '', plural: str = '', atom: type = None) -> Callable[[type], type]:

    def register(species: type) -> type:

        if singular and plural:
            SINGULAR_TO_PLURAL[singular] = plural
            PLURAL_TO_SINGULAR[plural] = singular

        if singular and atom:
            SINGULAR_TO_ATOM[singular] = atom

        if plural and atom:
            PLURAL_TO_ATOM[singular] = atom

        if singular:
            SPECIES_TO_SINGULAR[species] = singular
            SINGULAR_TO_SPECIES[singular] = species

        if plural:
            SPECIES_TO_PLURAL[species] = singular
            PLURAL_TO_SPECIES[singular] = species

        return species

    return register


# -------------------------------------------------------------------------------------------------
# ---------------------------- UTILITY :: Partition Attributes by Atom ----------------------------
# -------------------------------------------------------------------------------------------------
def partition(attributes: dict[str, int]) -> dict[type, dict[str, int]]:

    output = defaultdict(dict)

    for attribute, value in attributes.items():
        output[SINGULAR_TO_ATOM][attribute] = value

    return output


# -------------------------------------------------------------------------------------------------
# ---------------------- UTILITY :: Partition Components by Type into Groups ----------------------
# -------------------------------------------------------------------------------------------------
def sort_multiple(components: list['Node']) -> dict[type, list['Node']]:

    output = defaultdict(list)

    for component in components:
        output[type(component)].append(component)

    return output


# -------------------------------------------------------------------------------------------------
# ----------------- UTILITY :: Partition Components by Type into Singluar Objects -----------------
# -------------------------------------------------------------------------------------------------
def sort_singular(components: list['Node']) -> dict[type, 'Node']:

    output = dict()

    for component in components:
        output[type(component)] = component

    return output


# -------------------------------------------------------------------------------------------------
# ---------------------------- Import and Register Every Node Subclass ----------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node  import Node
from Ontology.Objects.Object import Object
from Ontology.Objects.Player import Player
from Ontology.Objects.Card   import Card
from Ontology.Objects.Zone   import Zone
from Ontology.Zones.World    import World
