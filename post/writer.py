import os
from post.subprogram import generate_subprogram


def apply_markers(template, markers):

    for key, value in markers.items():

        template = template.replace(
            "{" + key + "}",
            str(value)
        )

    return template


def generate_program(
        program_name,
        thickness,
        material,
        material_iso,
        density,
        tech_name,
        tech_data,
        date,
        contours,
        part_positions,
        part_width,
        part_height
    ):

    template_path = "templates/template.lst"
    output_path = "output/generated.lst"

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    part_center_x = part_width / 2
    part_center_y = part_height / 2

    markers = {

    "PROGRAM_NAME": program_name,
    "THICKNESS": thickness,
    "DATE": date,
    "PROGRAM_PATH": "",
    "HTML_PATH": "",
    "MATERIAL": material,
    "MATERIAL_ISO": material_iso,
    "DENSITY": density,
    "SHEET_NAME": f"{material}{int(thickness*10):03}----3000x1500",
    "TECH_NAME": tech_name,
    "TECH_DATA": tech_data,
    "TOOLPATH": generate_subprogram(contours),
    "PART_POSITIONS": part_positions,
    "PART_WIDTH": f"{part_width:.3f}",
    "PART_HEIGHT": f"{part_height:.3f}",

    }

    program = apply_markers(template, markers)

    os.makedirs("output", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(program)

    print("Program wygenerowany:")
    print(output_path)