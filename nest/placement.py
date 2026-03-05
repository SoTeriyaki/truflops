from nest.grid import generate_grid_nest


def generate_part_placements(program_name, bbox, quantity):

    placements = generate_grid_nest(bbox, quantity)

    lines = []

    i = 1

    for p in placements:

        line = (
            f"DA,{i},'{program_name}','LO',"
            f"{p['x']:.3f},{p['y']:.3f},0,0,0"
        )

        lines.append(line)

        i += 1

    return "\n".join(lines)