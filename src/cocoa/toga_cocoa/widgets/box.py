from rubicon.objc import *

from toga.interface import Box as BoxInterface

from ..libs import *
from .base import WidgetMixin

from typing import Any


class Box(BoxInterface, WidgetMixin):
    def __init__(self,
                 id: str = id,
                 style: Any = None,
                 children=None) -> None:
        super().__init__(id=id, style=style, children=children)
        self._create()

    def create(self) -> None:
        # # self._impl.setWantsLayer_(True)
        # # self._impl.setBackgroundColor_(NSColor.blueColor)

        self._constraints = None
