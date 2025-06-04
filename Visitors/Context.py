# -------------------------------------------------------------------------------------------------
# ------------------------------- Visitors :: Visitor Context Helper ------------------------------
# -------------------------------------------------------------------------------------------------
from collections import ChainMap

from typing import Any
from typing import Optional


# -------------------------------------------------------------------------------------------------
# ----------------------------------- Helper :: Visitor Context -----------------------------------
# -------------------------------------------------------------------------------------------------
class Context(object):

    def __init__(self, parent: Optional['Context'] = None) -> None:

        self.parent   = parent
        self.children = []
        self.context  = {}

    def descend(self) -> 'Context':
        return Context(parent=self)

    def ascend(self) -> ChainMap[str, int]:

        ancestry = list()
        ancestor = self

        while ancestor:
            ancestry.append(ancestor.context)
            ancestor = ancestor.parent

        return ChainMap(*ancestry)

    def get(self, key: str, default: Any = None) -> Any:
        return self.ascend().get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.context[key] = value