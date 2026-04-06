import os
import pathlib


class Theme:
    themes = {}
    using_theme = "dark"

    INTERNAL_THEME_DIR = pathlib.Path(__file__).parent / "themes"

    def __init__(self):
        self.load_internal_themes()

    def load_internal_themes(self):
        for file in os.listdir(self.INTERNAL_THEME_DIR):
            self.load_from_file(yaml_filename=self.INTERNAL_THEME_DIR / file)

    def load_from_file(self, toml_filename=None, yaml_filename=None):
        if toml_filename:
            with open(toml_filename, "r") as f:
                data = f.read()
                return self.load_toml(data)
        if yaml_filename:
            with open(yaml_filename, "r") as f:
                data = f.read()
                return self.load_yaml(data)
        return None

    def load(self, data):
        if "copy" in data:
            copy = dict(self.themes[data["copy"]])
            copy.update(data)
        else:
            copy = data
        self.themes[data["name"]] = copy

    def load_toml(self, data):
        import toml

        data = toml.loads(data)
        self.load(data)
        return data["name"]

    def load_yaml(self, data):
        import yaml

        data = yaml.safe_load(data)
        self.load(data)
        return data["name"]

    def get_using_theme(self):
        return self.themes[self.using_theme]

    def _original_style(self, widget_name, state, style_name: str) -> str:
        # Custom style
        theme = self.get_using_theme()
        if state and state in theme["widgets"][widget_name]:
            if style_name not in theme["widgets"][widget_name][state]:
                return theme["widgets"][widget_name][style_name]
            else:
                return theme["widgets"][widget_name][state][
                    style_name
                ]
        # Rest style
        return theme["widgets"][widget_name][style_name]

    def style(self, widget_name, state, style_name: str) -> str | int:
        _s = self._original_style(widget_name, state, style_name)
        if isinstance(_s, str):
            if _s.startswith("@"):
                return self.get_using_theme()["styles"][_s[1:]]
        return _s



using_theme = Theme().get_using_theme()
