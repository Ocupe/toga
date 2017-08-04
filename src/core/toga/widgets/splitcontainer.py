from .base import Widget


class SplitContainer(Widget):
    """
    Split container widget
    """
    HORIZONTAL = False
    VERTICAL = True

    def __init__(self, id=None, style=None, direction=VERTICAL, content=None, factory=None):
        """ Instantiate a new instance of the split container widget

        :param id:          An identifier for this widget.
        :type  id:          ``str``

        :param style:       an optional style object. If no style is provided then a
                            new one will be created for the widget.
        :type style:        :class:`colosseum.CSSNode`

        :param direction: The direction for the container split, either `SplitContainer.HORIZONTAL` or
            `SplitContainer.VERTICAL`
        :type  direction: ``bool``

        :param content: The list of components to be split
        :type  content: ``list`` of :class:`toga.Widget`
        """
        super().__init__(id=id, style=style, factory=factory)
        self._direction = direction
        self._containers = []

        # Create a platform specific implementation of a SplitContainer
        self._impl = self.factory.SplitContainer(interface=self)

        self.content = content
        self.direction = direction

    @property
    def content(self):
        """
        The content of the split container

        :rtype: ``list`` of :class:`toga.Widget`
        """
        return self._content

    @content.setter
    def content(self, content):
        if content is None:
            self._content = None
            return

        if len(content) < 2:
            raise ValueError('SplitContainer content must have at least 2 elements')

        self._content = content

        for position, widget in enumerate(self._content):
            widget._update_layout()
            widget.app = self.app
            widget.window = self.window
            self._impl.add_content(position, widget._impl)

    def _set_app(self, app):
        if self._content:
            for content in self._content:
                content.app = self.app

    def _set_window(self, window):
        if self._content:
            for content in self._content:
                content.window = self.window

    @property
    def direction(self):
        """
        The direction of the split

        :rtype: ``bool``
        """
        return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value
        self._impl.set_direction(value)
        self.rehint()