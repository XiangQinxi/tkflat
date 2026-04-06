from tkinter import Canvas, Event

from .styled import Styled


class Visual(Canvas, Styled):
    def __init__(self, *args, width=66, height=34, **kwargs):
        Canvas.__init__(self, *args, width=width, height=height, **kwargs)
        Styled.__init__(self)

        self._widget_name = "Visual"
        self.__last_size = (0, 0)
        self._enter = False
        self._press = False
        self._focused = False
        self.bind("<Configure>", self._on_configure)
        self.bind("<Enter>", self._on_hover)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button>", self._on_press)
        self.bind("<ButtonRelease>", self._on_release)

        self._visual_attrs = {}

    @property
    def transparent(self):
        try:
            return self.master.cget("background")
        except AttributeError:
            if hasattr(self.master, "style"):
                return self.master.style("background")
        return False

    def update_state(self):
        if self._enter:
            if self._press:
                self._state = "press"
            else:
                self._state = "hover"
        else:
            self._state = None
        self.draw()

    def _on_press(self, event: Event = None):  # NOQA
        self._press = True
        self.focus_set()
        self.update_state()

    def _on_release(self, event: Event = None):  # NOQA
        self._press = False
        self.update_state()
        if self._enter:
            self.event_generate("<<Click>>")

    def _on_hover(self, event: Event = None):  # NOQA
        self._enter = True
        self.update_state()

    def _on_leave(self, event: Event = None):  # NOQA
        self._enter = False
        self.update_state()

    def _on_configure(self, event: Event):
        w, h = event.width, event.height
        if (w, h) != self.__last_size:
            self.__last_size = (w, h)
            self.draw()

    def draw(self):
        pass

    # region Configure / Cget
    def configure(self, **kwargs):
        for k, v in kwargs.items():
            if k in self._visual_attrs:
                self._visual_attrs[k] = v
                self.draw()

        return super().configure(**kwargs)

    def cget(self, key):
        if key in self._visual_attrs:
            return self._visual_attrs[key]
        return super().cget(key)
