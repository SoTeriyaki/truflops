def compute_bbox(geometry):

    xs = []
    ys = []

    for g in geometry:

        if g["type"] == "circle":

            cx, cy = g["center"]
            r = g["radius"]

            xs.extend([cx - r, cx + r])
            ys.extend([cy - r, cy + r])

        elif g["type"] == "polyline":

            for x, y in g["points"]:
                xs.append(x)
                ys.append(y)

        elif g["type"] == "arc":

            xs.append(g["start"][0])
            ys.append(g["start"][1])

            xs.append(g["end"][0])
            ys.append(g["end"][1])

            xs.append(g["center"][0])
            ys.append(g["center"][1])

    min_x = min(xs)
    max_x = max(xs)

    min_y = min(ys)
    max_y = max(ys)

    width = max_x - min_x
    height = max_y - min_y

    return {
        "min_x": min_x,
        "max_x": max_x,
        "min_y": min_y,
        "max_y": max_y,
        "width": width,
        "height": height
    }