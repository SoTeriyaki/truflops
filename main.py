from config.technology import get_tech_table
from geometry import bbox
from geometry.align import align_to_origin
from geometry.cut_order import apply_cut_order
from post.writer import generate_program
from dxf.parser import parse_dxf
from geometry.contour import build_contours
from geometry.lead import apply_leads
from preview.generator import generate_preview
from geometry.bbox import compute_bbox
from geometry.placement import generate_part_placements
from geometry.kerf import apply_kerf
from geometry.direction import detect_direction

import os
from datetime import datetime


def main():

    dxf_path = input("Sciezka do DXF: ").strip().strip('"')
    material = input("Material (SC/SN/OC/AL): ").upper()
    thickness = float(input("Grubosc blachy: "))
    quantity = int(input("Liczba detali: "))

    program_name = os.path.splitext(os.path.basename(dxf_path))[0]

    # tabela technologiczna
    tech_table = get_tech_table(material, thickness)

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

    print("Bounding box:")
    print(bbox)

    # preview toolpath
    generate_preview(contours, bbox, "output/output_preview.png")

    # placement
    part_placements = generate_part_placements(program_name, bbox, quantity)

    # data programu
    date = datetime.now().strftime("%d.%m.%Y")

    # generowanie programu
    generate_program(
        program_name,
        thickness,
        tech_table,
        date,
        contours,
        part_placements
    )


if __name__ == "__main__":
    main()