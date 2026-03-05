from config.technology import get_tech_table
from geometry import bbox
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

    program_name = os.path.splitext(os.path.basename(dxf_path))[0]

    # tabela technologiczna
    tech_table = get_tech_table(material, thickness)

    # parsowanie DXF
    geometry = parse_dxf(dxf_path)

    generate_preview(geometry, "output/output_preview.png")

    print("Wczytana geometria:")
    print(geometry)

    # budowa konturów
    contours = build_contours(geometry)

    # kolejność cięcia
    contours = apply_cut_order(contours)

    # kompensacja kerf
    contours = apply_kerf(contours)

    # lead-in
    contours = apply_leads(contours)
    print("Contours:")
    print(contours)

    # bounding box
    bbox = compute_bbox(geometry)
    part_placements = generate_part_placements(program_name, bbox)
    print("Bounding box:")
    print(bbox)
        
    # data
    date = datetime.now().strftime("%d.%m.%Y")

    # generowanie programu
    generate_program(
    program_name,
    thickness,
    tech_table,
    date,
    geometry,
    part_placements
)


if __name__ == "__main__":
    main()