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
        part_height,
        dry_run
    ):

    template_path = "templates/template.lst"
    output_path = "output/generated.lst"

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    part_center_x = part_width / 2
    part_center_y = part_height / 2

    # --------------------------------
    # TOOLPATH GENERATION
    # --------------------------------

    toolpath_cut = generate_subprogram(contours)

    # --------------------------------
    # DRY RUN SECTION
    # --------------------------------

    if dry_run:

        dry_section = f"""
N140 MSG("DRY RUN START")

N145 TC_LASER_OFF(2)
N150 TC_POS_LEVEL(60.0)

N160 F70500
G90

; ===== DRY RUN START =====
{part_positions}
; ===== DRY RUN END =====

N170 MSG("DRY RUN END")

N180 TC_POS_LEVEL(40.0)
N185 TC_LASER_ON
N190 F141000
"""

    else:

        dry_section = ""

    # --------------------------------
    # MARKERS
    # --------------------------------

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

        "DRY_SECTION": dry_section,
        "CUT_TOOLPATH": toolpath_cut,

        "PART_POSITIONS": part_positions,

        "PART_WIDTH": f"{part_width:.3f}",
        "PART_HEIGHT": f"{part_height:.3f}",

        "PART_CENTER_X": f"{part_center_x:.3f}",
        "PART_CENTER_Y": f"{part_center_y:.3f}",
    }

    # --------------------------------
    # APPLY MARKERS
    # --------------------------------

    program = apply_markers(template, markers)

    # --------------------------------
    # SAVE FILE
    # --------------------------------

    os.makedirs("output", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(program)

    print("Program wygenerowany:")
    print(output_path)