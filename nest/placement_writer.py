def write_part_positions(placements):

    lines = []

    for i, p in enumerate(placements, start=1):

        x = p["x"]
        y = p["y"]

        lines.append("G90")
        lines.append(f"X{x:.3f} Y{y:.3f}")
        lines.append("L SP1test")
        lines.append("")

    return "\n".join(lines)