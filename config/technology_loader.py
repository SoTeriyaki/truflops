from pathlib import Path

TECH_DIR = Path("config/technology")

def load_technology(tech_name):

    path = TECH_DIR / f"{tech_name}.lst"

    if not path.exists():
        raise RuntimeError(f"Brak technologii: {tech_name}")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()