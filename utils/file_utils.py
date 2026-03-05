from pathlib import Path


def load_template():

    path = Path("templates/template.lst")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()