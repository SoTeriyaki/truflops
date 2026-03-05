def translate_geometry(geometry, dx, dy):

    new_geometry = []

    for g in geometry:

        g2 = g.copy()

        if g["type"] == "circle":

            x, y = g["center"]
            g2["center"] = (x + dx, y + dy)

        elif g["type"] == "line":

            x1, y1 = g["start"]
            x2, y2 = g["end"]

            g2["start"] = (x1 + dx, y1 + dy)
            g2["end"] = (x2 + dx, y2 + dy)

        elif g["type"] == "arc":

            x, y = g["center"]
            g2["center"] = (x + dx, y + dy)

        new_geometry.append(g2)

    return new_geometry