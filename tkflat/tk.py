import tkinter

from .theme import using_theme


class Tk(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._style = "Window"
        self._theme = using_theme

        self.configure(background=using_theme[self._style]["bg"])
