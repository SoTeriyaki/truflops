def write_part_positions(placements):

    lines = []

    for p in placements:

        x = p["x"]
        y = p["y"]

        lines.append(f"G90")
        lines.append(f"X{x:.3f} Y{y:.3f}")
        lines.append("L SP1test")
        lines.append("")

    return "\n".join(lines)