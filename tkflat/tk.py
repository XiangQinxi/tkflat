import tkinter

from .theme import using_theme


class Tk(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._widget_name = "Window"
        self._theme = using_theme

        self.configure(background=using_theme["styles"]["bg"])
