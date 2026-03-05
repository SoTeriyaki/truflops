from datetime import datetime

from config.technology import get_tech_table, load_tech_data
from utils.file_utils import load_template
from post.writer import apply_markers


def main():

    program_name = input("Nazwa programu: ")
    material = input("Material (SC/SN/OC/AL): ")
    thickness = float(input("Grubosc blachy: "))

    tech_table = get_tech_table(material, thickness)
    tech_data = load_tech_data(tech_table)

    template = load_template()

    markers = {

        "PROGRAM_NAME": program_name,
        "DATE": datetime.now().strftime("%d.%m.%Y"),
        "MATERIAL": material,
        "MATERIAL_ISO": "1.0038",
        "THICKNESS": thickness,
        "TECH_TABLE": tech_table,
        "TECH_DATA": tech_data,
        "SHEET_NAME": f"ST{int(thickness*1000):06}----3000x1500",

        "TOOLPATH": "",
        "PART_PLACEMENTS": "",
        "PART_POSITIONS": "",

        "PROGRAM_PATH": "",
        "HTML_PATH": ""
    }

    program = apply_markers(template, markers)

    with open("output/generated.lst", "w", encoding="utf-8") as f:
        f.write(program)

    print("Program wygenerowany.")


if __name__ == "__main__":
    main()