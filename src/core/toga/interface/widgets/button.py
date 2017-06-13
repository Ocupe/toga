from .base import Widget

from typing import Callable, Any

class Button(Widget):
    """
    Button widget, a clickable button

    :param label:       Text to be shown on the button
    :type label:        ``str``

    :param id:          An identifier for this widget.
    :type  id:          ``str``

    :param style:       an optional style object. If no style is provided then a
                        new one will be created for the widget.
    :type style:        :class:`colosseum.CSSNode`

    :param on_press:    Function to execute when pressed
    :type on_press:     ``callable``
    """
    def __init__(self,
                 label: str,
                 id: str = None,
                 style=None,
                 on_press: Callable = None,
                 enabled: bool = None,
                 background_color: Any = None) -> None:
        super().__init__(id=id, style=style, label=label, on_press=on_press,
                         enabled=enabled, background_color=background_color)

    def _configure(self, label, on_press, enabled, background_color):
        self.label = label
        self.on_press = on_press
        self.enabled = enabled
        self.background_color = background_color

    @property
    def label(self) -> str:
        """
        :returns: The label value
        :rtype: ``str``
        """
        return self._label

    @label.setter
    def label(self, value: str) -> None:
        """
        Set the label value

        :param value: The new label value
        :type  value: ``str``
        """
        if value is None:
            self._label = ''
        else:
            self._label = str(value)
        self._set_label(str(value))
        self.rehint()

    def _set_label(self, value: str) -> None:
        raise NotImplementedError('Button widget must define _set_label()')

    @property
    def on_press(self) -> Callable:
        """
        The callable function for when the button is pressed

        :rtype: ``callable``
        """
        return self._on_press

    @on_press.setter
    def on_press(self, handler: Callable) -> None:
        """
        Set the function to be executed on button press.

        :param handler:     callback function
        :type handler:      ``callable``
        """
        self._on_press = handler
        self._set_on_press(handler)

    def _set_on_press(self, value:Callable) -> None:
        pass

    @property
    def enabled(self) -> bool:
        """
        Indicates whether the button can be pressed by the user.

        :returns:   Button status. Default is True.
        :rtype:     ``Bool`
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        """
        Set if the button can be pressed by the user.

        :param value:   Enabled state for button
        :type value:    ``Bool``
        """
        if value is None:
            self._enabled = True
        else:
            self._enabled = value
        self._set_enabled(value)

    def _set_enabled(self, value: bool) -> None:
        raise NotImplementedError('Button widget must define _set_enabled()')

    @property
    def background_color(self) -> Any:
        """
        Indicates the button background color.
        :returns:   Button background color. Default is None.
        :rtype:     ``str` or ``tuple``
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value: Any) -> None:
        """
        Set the button background color.
        :param value:   Button background color
        :type value:    ``str` or ``tuple``
        """

        self._background_color = value
        self._set_background_color(value)

    def _set_background_color(self, value: Any) -> None:
        raise NotImplementedError('Button widget must define \
                                    _set_background_color()')
