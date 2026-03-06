def write_part_positions(placements):

    lines = []

    lines.append("G90")

    for p in placements:

        x = p["x"]
        y = p["y"]

        lines.append(f"X{x:.3f} Y{y:.3f}")
        lines.append("SP1test")

    return "\n".join(lines)