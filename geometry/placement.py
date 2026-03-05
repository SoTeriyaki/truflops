def generate_part_placements(program_name, bbox):

    x = 0
    y = 0

    lines = []

    lines.append(f"N190 X{x:.3f} Y{y:.3f}")
    lines.append(f"N200 SP1{program_name}")

    return "\n".join(lines)