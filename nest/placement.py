def generate_part_placements(program_name, bbox, quantity):

    start_x = 30
    start_y = 30

    margin = 20

    step_x = bbox["width"] + margin
    step_y = bbox["height"] + margin

    sheet_x = 3000
    sheet_y = 1500

    cols = int(sheet_y // step_y)

    lines = []

    for i in range(quantity):

        row = i // cols
        col = i % cols

        x = start_x + row * step_x
        y = start_y + col * step_y

        lines.append(f"G90")
        lines.append(f"X{x:.3f} Y{y:.3f}")
        lines.append(f"SP1{program_name}")
        lines.append("")

    return "\n".join(lines)