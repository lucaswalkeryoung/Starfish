# -------------------------------------------------------------------------------------------------
# ----------------- Taxonomy :: Taxonomic Class-to-Keyword Helpers and Constants ------------------
# -------------------------------------------------------------------------------------------------
from typing import TYPE_CHECKING
from typing import Callable
from typing import Iterable
from typing import Type
from typing import overload

if TYPE_CHECKING:
    from Ontology.Abstract.Node import Node

import collections


# -------------------------------------------------------------------------------------------------
# ------------------------------------------- Constants -------------------------------------------
# -------------------------------------------------------------------------------------------------
SINGULAR_TO_SPECIES = {}
SPECIES_TO_SINGULAR = {}
PLURAL_TO_SPECIES   = {}
SPECIES_TO_PLURAL   = {}
SINGULAR_TO_ATOM    = {}
PLURAL_TO_ATOM      = {}


# -------------------------------------------------------------------------------------------------
# ---------------------------------------- Register a Node ----------------------------------------
# -------------------------------------------------------------------------------------------------
def register(singular: str = '', plural: str = '', atom: Type = None) -> Callable[[Type], Type]:

    def decorator(species: Type) -> Type:

        if singular:
            SINGULAR_TO_SPECIES[singular] = species
            SPECIES_TO_SINGULAR[species] = singular

        if plural:
            PLURAL_TO_SPECIES[plural] = species
            SPECIES_TO_PLURAL[species] = plural

        if atom:
            SINGULAR_TO_ATOM[singular] = atom
            PLURAL_TO_ATOM[plural] = atom

        return species

    return decorator


# -------------------------------------------------------------------------------------------------
# --------------------- HELPER :: Partition Kwargs by Atom (Singular Keyword) ---------------------
# -------------------------------------------------------------------------------------------------
def partition_single(attributes: dict[str, int]) -> dict[type, dict[str, int]]:

    grouped = collections.defaultdict(dict)

    for attribute, value in attributes.items():
        grouped[SINGULAR_TO_ATOM[attribute]][attribute] = value

    return grouped


# -------------------------------------------------------------------------------------------------
# ---------------------- HELPER :: Partition Kwargs by Atom (Plural Keyword) ----------------------
# -------------------------------------------------------------------------------------------------
def partition_plural(attributes: dict[str, int]) -> dict[type, dict[str, int]]:
    grouped = collections.defaultdict(dict)

    for attribute, value in attributes.items():
        grouped[SINGULAR_TO_ATOM[attribute]][attribute] = value

    return grouped


# -------------------------------------------------------------------------------------------------
# --------------------- HELPER :: Partition Components by Type (into Groups) ----------------------
# -------------------------------------------------------------------------------------------------
def sort_plural(components: Iterable['Node']) -> dict[type, list['Node']]:

    grouped = collections.defaultdict(list)

    for component in components:
        grouped[type(component)].append(component)

    return grouped


# -------------------------------------------------------------------------------------------------
# -------------------- HELPER :: Partition Components by Type (One Entry Per) ---------------------
# -------------------------------------------------------------------------------------------------
def sort_single(components: Iterable['Node']):

    grouped = dict()

    for component in components:
        grouped[type(component)] = component

    return grouped