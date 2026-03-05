from geometry import bbox
from geometry.align import align_to_origin
from geometry.cut_order import apply_cut_order
from post.writer import generate_program
from dxf.parser import parse_dxf
from geometry.contour import build_contours
from geometry.lead import apply_leads
from preview.generator import generate_preview
from geometry.bbox import compute_bbox
from geometry.kerf import apply_kerf
from geometry.direction import detect_direction
from nest.placement import generate_part_placements
from nest.placement_writer import write_part_positions
from nest.grid import generate_grid_nest
from config.materials import MATERIALS
from config.technology_selector import get_tech_name
from config.technology_loader import load_technology

import os
from datetime import datetime


def main():

    dxf_path = input("Sciezka do DXF: ").strip().strip('"')
    material = input("Material (SC/SN/OC/AL): ").upper()
    thickness = float(input("Grubosc blachy: "))
    quantity = int(input("Liczba detali: "))
    material_data = MATERIALS[material]
    material_iso = material_data["iso"]
    density = material_data["density"]
    program_name = os.path.splitext(os.path.basename(dxf_path))[0]

    # tabela technologiczna
    tech_table = get_tech_name(material, thickness)
    tech_data = load_technology(tech_name)

    # parsowanie DXF
    geometry = parse_dxf(dxf_path)

    # AUTO ALIGN
    geometry = align_to_origin(geometry)

    print("Wczytana geometria:")
    print(geometry)

    # budowa konturów
    contours = build_contours(geometry)

    # kolejność cięcia
    contours = apply_cut_order(contours)

    # kierunek
    contours = detect_direction(contours)

    # kerf
    contours = apply_kerf(contours)

    # lead
    contours = apply_leads(contours)

    print("Contours:")
    print(contours)

    # bounding box
    bbox = compute_bbox(geometry)
    part_width = bbox["width"]
    part_height = bbox["height"]

    print("Bounding box:")
    print(bbox)

    # grid nest
    placements = generate_grid_nest(bbox, quantity)
    part_positions = write_part_positions(part_placements)

    # preview
    generate_preview(
        contours,
        placements,
        bbox,
        "output/output_preview.png"
    )


    # data programu
    date = datetime.now().strftime("%d.%m.%Y")

    # generowanie programu
    generate_program(
        program_name,
        thickness,
        material,
        material_iso,
        density,
        tech_table,
        tech_data,
        date,
        contours,
        part_positions,
        part_width,
        part_height
    )


if __name__ == "__main__":
    main()