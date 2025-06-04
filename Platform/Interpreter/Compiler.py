# -------------------------------------------------------------------------------------------------
# ------------------------------ Platform :: Interpreter :: Compiler ------------------------------
# -------------------------------------------------------------------------------------------------
from Ontology.Abstract.Node import Node
from Ontology.Atoms.Archetype import Archetype
from Ontology.Atoms.Atom import Atom
from Ontology.Atoms.Color import Color
from Ontology.Atoms.Role import Role
from Ontology.Atoms.Subtype import Subtype
from Ontology.Atoms.Supertype import Supertype
from Ontology.Atoms.Type import Type
from Ontology.Components.Component import Component
from Ontology.Components.Eligibility import Eligibility
from Ontology.Components.Identity import Identity
from Ontology.Components.Negative import Negative
from Ontology.Components.Phase import Phase
from Ontology.Components.Positive import Positive
from Ontology.Components.Step import Step
from Ontology.Components.Turn import Turn
from Ontology.Logic.Logic import Logic
from Ontology.Mechanics.Cast import Cast
from Ontology.Mechanics.Mechanic import Mechanic
from Ontology.Mechanics.Play import Play
from Ontology.Objects.Card import Card
from Ontology.Objects.Object import Object
from Ontology.Objects.Zone import Zone
from Ontology.Shorthand.Abstract.Criterand import Criterand
from Ontology.Shorthand.Abstract.Explorand import Explorand
from Ontology.Shorthand.Abstract.Shorthand import Shorthand
from Ontology.Shorthand.Archetypes.Abilities import Abilities
from Ontology.Shorthand.Archetypes.Cards import Cards
from Ontology.Shorthand.Archetypes.Counters import Counters
from Ontology.Shorthand.Archetypes.Damage import Damage
from Ontology.Shorthand.Archetypes.Effects import Effects
from Ontology.Shorthand.Archetypes.Emblems import Emblems
from Ontology.Shorthand.Archetypes.Keywords import Keywords
from Ontology.Shorthand.Archetypes.Mana import Mana
from Ontology.Shorthand.Archetypes.Permanents import Permanents
from Ontology.Shorthand.Archetypes.Players import Players
from Ontology.Shorthand.Archetypes.Spells import Spells
from Ontology.Shorthand.Archetypes.Tokens import Tokens
from Ontology.Shorthand.Archetypes.Zones import Zones
from Ontology.Shorthand.Colors.Black import Black
from Ontology.Shorthand.Colors.Blue import Blue
from Ontology.Shorthand.Colors.Colorless import Colorless
from Ontology.Shorthand.Colors.Generic import Generic
from Ontology.Shorthand.Colors.Green import Green
from Ontology.Shorthand.Colors.Red import Red
from Ontology.Shorthand.Colors.White import White
from Ontology.Shorthand.Subtypes.Biomes.Caves import Caves
from Ontology.Shorthand.Subtypes.Biomes.Deserts import Deserts
from Ontology.Shorthand.Subtypes.Biomes.Gates import Gates
from Ontology.Shorthand.Subtypes.Biomes.Islands import Islands
from Ontology.Shorthand.Subtypes.Biomes.Lairs import Lairs
from Ontology.Shorthand.Subtypes.Biomes.Locus import Locus
from Ontology.Shorthand.Subtypes.Biomes.Mines import Mines
from Ontology.Shorthand.Subtypes.Biomes.Mountains import Mountains
from Ontology.Shorthand.Subtypes.Biomes.Plains import Plains
from Ontology.Shorthand.Subtypes.Biomes.Powerplants import Powerplants
from Ontology.Shorthand.Subtypes.Biomes.Spheres import Spheres
from Ontology.Shorthand.Subtypes.Biomes.Swamps import Swamps
from Ontology.Shorthand.Subtypes.Biomes.Towers import Towers
from Ontology.Shorthand.Subtypes.Biomes.Urzas import Urzas
from Ontology.Shorthand.Subtypes.Biomes.Wastes import Wastes
from Ontology.Shorthand.Subtypes.Others.Adventures import Adventures
from Ontology.Shorthand.Subtypes.Others.Arcane import Arcane
from Ontology.Shorthand.Subtypes.Others.Aura import Aura
from Ontology.Shorthand.Subtypes.Others.Backgrounds import Backgrounds
from Ontology.Shorthand.Subtypes.Others.Cartouches import Cartouches
from Ontology.Shorthand.Subtypes.Others.Classes import Classes
from Ontology.Shorthand.Subtypes.Others.Clues import Clues
from Ontology.Shorthand.Subtypes.Others.Contraptions import Contraptions
from Ontology.Shorthand.Subtypes.Others.Curses import Curses
from Ontology.Shorthand.Subtypes.Others.Equipment import Equipment
from Ontology.Shorthand.Subtypes.Others.Food import Food
from Ontology.Shorthand.Subtypes.Others.Fortifications import Fortifications
from Ontology.Shorthand.Subtypes.Others.Gold import Gold
from Ontology.Shorthand.Subtypes.Others.Lessons import Lessons
from Ontology.Shorthand.Subtypes.Others.Omens import Omens
from Ontology.Shorthand.Subtypes.Others.Phenomenea import Phenomenea
from Ontology.Shorthand.Subtypes.Others.Powerstones import Powerstones
from Ontology.Shorthand.Subtypes.Others.Roles import Roles
from Ontology.Shorthand.Subtypes.Others.Rooms import Rooms
from Ontology.Shorthand.Subtypes.Others.Runes import Runes
from Ontology.Shorthand.Subtypes.Others.Sagas import Sagas
from Ontology.Shorthand.Subtypes.Others.Schemes import Schemes
from Ontology.Shorthand.Subtypes.Others.Shards import Shards
from Ontology.Shorthand.Subtypes.Others.Shrines import Shrines
from Ontology.Shorthand.Subtypes.Others.Traps import Traps
from Ontology.Shorthand.Subtypes.Others.Treasure import Treasure
from Ontology.Shorthand.Subtypes.Others.Vanguard import Vanguard
from Ontology.Shorthand.Subtypes.Others.Vehicles import Vehicles
from Ontology.Shorthand.Subtypes.Titles.Ajani import Ajani
from Ontology.Shorthand.Subtypes.Titles.Aminatou import Aminatou
from Ontology.Shorthand.Subtypes.Titles.Angrath import Angrath
from Ontology.Shorthand.Subtypes.Titles.Arlin import Arlin
from Ontology.Shorthand.Subtypes.Titles.Ashiok import Ashiok
from Ontology.Shorthand.Subtypes.Titles.Bahamut import Bahamut
from Ontology.Shorthand.Subtypes.Titles.Basri import Basri
from Ontology.Shorthand.Subtypes.Titles.Bolas import Bolas
from Ontology.Shorthand.Subtypes.Titles.Calix import Calix
from Ontology.Shorthand.Subtypes.Titles.Chandra import Chandra
from Ontology.Shorthand.Subtypes.Titles.Comet import Comet
from Ontology.Shorthand.Subtypes.Titles.Dack import Dack
from Ontology.Shorthand.Subtypes.Titles.Dakkon import Dakkon
from Ontology.Shorthand.Subtypes.Titles.Daretti import Daretti
from Ontology.Shorthand.Subtypes.Titles.Davriel import Davriel
from Ontology.Shorthand.Subtypes.Titles.Dihada import Dihada
from Ontology.Shorthand.Subtypes.Titles.Domri import Domri
from Ontology.Shorthand.Subtypes.Titles.Dovin import Dovin
from Ontology.Shorthand.Subtypes.Titles.Ellywick import Ellywick
from Ontology.Shorthand.Subtypes.Titles.Elminster import Elminster
from Ontology.Shorthand.Subtypes.Titles.Elspeth import Elspeth
from Ontology.Shorthand.Subtypes.Titles.Estrid import Estrid
from Ontology.Shorthand.Subtypes.Titles.Freyalise import Freyalise
from Ontology.Shorthand.Subtypes.Titles.Garruk import Garruk
from Ontology.Shorthand.Subtypes.Titles.Gideon import Gideon
from Ontology.Shorthand.Subtypes.Titles.Grist import Grist
from Ontology.Shorthand.Subtypes.Titles.Guff import Guff
from Ontology.Shorthand.Subtypes.Titles.Huatli import Huatli
from Ontology.Shorthand.Subtypes.Titles.Jace import Jace
from Ontology.Shorthand.Subtypes.Titles.Jared import Jared
from Ontology.Shorthand.Subtypes.Titles.Jaya import Jaya
from Ontology.Shorthand.Subtypes.Titles.Jeska import Jeska
from Ontology.Shorthand.Subtypes.Titles.Kaito import Kaito
from Ontology.Shorthand.Subtypes.Titles.Karn import Karn
from Ontology.Shorthand.Subtypes.Titles.Kasmina import Kasmina
from Ontology.Shorthand.Subtypes.Titles.Kaya import Kaya
from Ontology.Shorthand.Subtypes.Titles.Kiora import Kiora
from Ontology.Shorthand.Subtypes.Titles.Koth import Koth
from Ontology.Shorthand.Subtypes.Titles.Liliana import Liliana
from Ontology.Shorthand.Subtypes.Titles.Lolth import Lolth
from Ontology.Shorthand.Subtypes.Titles.Lukka import Lukka
from Ontology.Shorthand.Subtypes.Titles.Minsc import Minsc
from Ontology.Shorthand.Subtypes.Titles.Mordenkainen import Mordenkainen
from Ontology.Shorthand.Subtypes.Titles.Nahiri import Nahiri
from Ontology.Shorthand.Subtypes.Titles.Narset import Narset
from Ontology.Shorthand.Subtypes.Titles.Niko import Niko
from Ontology.Shorthand.Subtypes.Titles.Nissa import Nissa
from Ontology.Shorthand.Subtypes.Titles.Nixilis import Nixilis
from Ontology.Shorthand.Subtypes.Titles.Oko import Oko
from Ontology.Shorthand.Subtypes.Titles.Ral import Ral
from Ontology.Shorthand.Subtypes.Titles.Rowan import Rowan
from Ontology.Shorthand.Subtypes.Titles.Saheeli import Saheeli
from Ontology.Shorthand.Subtypes.Titles.Samut import Samut
from Ontology.Shorthand.Subtypes.Titles.Sarkhan import Sarkhan
from Ontology.Shorthand.Subtypes.Titles.Serra import Serra
from Ontology.Shorthand.Subtypes.Titles.Sivitri import Sivitri
from Ontology.Shorthand.Subtypes.Titles.Sorin import Sorin
from Ontology.Shorthand.Subtypes.Titles.Szat import Szat
from Ontology.Shorthand.Subtypes.Titles.Tamiyo import Tamiyo
from Ontology.Shorthand.Subtypes.Titles.Tasha import Tasha
from Ontology.Shorthand.Subtypes.Titles.Teferi import Teferi
from Ontology.Shorthand.Subtypes.Titles.Teyo import Teyo
from Ontology.Shorthand.Subtypes.Titles.Tezzeret import Tezzeret
from Ontology.Shorthand.Subtypes.Titles.Tibalt import Tibalt
from Ontology.Shorthand.Subtypes.Titles.Tyvar import Tyvar
from Ontology.Shorthand.Subtypes.Titles.Ugin import Ugin
from Ontology.Shorthand.Subtypes.Titles.Urza import Urza
from Ontology.Shorthand.Subtypes.Titles.Venser import Venser
from Ontology.Shorthand.Subtypes.Titles.Vivien import Vivien
from Ontology.Shorthand.Subtypes.Titles.Vraska import Vraska
from Ontology.Shorthand.Subtypes.Titles.Vronos import Vronos
from Ontology.Shorthand.Subtypes.Titles.Will import Will
from Ontology.Shorthand.Subtypes.Titles.Windgrace import Windgrace
from Ontology.Shorthand.Subtypes.Titles.Wrenn import Wrenn
from Ontology.Shorthand.Subtypes.Titles.Xenagos import Xenagos
from Ontology.Shorthand.Subtypes.Titles.Yanggu import Yanggu
from Ontology.Shorthand.Subtypes.Titles.Yanling import Yanling
from Ontology.Shorthand.Subtypes.Titles.Zariel import Zariel
from Ontology.Shorthand.Subtypes.Tribes.Advisors import Advisors
from Ontology.Shorthand.Subtypes.Tribes.Aetherborn import Aetherborn
from Ontology.Shorthand.Subtypes.Tribes.Aliens import Aliens
from Ontology.Shorthand.Subtypes.Tribes.Allies import Allies
from Ontology.Shorthand.Subtypes.Tribes.Angels import Angels
from Ontology.Shorthand.Subtypes.Tribes.Antelopes import Antelopes
from Ontology.Shorthand.Subtypes.Tribes.Apes import Apes
from Ontology.Shorthand.Subtypes.Tribes.Archers import Archers
from Ontology.Shorthand.Subtypes.Tribes.Archons import Archons
from Ontology.Shorthand.Subtypes.Tribes.Armadillos import Armadillos
from Ontology.Shorthand.Subtypes.Tribes.Armies import Armies
from Ontology.Shorthand.Subtypes.Tribes.Artificers import Artificers
from Ontology.Shorthand.Subtypes.Tribes.Assassins import Assassins
from Ontology.Shorthand.Subtypes.Tribes.AssemblyWorkers import AssemblyWorkers
from Ontology.Shorthand.Subtypes.Tribes.Astartes import Astartes
from Ontology.Shorthand.Subtypes.Tribes.Atogs import Atogs
from Ontology.Shorthand.Subtypes.Tribes.Aurochs import Aurochs
from Ontology.Shorthand.Subtypes.Tribes.Avatars import Avatars
from Ontology.Shorthand.Subtypes.Tribes.Azra import Azra
from Ontology.Shorthand.Subtypes.Tribes.Badgers import Badgers
from Ontology.Shorthand.Subtypes.Tribes.Balloons import Balloons
from Ontology.Shorthand.Subtypes.Tribes.Barbarians import Barbarians
from Ontology.Shorthand.Subtypes.Tribes.Bards import Bards
from Ontology.Shorthand.Subtypes.Tribes.Basilisks import Basilisks
from Ontology.Shorthand.Subtypes.Tribes.Bats import Bats
from Ontology.Shorthand.Subtypes.Tribes.Bears import Bears
from Ontology.Shorthand.Subtypes.Tribes.Beasts import Beasts
from Ontology.Shorthand.Subtypes.Tribes.Beavers import Beavers
from Ontology.Shorthand.Subtypes.Tribes.Beebles import Beebles
from Ontology.Shorthand.Subtypes.Tribes.Beholders import Beholders
from Ontology.Shorthand.Subtypes.Tribes.Berserkers import Berserkers
from Ontology.Shorthand.Subtypes.Tribes.Birds import Birds
from Ontology.Shorthand.Subtypes.Tribes.Blinkmoths import Blinkmoths
from Ontology.Shorthand.Subtypes.Tribes.Boars import Boars
from Ontology.Shorthand.Subtypes.Tribes.Bringers import Bringers
from Ontology.Shorthand.Subtypes.Tribes.Brushwaggs import Brushwaggs
from Ontology.Shorthand.Subtypes.Tribes.Camarids import Camarids
from Ontology.Shorthand.Subtypes.Tribes.Camels import Camels
from Ontology.Shorthand.Subtypes.Tribes.Capybaras import Capybaras
from Ontology.Shorthand.Subtypes.Tribes.Caribous import Caribous
from Ontology.Shorthand.Subtypes.Tribes.Carriers import Carriers
from Ontology.Shorthand.Subtypes.Tribes.Cats import Cats
from Ontology.Shorthand.Subtypes.Tribes.Centaurs import Centaurs
from Ontology.Shorthand.Subtypes.Tribes.Cephalids import Cephalids
from Ontology.Shorthand.Subtypes.Tribes.Chimeras import Chimeras
from Ontology.Shorthand.Subtypes.Tribes.Citizens import Citizens
from Ontology.Shorthand.Subtypes.Tribes.Clerics import Clerics
from Ontology.Shorthand.Subtypes.Tribes.Clowns import Clowns
from Ontology.Shorthand.Subtypes.Tribes.Cockatrices import Cockatrices
from Ontology.Shorthand.Subtypes.Tribes.Constructs import Constructs
from Ontology.Shorthand.Subtypes.Tribes.Cowards import Cowards
from Ontology.Shorthand.Subtypes.Tribes.Crabs import Crabs
from Ontology.Shorthand.Subtypes.Tribes.Crocodiles import Crocodiles
from Ontology.Shorthand.Subtypes.Tribes.Ctans import Ctans
from Ontology.Shorthand.Subtypes.Tribes.Custodes import Custodes
from Ontology.Shorthand.Subtypes.Tribes.Cybermen import Cybermen
from Ontology.Shorthand.Subtypes.Tribes.Cyclopes import Cyclopes
from Ontology.Shorthand.Subtypes.Tribes.Daleks import Daleks
from Ontology.Shorthand.Subtypes.Tribes.Dauthi import Dauthi
from Ontology.Shorthand.Subtypes.Tribes.Demigods import Demigods
from Ontology.Shorthand.Subtypes.Tribes.Demons import Demons
from Ontology.Shorthand.Subtypes.Tribes.Deserters import Deserters
from Ontology.Shorthand.Subtypes.Tribes.Detectives import Detectives
from Ontology.Shorthand.Subtypes.Tribes.Devils import Devils
from Ontology.Shorthand.Subtypes.Tribes.Dinosaurs import Dinosaurs
from Ontology.Shorthand.Subtypes.Tribes.Djinns import Djinns
from Ontology.Shorthand.Subtypes.Tribes.Doctors import Doctors
from Ontology.Shorthand.Subtypes.Tribes.Dogs import Dogs
from Ontology.Shorthand.Subtypes.Tribes.Dragons import Dragons
from Ontology.Shorthand.Subtypes.Tribes.Drakes import Drakes
from Ontology.Shorthand.Subtypes.Tribes.Dreadnoughts import Dreadnoughts
from Ontology.Shorthand.Subtypes.Tribes.Drones import Drones
from Ontology.Shorthand.Subtypes.Tribes.Druids import Druids
from Ontology.Shorthand.Subtypes.Tribes.Dryads import Dryads
from Ontology.Shorthand.Subtypes.Tribes.Dwarves import Dwarves
from Ontology.Shorthand.Subtypes.Tribes.Efreets import Efreets
from Ontology.Shorthand.Subtypes.Tribes.Eggs import Eggs
from Ontology.Shorthand.Subtypes.Tribes.Elders import Elders
from Ontology.Shorthand.Subtypes.Tribes.Eldrazi import Eldrazi
from Ontology.Shorthand.Subtypes.Tribes.Elementals import Elementals
from Ontology.Shorthand.Subtypes.Tribes.Elephants import Elephants
from Ontology.Shorthand.Subtypes.Tribes.Elks import Elks
from Ontology.Shorthand.Subtypes.Tribes.Elves import Elves
from Ontology.Shorthand.Subtypes.Tribes.Employees import Employees
from Ontology.Shorthand.Subtypes.Tribes.Eyes import Eyes
from Ontology.Shorthand.Subtypes.Tribes.Faeries import Faeries
from Ontology.Shorthand.Subtypes.Tribes.Ferrets import Ferrets
from Ontology.Shorthand.Subtypes.Tribes.Fish import Fish
from Ontology.Shorthand.Subtypes.Tribes.Flagbearers import Flagbearers
from Ontology.Shorthand.Subtypes.Tribes.Foxes import Foxes
from Ontology.Shorthand.Subtypes.Tribes.Fractals import Fractals
from Ontology.Shorthand.Subtypes.Tribes.Frogs import Frogs
from Ontology.Shorthand.Subtypes.Tribes.Fungi import Fungi
from Ontology.Shorthand.Subtypes.Tribes.Gamers import Gamers
from Ontology.Shorthand.Subtypes.Tribes.Gargoyles import Gargoyles
from Ontology.Shorthand.Subtypes.Tribes.Germs import Germs
from Ontology.Shorthand.Subtypes.Tribes.Giants import Giants
from Ontology.Shorthand.Subtypes.Tribes.Gith import Gith
from Ontology.Shorthand.Subtypes.Tribes.Glimmers import Glimmers
from Ontology.Shorthand.Subtypes.Tribes.Gnolls import Gnolls
from Ontology.Shorthand.Subtypes.Tribes.Gnomes import Gnomes
from Ontology.Shorthand.Subtypes.Tribes.Goats import Goats
from Ontology.Shorthand.Subtypes.Tribes.Goblins import Goblins
from Ontology.Shorthand.Subtypes.Tribes.Gods import Gods
from Ontology.Shorthand.Subtypes.Tribes.Golems import Golems
from Ontology.Shorthand.Subtypes.Tribes.Gorgons import Gorgons
from Ontology.Shorthand.Subtypes.Tribes.Graveborn import Graveborn
from Ontology.Shorthand.Subtypes.Tribes.Gremlins import Gremlins
from Ontology.Shorthand.Subtypes.Tribes.Griffins import Griffins
from Ontology.Shorthand.Subtypes.Tribes.Guests import Guests
from Ontology.Shorthand.Subtypes.Tribes.Hags import Hags
from Ontology.Shorthand.Subtypes.Tribes.Halflings import Halflings
from Ontology.Shorthand.Subtypes.Tribes.Hamsters import Hamsters
from Ontology.Shorthand.Subtypes.Tribes.Harpies import Harpies
from Ontology.Shorthand.Subtypes.Tribes.Hellions import Hellions
from Ontology.Shorthand.Subtypes.Tribes.Hippogriffs import Hippogriffs
from Ontology.Shorthand.Subtypes.Tribes.Hippos import Hippos
from Ontology.Shorthand.Subtypes.Tribes.Homarids import Homarids
from Ontology.Shorthand.Subtypes.Tribes.Homunculi import Homunculi
from Ontology.Shorthand.Subtypes.Tribes.Horrors import Horrors
from Ontology.Shorthand.Subtypes.Tribes.Horses import Horses
from Ontology.Shorthand.Subtypes.Tribes.Humans import Humans
from Ontology.Shorthand.Subtypes.Tribes.Hydras import Hydras
from Ontology.Shorthand.Subtypes.Tribes.Hyenas import Hyenas
from Ontology.Shorthand.Subtypes.Tribes.Illusions import Illusions
from Ontology.Shorthand.Subtypes.Tribes.Imps import Imps
from Ontology.Shorthand.Subtypes.Tribes.Incarnations import Incarnations
from Ontology.Shorthand.Subtypes.Tribes.Inklings import Inklings
from Ontology.Shorthand.Subtypes.Tribes.Inquisitors import Inquisitors
from Ontology.Shorthand.Subtypes.Tribes.Insects import Insects
from Ontology.Shorthand.Subtypes.Tribes.Jackals import Jackals
from Ontology.Shorthand.Subtypes.Tribes.Jellyfish import Jellyfish
from Ontology.Shorthand.Subtypes.Tribes.Juggernauts import Juggernauts
from Ontology.Shorthand.Subtypes.Tribes.Kavus import Kavus
from Ontology.Shorthand.Subtypes.Tribes.Kirin import Kirin
from Ontology.Shorthand.Subtypes.Tribes.Kithkin import Kithkin
from Ontology.Shorthand.Subtypes.Tribes.Knights import Knights
from Ontology.Shorthand.Subtypes.Tribes.Kobolds import Kobolds
from Ontology.Shorthand.Subtypes.Tribes.Kor import Kor
from Ontology.Shorthand.Subtypes.Tribes.Krakens import Krakens
from Ontology.Shorthand.Subtypes.Tribes.Lamia import Lamia
from Ontology.Shorthand.Subtypes.Tribes.Lammasu import Lammasu
from Ontology.Shorthand.Subtypes.Tribes.Leeches import Leeches
from Ontology.Shorthand.Subtypes.Tribes.Leviathans import Leviathans
from Ontology.Shorthand.Subtypes.Tribes.Lhurgoyfs import Lhurgoyfs
from Ontology.Shorthand.Subtypes.Tribes.Licids import Licids
from Ontology.Shorthand.Subtypes.Tribes.Lizards import Lizards
from Ontology.Shorthand.Subtypes.Tribes.Llamas import Llamas
from Ontology.Shorthand.Subtypes.Tribes.Manticores import Manticores
from Ontology.Shorthand.Subtypes.Tribes.Masticores import Masticores
from Ontology.Shorthand.Subtypes.Tribes.Mercenaries import Mercenaries
from Ontology.Shorthand.Subtypes.Tribes.Merfolk import Merfolk
from Ontology.Shorthand.Subtypes.Tribes.Metathran import Metathran
from Ontology.Shorthand.Subtypes.Tribes.Mice import Mice
from Ontology.Shorthand.Subtypes.Tribes.Minions import Minions
from Ontology.Shorthand.Subtypes.Tribes.Minotaurs import Minotaurs
from Ontology.Shorthand.Subtypes.Tribes.Mites import Mites
from Ontology.Shorthand.Subtypes.Tribes.Moles import Moles
from Ontology.Shorthand.Subtypes.Tribes.Mongers import Mongers
from Ontology.Shorthand.Subtypes.Tribes.Mongooses import Mongooses
from Ontology.Shorthand.Subtypes.Tribes.Monkeys import Monkeys
from Ontology.Shorthand.Subtypes.Tribes.Monks import Monks
from Ontology.Shorthand.Subtypes.Tribes.Moonfolk import Moonfolk
from Ontology.Shorthand.Subtypes.Tribes.Mounts import Mounts
from Ontology.Shorthand.Subtypes.Tribes.Mutants import Mutants
from Ontology.Shorthand.Subtypes.Tribes.Myr import Myr
from Ontology.Shorthand.Subtypes.Tribes.Mystics import Mystics
from Ontology.Shorthand.Subtypes.Tribes.Nautili import Nautili
from Ontology.Shorthand.Subtypes.Tribes.Necrons import Necrons
from Ontology.Shorthand.Subtypes.Tribes.Nephilim import Nephilim
from Ontology.Shorthand.Subtypes.Tribes.Nightmares import Nightmares
from Ontology.Shorthand.Subtypes.Tribes.Nightstalkers import Nightstalkers
from Ontology.Shorthand.Subtypes.Tribes.Ninjas import Ninjas
from Ontology.Shorthand.Subtypes.Tribes.Nobles import Nobles
from Ontology.Shorthand.Subtypes.Tribes.Noggles import Noggles
from Ontology.Shorthand.Subtypes.Tribes.Nomads import Nomads
from Ontology.Shorthand.Subtypes.Tribes.Nymphs import Nymphs
from Ontology.Shorthand.Subtypes.Tribes.Octopuses import Octopuses
from Ontology.Shorthand.Subtypes.Tribes.Ogres import Ogres
from Ontology.Shorthand.Subtypes.Tribes.Oozes import Oozes
from Ontology.Shorthand.Subtypes.Tribes.Orbs import Orbs
from Ontology.Shorthand.Subtypes.Tribes.Orcs import Orcs
from Ontology.Shorthand.Subtypes.Tribes.Orggs import Orggs
from Ontology.Shorthand.Subtypes.Tribes.Otters import Otters
from Ontology.Shorthand.Subtypes.Tribes.Ouphes import Ouphes
from Ontology.Shorthand.Subtypes.Tribes.Oxen import Oxen
from Ontology.Shorthand.Subtypes.Tribes.Oysters import Oysters
from Ontology.Shorthand.Subtypes.Tribes.Pangolins import Pangolins
from Ontology.Shorthand.Subtypes.Tribes.Peasants import Peasants
from Ontology.Shorthand.Subtypes.Tribes.Pegasi import Pegasi
from Ontology.Shorthand.Subtypes.Tribes.Pentavites import Pentavites
from Ontology.Shorthand.Subtypes.Tribes.Performers import Performers
from Ontology.Shorthand.Subtypes.Tribes.Pests import Pests
from Ontology.Shorthand.Subtypes.Tribes.Phelddagrifs import Phelddagrifs
from Ontology.Shorthand.Subtypes.Tribes.Phoenixes import Phoenixes
from Ontology.Shorthand.Subtypes.Tribes.Phyrexians import Phyrexians
from Ontology.Shorthand.Subtypes.Tribes.Pilots import Pilots
from Ontology.Shorthand.Subtypes.Tribes.Pinchers import Pinchers
from Ontology.Shorthand.Subtypes.Tribes.Pirates import Pirates
from Ontology.Shorthand.Subtypes.Tribes.Plants import Plants
from Ontology.Shorthand.Subtypes.Tribes.Porcupines import Porcupines
from Ontology.Shorthand.Subtypes.Tribes.Possums import Possums
from Ontology.Shorthand.Subtypes.Tribes.Praetors import Praetors
from Ontology.Shorthand.Subtypes.Tribes.Primarchs import Primarchs
from Ontology.Shorthand.Subtypes.Tribes.Prisms import Prisms
from Ontology.Shorthand.Subtypes.Tribes.Processors import Processors
from Ontology.Shorthand.Subtypes.Tribes.Rabbits import Rabbits
from Ontology.Shorthand.Subtypes.Tribes.Raccoons import Raccoons
from Ontology.Shorthand.Subtypes.Tribes.Rangers import Rangers
from Ontology.Shorthand.Subtypes.Tribes.Rats import Rats
from Ontology.Shorthand.Subtypes.Tribes.Rebels import Rebels
from Ontology.Shorthand.Subtypes.Tribes.Reflections import Reflections
from Ontology.Shorthand.Subtypes.Tribes.Rhinos import Rhinos
from Ontology.Shorthand.Subtypes.Tribes.Riggers import Riggers
from Ontology.Shorthand.Subtypes.Tribes.Robots import Robots
from Ontology.Shorthand.Subtypes.Tribes.Rogues import Rogues
from Ontology.Shorthand.Subtypes.Tribes.Sables import Sables
from Ontology.Shorthand.Subtypes.Tribes.Salamanders import Salamanders
from Ontology.Shorthand.Subtypes.Tribes.Samurai import Samurai
from Ontology.Shorthand.Subtypes.Tribes.Sands import Sands
from Ontology.Shorthand.Subtypes.Tribes.Saprolings import Saprolings
from Ontology.Shorthand.Subtypes.Tribes.Satyrs import Satyrs
from Ontology.Shorthand.Subtypes.Tribes.Scarecrows import Scarecrows
from Ontology.Shorthand.Subtypes.Tribes.Scientists import Scientists
from Ontology.Shorthand.Subtypes.Tribes.Scions import Scions
from Ontology.Shorthand.Subtypes.Tribes.Scorpions import Scorpions
from Ontology.Shorthand.Subtypes.Tribes.Scouts import Scouts
from Ontology.Shorthand.Subtypes.Tribes.Sculptures import Sculptures
from Ontology.Shorthand.Subtypes.Tribes.Serfs import Serfs
from Ontology.Shorthand.Subtypes.Tribes.Serpents import Serpents
from Ontology.Shorthand.Subtypes.Tribes.Servos import Servos
from Ontology.Shorthand.Subtypes.Tribes.Shades import Shades
from Ontology.Shorthand.Subtypes.Tribes.Shamans import Shamans
from Ontology.Shorthand.Subtypes.Tribes.Shapeshifters import Shapeshifters
from Ontology.Shorthand.Subtypes.Tribes.Sharks import Sharks
from Ontology.Shorthand.Subtypes.Tribes.Sheep import Sheep
from Ontology.Shorthand.Subtypes.Tribes.Sirens import Sirens
from Ontology.Shorthand.Subtypes.Tribes.Skeletons import Skeletons
from Ontology.Shorthand.Subtypes.Tribes.Skunks import Skunks
from Ontology.Shorthand.Subtypes.Tribes.Sliths import Sliths
from Ontology.Shorthand.Subtypes.Tribes.Slivers import Slivers
from Ontology.Shorthand.Subtypes.Tribes.Sloths import Sloths
from Ontology.Shorthand.Subtypes.Tribes.Slugs import Slugs
from Ontology.Shorthand.Subtypes.Tribes.Snails import Snails
from Ontology.Shorthand.Subtypes.Tribes.Snakes import Snakes
from Ontology.Shorthand.Subtypes.Tribes.Soldiers import Soldiers
from Ontology.Shorthand.Subtypes.Tribes.Soltari import Soltari
from Ontology.Shorthand.Subtypes.Tribes.Spawns import Spawns
from Ontology.Shorthand.Subtypes.Tribes.Specters import Specters
from Ontology.Shorthand.Subtypes.Tribes.Spellshapers import Spellshapers
from Ontology.Shorthand.Subtypes.Tribes.Sphinxes import Sphinxes
from Ontology.Shorthand.Subtypes.Tribes.Spiders import Spiders
from Ontology.Shorthand.Subtypes.Tribes.Spikes import Spikes
from Ontology.Shorthand.Subtypes.Tribes.Spirits import Spirits
from Ontology.Shorthand.Subtypes.Tribes.Splinters import Splinters
from Ontology.Shorthand.Subtypes.Tribes.Sponges import Sponges
from Ontology.Shorthand.Subtypes.Tribes.Squids import Squids
from Ontology.Shorthand.Subtypes.Tribes.Squirrels import Squirrels
from Ontology.Shorthand.Subtypes.Tribes.Starfish import Starfish
from Ontology.Shorthand.Subtypes.Tribes.Surrakars import Surrakars
from Ontology.Shorthand.Subtypes.Tribes.Survivors import Survivors
from Ontology.Shorthand.Subtypes.Tribes.Synths import Synths
from Ontology.Shorthand.Subtypes.Tribes.Tentacles import Tentacles
from Ontology.Shorthand.Subtypes.Tribes.Tetravites import Tetravites
from Ontology.Shorthand.Subtypes.Tribes.Thalakos import Thalakos
from Ontology.Shorthand.Subtypes.Tribes.Thopters import Thopters
from Ontology.Shorthand.Subtypes.Tribes.Thrulls import Thrulls
from Ontology.Shorthand.Subtypes.Tribes.Tieflings import Tieflings
from Ontology.Shorthand.Subtypes.Tribes.Toys import Toys
from Ontology.Shorthand.Subtypes.Tribes.Treefolk import Treefolk
from Ontology.Shorthand.Subtypes.Tribes.Trilobites import Trilobites
from Ontology.Shorthand.Subtypes.Tribes.Triskelavites import Triskelavites
from Ontology.Shorthand.Subtypes.Tribes.Trolls import Trolls
from Ontology.Shorthand.Subtypes.Tribes.Turtles import Turtles
from Ontology.Shorthand.Subtypes.Tribes.Tyranids import Tyranids
from Ontology.Shorthand.Subtypes.Tribes.Unicorns import Unicorns
from Ontology.Shorthand.Subtypes.Tribes.Vampires import Vampires
from Ontology.Shorthand.Subtypes.Tribes.Varmints import Varmints
from Ontology.Shorthand.Subtypes.Tribes.Vedalken import Vedalken
from Ontology.Shorthand.Subtypes.Tribes.Volvers import Volvers
from Ontology.Shorthand.Subtypes.Tribes.Walls import Walls
from Ontology.Shorthand.Subtypes.Tribes.Walruses import Walruses
from Ontology.Shorthand.Subtypes.Tribes.Warlocks import Warlocks
from Ontology.Shorthand.Subtypes.Tribes.Warriors import Warriors
from Ontology.Shorthand.Subtypes.Tribes.Weasels import Weasels
from Ontology.Shorthand.Subtypes.Tribes.Weirds import Weirds
from Ontology.Shorthand.Subtypes.Tribes.Werewolves import Werewolves
from Ontology.Shorthand.Subtypes.Tribes.Whales import Whales
from Ontology.Shorthand.Subtypes.Tribes.Wizards import Wizards
from Ontology.Shorthand.Subtypes.Tribes.Wolverines import Wolverines
from Ontology.Shorthand.Subtypes.Tribes.Wolves import Wolves
from Ontology.Shorthand.Subtypes.Tribes.Wombats import Wombats
from Ontology.Shorthand.Subtypes.Tribes.Worms import Worms
from Ontology.Shorthand.Subtypes.Tribes.Wraiths import Wraiths
from Ontology.Shorthand.Subtypes.Tribes.Wurms import Wurms
from Ontology.Shorthand.Subtypes.Tribes.Yetis import Yetis
from Ontology.Shorthand.Subtypes.Tribes.Zombies import Zombies
from Ontology.Shorthand.Subtypes.Tribes.Zuberas import Zuberas
from Ontology.Shorthand.Supertypes.Basics import Basics
from Ontology.Shorthand.Supertypes.Legendaries import Legendaries
from Ontology.Shorthand.Supertypes.Ongoings import Ongoings
from Ontology.Shorthand.Supertypes.Snows import Snows
from Ontology.Shorthand.Supertypes.Worlds import Worlds
from Ontology.Shorthand.Types.Artifacts import Artifacts
from Ontology.Shorthand.Types.Battles import Battles
from Ontology.Shorthand.Types.Conspiracies import Conspiracies
from Ontology.Shorthand.Types.Creatures import Creatures
from Ontology.Shorthand.Types.Dungeons import Dungeons
from Ontology.Shorthand.Types.Enchantments import Enchantments
from Ontology.Shorthand.Types.Instants import Instants
from Ontology.Shorthand.Types.Kindred import Kindred
from Ontology.Shorthand.Types.Lands import Lands
from Ontology.Shorthand.Types.Phenomena import Phenomena
from Ontology.Shorthand.Types.Planes import Planes
from Ontology.Shorthand.Types.Planeswalkers import Planeswalkers
from Ontology.Shorthand.Types.Schemes import Schemes
from Ontology.Shorthand.Types.Sorceries import Sorceries
from Ontology.Shorthand.Types.Tribals import Tribals
from Ontology.Shorthand.Types.Vanguards import Vanguards
from Ontology.Zones.Battlefield import Battlefield
from Ontology.Zones.Clock import Clock
from Ontology.Zones.CommandZone import CommandZone
from Ontology.Zones.Exile import Exile
from Ontology.Zones.Graveyard import Graveyard
from Ontology.Zones.Hand import Hand
from Ontology.Zones.Heap import Heap
from Ontology.Zones.Outside import Outside
from Ontology.Zones.Pool import Pool
from Ontology.Zones.Stack import Stack

from Visitors.Context import Context
from Visitors.Visitor import Visitor

from typing import TYPE_CHECKING
from typing import Generator
from typing import overload

if TYPE_CHECKING:
    from Ontology.Objects.Player import Player
    from Ontology.Zones.Library  import Library
    from Ontology.Zones.World    import World

from Taxonomy import Taxonomy

import itertools


# -------------------------------------------------------------------------------------------------
# -------------------------------------- Visitor :: Compiler --------------------------------------
# -------------------------------------------------------------------------------------------------
class Compiler(Visitor):

    # -----------------------------------------------------------------------------------------
    # -------------------------- COMPILER :: Base Compilation Method --------------------------
    # -----------------------------------------------------------------------------------------
    def visit_node(self, node: Node, context: Context) -> Node:

        def compile() -> Generator[Node, None, None]:

            for component in node.components:
                yield component.visit(self, context.descend())

        return type(node)(*compile(), **node.attributes)


    # -----------------------------------------------------------------------------------------
    # ------------------- COMPILER :: Compile a Mana, Life, or Damage Pool --------------------
    # -----------------------------------------------------------------------------------------
    def visit_pool(self, node: Pool, context: Context) -> Pool:
        return Pool(Role(**node.attributes))


    # -----------------------------------------------------------------------------------------
    # -------------------------- COMPILER :: Compile a Player Object --------------------------
    # -----------------------------------------------------------------------------------------
    def visit_player(self, node: 'Player', context: Context) -> 'Player':

        components = map(lambda component : component.visit(self, context), [
            CommandZone(),
            Hand(),
            Graveyard(),
            Pool(mana=True),
            Pool(life=True),
            Pool(damage=True),
        ])

        return type(node)(*node.components, *components, **node.attributes)


    # -----------------------------------------------------------------------------------------
    # ----------------------------- COMPILER :: Compile the Clock -----------------------------
    # -----------------------------------------------------------------------------------------
    def visit_clock(self, node: Clock, context: Context) -> Clock:

        def compile() -> Generator[Turn, None, None]:

            for player in context.get('players'):

                yield Turn(
                    Phase(
                        Step(untap=True),
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
                )

        return Clock(*compile())


    # -----------------------------------------------------------------------------------------
    # ------------------------- COMPILER :: Compile the World Object --------------------------
    # -----------------------------------------------------------------------------------------
    def visit_world(self, node: 'World', context: Context) -> 'World':

        context.set('players', node.players)

        components = map(lambda component : component.visit(self, context), [
            Battlefield(),
            Exile(),
            Outside(),
            Stack(),
            Heap(),
            Clock(),
           *node.components, # player objects
        ])

        return type(node)(*components, **node.attributes)


    # -----------------------------------------------------------------------------------------
    # ---------------------------- COMPILER :: Compile an Identity ----------------------------
    # -----------------------------------------------------------------------------------------
    def visit_identity(self, node: Identity, context: Context) -> Identity:

        if node.attributes:

            partition  = Taxonomy.partition_single(node.attributes)

            archetypes = partition.get(Archetype, {})
            supertypes = partition.get(Supertype, {})
            types      = partition.get(Type, {})
            subtypes   = partition.get(Subtype, {})
            colors     = partition.get(Color, {})

            components = []

            for key, value in archetypes.items():
                components.append(Archetype(**{key: value}))

            for key, value in supertypes.items():
                components.append(Supertype(**{key: value}))

            for key, value in types.items():
                components.append(Type(**{key: value}))

            for key, value in subtypes.items():
                components.append(Subtype(**{key: value}))

            for key, value in colors.items():
                components.append(Color(**{key: value}))

            node = Identity(*components)

        return self.visit_node(node, context)


    # -----------------------------------------------------------------------------------------
    # -------------------------- COMPILER :: Compile a Play Mechanic --------------------------
    # -----------------------------------------------------------------------------------------
    def visit_play(self, node: Play, context: Context) -> Play:

        components = node.components
        components = list(map(lambda component : component.visit(self, context), components))

        plural = Taxonomy.sort_plural(components)
        single = Taxonomy.sort_single(components)

        if not single.get(Eligibility):

            components.append(
                Eligibility(
                    Role(play=True),
                    Positive(),
                    Negative(),
                )
            )

        return Play(*components, **node.attributes)

    # -----------------------------------------------------------------------------------------
    # -------------------------- COMPILER :: Compile a Cast Mechanic --------------------------
    # -----------------------------------------------------------------------------------------
    def visit_cast(self, node: Cast, context: Context) -> Cast:

        components = node.components
        components = list(map(lambda component: component.visit(self, context), components))

        plural = Taxonomy.sort_plural(components)
        single = Taxonomy.sort_single(components)

        if not single.get(Eligibility):

            components.append(
                Eligibility(
                    Role(play=True),
                    Positive(),
                    Negative(),
                )
            )

        if not single.get(Cost):
            components.append(Cost())

        return Cast(*components, **node.attributes)


    # -----------------------------------------------------------------------------------------
    # --------------------------- COMPILER :: Compile a Card Object ---------------------------
    # -----------------------------------------------------------------------------------------
    def visit_card(self, node: Card, context: Context) -> Card:

        components = node.components
        components = list(map(lambda component : component.visit(self, context), components))

        plural = Taxonomy.sort_plural(components)
        single = Taxonomy.sort_single(components)

        identity = single.get(Identity)
        plays    = plural.get(Play)
        casts    = plural.get(Cast)

        if 'land' in identity.types:

            if not plural.get(Play):
                components.append(Play().visit(self, context.descend()))

        elif not plural.get(Cast):
            components.append(Cast().visit(self, context.descend()))

        return Card(*components, **node.attributes)


    # -----------------------------------------------------------------------------------------
    # ------------------------ OVERLOADS :: Dual Compiler Entry Points ------------------------
    # -----------------------------------------------------------------------------------------
    @staticmethod
    @overload
    def compile(root: str) -> Card:
        ...

    @staticmethod
    @overload
    def compile(root: 'World') -> 'World':
        ...

    @staticmethod
    def compile(root: 'World | str') -> 'World':

        if isinstance(root, str):
            return eval(root).visit(Compiler(), Context())

        return root.visit(Compiler(), Context())