import tkinter
from .styled import Styled



class Frame(tkinter.Frame, Styled):
    def __init__(self, *args, **kwargs):
        tkinter.Frame.__init__(self, *args, **kwargs)
        Styled.__init__(self)

        self._widget_name = "Frame"

        self.configure(background=self.style("bg"), highlightthickness=self.style("border_width"), highlightbackground=self.style("border"))