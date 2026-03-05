import os
from post.subprogram import generate_toolpath


def apply_markers(template, markers):

    for key, value in markers.items():

        template = template.replace(
            "{" + key + "}",
            str(value)
        )

    return template


def generate_program(program_name, thickness, tech_table, date, contours, part_positions):

    template_path = "templates/template.lst"
    output_path = "output/generated.lst"

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    markers = {

        "PROGRAM_NAME": program_name,
        "THICKNESS": thickness,
        "DATE": date,

        "TECH_TABLE": tech_table,

        "PROGRAM_PATH": "",
        "HTML_PATH": "",
        "MATERIAL": "SC",
        "SHEET_NAME": "ST004000----3000x1500",

        "TOOLPATH": generate_toolpath(contours),

        "PART_POSITIONS": part_positions
    }

    program = apply_markers(template, markers)

    os.makedirs("output", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(program)

    print("Program wygenerowany:")
    print(output_path)