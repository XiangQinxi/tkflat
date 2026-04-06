from typing import Literal

from .font import default_font
from .visual import Visual


class Button(Visual):
    def __init__(
        self,
        *args,
        text="Button",
        anchor: Literal[
            "nw", "n", "ne", "w", "center", "e", "sw", "s", "se"
        ] = "center",
        font=None,
        command=None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        self._command = command
        self.bind("<<Click>>", self._on_click)

        self._widget_name = "Button"

        if font is None:
            font = default_font()

        self._visual_attrs = {
            "text": text,
            "anchor": anchor,
            "font": font,
        }

        # self._border = self.create_rectangle(
        #     0, 0, w, h, outline="#2D3234", fill="#202527"
        # )
        self._text = self.create_text(
            0, 0, text=self.cget("text"), anchor=self.cget("anchor"), font=font  # NOQA
        )

        self.draw()

    def _on_click(self, event):
        if self._command:
            self._command()

    def draw(self):
        # self.coords(self._border, 0, 0, self.winfo_width(), self.winfo_height())
        self.coords(self._text, self.winfo_width() / 2, self.winfo_height() / 2)
        self.configure(
            background=self.style("bg"),  # Background color
            highlightbackground=self.style("border"),  # Border color
            # borderwidth=self._theme[self._style][self._state]["border_width"],  # Border width
            highlightthickness=self.style("border_width"),
        )
        self.itemconfig(
            self._text,
            text=self.cget("text"),
            anchor=self.cget("anchor"),
            fill=self.style("text"),
            font=self.cget("font"),
        )
