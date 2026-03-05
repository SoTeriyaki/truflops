from nest.grid import generate_grid_nest


def generate_part_placements(program_name, bbox, quantity):

    placements = generate_grid_nest(bbox, quantity)

    lines = []

    i = 1

    part_w = bbox["width"]
    part_h = bbox["height"]

    for p in placements:

        line = (
            f"DA,{i},'{program_name}','LO',"
            f"{p['x']:.3f},{p['y']:.3f},"
            f"{part_w:.3f},{part_h:.3f},0"
        )

        lines.append(line)

        i += 1

    return "\n".join(lines)