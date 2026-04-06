import tkinter
from tkinter import Event

from .font import default_font
from .visual import Visual


class Entry(Visual):
    def __init__(self, *args, font=None, **kwargs):
        super().__init__(*args, **kwargs)

        self._widget_name = "Entry"

        if font is None:
            font = default_font()

        self._visual_attrs = {
            "font": font,
        }

        self.entry = tkinter.Entry(self, width=0, **kwargs)
        self._entry_input_event = None
        self._entry = self.create_window(0, 0, window=self.entry, anchor="w")

        self.bind("<FocusIn>", self._on_focus_in)
        self.entry.bind("<FocusIn>", self._on_focus_in)
        self.entry.bind("<FocusOut>", self._on_focus_out)
        self.entry.bind("<Key>", lambda e: self.draw())
        self.entry.bind("<Configure>", self._on_configure)
        self.entry.bind("<Enter>", self._on_hover)
        self.entry.bind("<Leave>", self._on_leave)

        self.draw()

    def _on_focus_in(self, event: Event = None):  # NOQA
        self._focused = True
        self.update_state()

    def _on_focus_out(self, event: Event = None):  # NOQA
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
        self.entry.focus_set()

    def draw(self):
        # self.coords(self._border, 0, 0, self.winfo_width(), self.winfo_height())
        border_width: int = self.style("border_width")
        self.coords(self._entry, border_width, self.winfo_height() / 2)
        self.configure(
            background=self.style("bg"),  # bg color
            highlightbackground=self.style("border"),  # Border color
            highlightthickness=border_width,
            width=self.entry.winfo_width() + border_width,
        )
        self.itemconfigure(self._entry, height=self.winfo_height() - border_width * 2)
        self.entry.configure(
            background=self.style("bg"),
            borderwidth=0,
            highlightthickness=0,
            foreground=self.style("text"),
            insertbackground=self.style("text"),
            insertborderwidth=1,
            font=self.cget("font"),
        )
        # self.itemconfigure(self._entry, width=0)
