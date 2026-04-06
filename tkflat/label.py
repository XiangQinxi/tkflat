from typing import Literal

from .font import default_font
from .visual import Visual


class Label(Visual):
    def __init__(
        self,
        *args,
        text="Label",
        anchor: Literal[
            "nw", "n", "ne", "w", "center", "e", "sw", "s", "se"
        ] = "center",
        font=None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        self._widget_name = "Label"

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

    def draw(self):
        # self.coords(self._border, 0, 0, self.winfo_width(), self.winfo_height())
        self.coords(self._text, self.winfo_width() / 2, self.winfo_height() / 2)
        size = self.bbox(self._text)
        self.configure(
            background=self.transparent,  # Background color
            highlightthickness=None,
            highlightbackground=self.transparent,
            highlightcolor=self.transparent,
            width=size[2] - size[0],
        )
        self.itemconfig(
            self._text,
            text=self.cget("text"),
            anchor=self.cget("anchor"),
            fill=self.style("text"),
            font=self.cget("font"),
        )
