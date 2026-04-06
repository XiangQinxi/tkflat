from .theme import Theme


class Styled:
    def __init__(self):
        self._theme = Theme()
        self.theme = self._theme.get_using_theme()
        self._widget_name = "Frame"
        self._state = None

    def style(self, style_name: str) -> str | int:
        return self._theme.style(self._widget_name, self._state, style_name)
