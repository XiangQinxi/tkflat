from tkinter.font import Font

_font = None


def default_font():
    global _font
    if _font is None:
        _font = Font(
            name="flatDefaultFont",
            family="segoe ui",
            size=10,
            weight="normal",
        )
    return _font
