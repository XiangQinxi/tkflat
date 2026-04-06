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

    def load_toml(self, data):
        import toml
        import yaml

        data = toml.loads(data)
        print(yaml.safe_dump(data, default_flow_style=False))
        self.themes[data["name"]] = data
        return data["name"]

    def load_yaml(self, data):
        import yaml

        data = yaml.safe_load(data)
        self.themes[data["name"]] = data
        return data["name"]

    def get_using_theme(self):
        return self.themes[self.using_theme]


using_theme = Theme().get_using_theme()
