import matplotlib.pyplot as plt
import matplotlib.patches as patches


SHEET_X = 3000
SHEET_Y = 1500
SAFE_MARGIN = 20


def compute_bounds(geometry):

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

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    width = max_x - min_x
    height = max_y - min_y

    return width, height


def generate_preview(geometry, output_path):

    width, height = compute_bounds(geometry)

    waste_x = width + SAFE_MARGIN
    waste_y = height + SAFE_MARGIN

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.set_xlim(0, SHEET_X)
    ax.set_ylim(0, SHEET_Y)

    ax.set_aspect("equal")

    ax.set_title(
        f"Detal: {round(width)} x {round(height)} mm / Wymagany odpad: {round(waste_x)} x {round(waste_y)} mm"
    )

    # ---------- DRAW GEOMETRY ----------

    for g in geometry:

        if g["type"] == "circle":

            cx, cy = g["center"]
            r = g["radius"]

            circle = patches.Circle((cx, cy), r, fill=False)

            ax.add_patch(circle)

        elif g["type"] == "polyline":

            xs = [p[0] for p in g["points"]]
            ys = [p[1] for p in g["points"]]

            ax.plot(xs, ys)

        elif g["type"] == "arc":

            x1, y1 = g["start"]
            x2, y2 = g["end"]

            ax.plot([x1, x2], [y1, y2])

    ax.set_facecolor("#f0f0f0")

    plt.savefig(output_path, dpi=150)
    plt.close()