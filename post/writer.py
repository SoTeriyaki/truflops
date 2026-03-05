import os
from post.subprogram import generate_toolpath


def apply_markers(template, markers):

    for key, value in markers.items():

        template = template.replace(
            "{" + key + "}",
            str(value)
        )

    return template


def generate_program(program_name, thickness, tech_table, date, geometry):

    template_path = "templates/template.lst"
    output_path = "output/generated.lst"

    # wczytanie template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # markery
    markers = {
        "PROGRAM_NAME": program_name,
        "THICKNESS": thickness,
        "DATE": date,
        "TECH_TABLE": tech_table,
        "TOOLPATH": "",
        "PART_PLACEMENTS": ""
    }

    # podmiana markerów
    program = apply_markers(template, markers)

    # stworzenie folderu output jeśli nie istnieje
    os.makedirs("output", exist_ok=True)

    # zapis pliku
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(program)

    print("Program wygenerowany:")
    print(output_path)