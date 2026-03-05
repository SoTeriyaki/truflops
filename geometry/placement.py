SAFE_OFFSET_X = 0
SAFE_OFFSET_Y = 10


def generate_part_placements(program_name, bbox, quantity)

    x = SAFE_OFFSET_X
    y = SAFE_OFFSET_Y

    lines = []

    lines.append(f"N190 X{x:.3f} Y{y:.3f}")
    lines.append(f"N200 SP1{program_name}")

    return "\n".join(lines)