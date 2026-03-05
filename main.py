from config.technology import get_tech_table
from geometry import bbox
from post.writer import generate_program
from dxf.parser import parse_dxf
from geometry.contour import build_contours
from geometry.lead import apply_leads
from preview.generator import generate_preview
from geometry.bbox import compute_bbox

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
    generate_preview(geometry,"output/output_preview.png")
    print("Wczytana geometria:")
    print(geometry)
    contours = build_contours(geometry)
    contours = apply_leads(contours)
    print("Contours:")
    print(contours)
    bbox = compute_bbox(geometry)
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
    contours
    )   


if __name__ == "__main__":
    main()