import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

SHEET_WIDTH = 3000
SHEET_HEIGHT = 1500


def compute_nest_bbox(placements, bbox):
    """
    Oblicza rzeczywisty bounding box całego nestu
    """

    part_w = bbox["width"]
    part_h = bbox["height"]

    max_x = 0
    max_y = 0

    for p in placements:

        x = p["x"] + part_w
        y = p["y"] + part_h

        if x > max_x:
            max_x = x

        if y > max_y:
            max_y = y

    return max_x, max_y


def generate_preview(contours, placements, bbox, output_path):

    fig, ax = plt.subplots(figsize=(12, 6))

    # zakres arkusza
    ax.set_xlim(0, SHEET_WIDTH)
    ax.set_ylim(0, SHEET_HEIGHT)

    # siatka
    ax.set_xticks(range(0, 3001, 200))
    ax.set_yticks(range(0, 1501, 100))
    ax.grid(True)

    # rysowanie wszystkich detali
    for place in placements:

        offset_x = place["x"]
        offset_y = place["y"]

        for c in contours:

            if c["type"] == "circle":

                cx, cy = c["center"]
                r = c["radius"]

                circle = Circle(
                    (cx + offset_x, cy + offset_y),
                    r,
                    fill=False
                )

                ax.add_patch(circle)

            elif c["type"] == "arc":

                cx, cy = c["center"]
                r = c["radius"]

                arc = Arc(
                    (cx + offset_x, cy + offset_y),
                    2 * r,
                    2 * r,
                    angle=0,
                    theta1=c["start_angle"],
                    theta2=c["end_angle"]
                )

                ax.add_patch(arc)

    # bounding box nestu
    nest_w, nest_h = compute_nest_bbox(placements, bbox)

    ax.set_title(
        f"Nest size: {nest_w:.1f} x {nest_h:.1f} mm | "
        f"Parts: {len(placements)}"
    )

    ax.set_aspect("equal", adjustable="box")

    plt.savefig(output_path, dpi=300)
    plt.close()

    print("Preview wygenerowany:")
    print(output_path)