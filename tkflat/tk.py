import tkinter
from .styled import Styled


class Tk(tkinter.Tk, Styled):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        Styled.__init__(self)

        self._widget_name = "Window"

        self.configure(background=self.style("bg"))