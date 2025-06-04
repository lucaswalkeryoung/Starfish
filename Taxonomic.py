# others_singular = [
#     'aura',
#     'background',
#     'cartouche',
#     'class',
#     'curse',
#     'role',
#     'room',
#     'rune',
#     'saga',
#     'shard',
#     'shrine',
#     'clue',
#     'contraption',
#     'equipment',
#     'food',
#     'fortification',
#     'gold',
#     'powerstone',
#     'treasure',
#     'vehicle',
#     'adventure',
#     'arcane',
#     'lesson',
#     'omen',
#     'trap',
#     'scheme',
#     'phenomenon',
#     'vanguard',
# ]
#
# others_plural = [
#     'aura',
#     'backgrounds',
#     'cartouches',
#     'classes',
#     'curses',
#     'roles',
#     'rooms',
#     'runes',
#     'sagas',
#     'shards',
#     'shrines',
#     'clues',
#     'contraptions',
#     'equipment',
#     'food',
#     'fortifications',
#     'gold',
#     'powerstones',
#     'treasure',
#     'vehicles',
#     'adventures',
#     'arcane',
#     'lessons',
#     'omens',
#     'traps',
#     'schemes',
#     'phenomenea',
#     'vanguard',
# ]
#
# others = zip(others_singular, others_plural)
#
# import pathlib
#
# for singular, plural in others:
#
#     file = pathlib.Path(f'Ontology/Shorthand/Subtypes/Others/{plural.title()}.py')
#
#     title = f'{f" Ontology :: Shorthand :: Subtypes :: Others :: {file.stem} ":-^97}'
#     subtitle = f'{f" Shorthand :: {file.stem} ":-^97}'
#
#     raw = f"""
# # -------------------------------------------------------------------------------------------------
# # { title }
# # -------------------------------------------------------------------------------------------------
# from Ontology.Shorthand.Abstract.Shorthand import Shorthand
# from Ontology.Shorthand.Abstract.Criterand import Criterand
# from Ontology.Abstract.Node import Node
#
# from Ontology.Atoms.Subtype import Subtype
#
# from typing import TYPE_CHECKING
#
# if TYPE_CHECKING:
#     from Visitors.Visitor import Visitor
#     from Visitors.Context import Context
#
# from Taxonomy import Taxonomy
#
#
# # -------------------------------------------------------------------------------------------------
# # { subtitle }
# # -------------------------------------------------------------------------------------------------
# @Taxonomy.register(singular='{singular}', plural='{plural}', atom=Subtype)
# class {file.stem}(Criterand, Shorthand):
#
#     def __init__(self, *components: Node, **attributes: int) -> None:
#         super().__init__(*components, **attributes)
#
#     def visit(self, visitor: 'Visitor', context: 'Context') -> '{file.stem}':
#
#         if visit := getattr(visitor, 'visit_{file.stem.lower()}', None):
#             return visit(self, context)
#
#         return super().visit(visitor, context)
#
# """
#
#     file.write_text(raw)

import pathlib

for file in sorted(pathlib.Path('Ontology').rglob('*.py')):

    main = str(file.with_suffix('')).replace('/', '.')
    name = file.stem

    print(f"from {main} import {name}")