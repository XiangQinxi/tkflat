import tkinter
from tkinter import Event
from tkinter.font import Font
from typing import Literal

from .visual import Visual
from .font import default_font


class Text(Visual):
    def __init__(self, *args, width=120, height=68, font=None, **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self._style = "Text"

        if font is None:
            font = default_font()

        self._visual_attrs = {
            "font": font,
        }

        self.text = tkinter.Text(self, width=0, **kwargs)
        self._text_input_event = None
        self._text = self.create_window(0, 0, window=self.text, anchor="nw")

        self.bind("<FocusIn>", self._on_focus_in)
        self.text.bind("<FocusIn>", self._on_focus_in)
        self.text.bind("<FocusOut>", self._on_focus_out)
        self.text.bind("<Key>", lambda e: self.draw())
        self.text.bind("<Configure>", self._on_configure)
        self.text.bind("<Enter>", self._on_hover)
        self.text.bind("<Leave>", self._on_leave)

        self.draw()

    def _on_focus_in(self, event: Event):
        self._focused = True
        self.update_state()

    def _on_focus_out(self, event: Event):
        self._focused = False
        self.update_state()

    def update_state(self):
        if self._focused:
            self._state = "focus"
        else:
            if self._enter:
                self._state = "hover"
            else:
                self._state = None
        self.draw()

    def focus_set(self):
        self.text.focus_set()

    def draw(self):
        # self.coords(self._border, 0, 0, self.winfo_width(), self.winfo_height())
        border_width = self.style("border_width")
        self.coords(self._text, border_width, border_width)
        self.configure(
            background=self.style("bg"),  # bg color
            highlightbackground=self.style("border"),  # Border color
            # borderwidth=self._theme[self._style][self._state]["border_width"],  # Border width
            highlightthickness=border_width,
        )
        self.itemconfigure(
            self._text,
            width=self.winfo_width() - border_width * 2,
            height=self.winfo_height() - border_width * 2,
        )
        self.text.configure(
            background=self.style("bg"),
            borderwidth=0,
            highlightthickness=0,
            foreground=self.style("text"),
            insertbackground=self.style("text"),
            insertborderwidth=1,
            font=self.cget("font"),
        )
        # self.itemconfigure(self._text, width=0)
