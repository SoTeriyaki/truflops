from config.technology import get_tech_table
from post.writer import generate_program
from dxf.parser import parse_dxf
from geometry.contour import build_contours
from geometry.lead import apply_leads

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

    print("Wczytana geometria:")
    print(geometry)
    contours = build_contours(geometry)
    print("Contours:")
    print(contours)
        
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