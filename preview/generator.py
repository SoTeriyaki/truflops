import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc

from geometry import bbox


SHEET_WIDTH = 3000
SHEET_HEIGHT = 1500


def generate_preview(contours, placements, bbox, output_path):

    fig, ax = plt.subplots(figsize=(12,6))

    # arkusz
    ax.set_xlim(0, SHEET_WIDTH)
    ax.set_ylim(0, SHEET_HEIGHT)

    # siatka
    ax.set_xticks(range(0, 3001, 200))
    ax.set_yticks(range(0, 1501, 100))
    ax.grid(True)

    # rysowanie detali
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

            if c["type"] == "arc":

                cx, cy = c["center"]
                r = c["radius"]

                arc = Arc(
                    (cx + offset_x, cy + offset_y),
                    2*r,
                    2*r,
                    angle=0,
                    theta1=c["start_angle"],
                    theta2=c["end_angle"]
                )

                ax.add_patch(arc)

    def compute_nest_bbox(placements, bbox):

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

    # bounding box detalu
    part_w = bbox["width"]
    part_h = bbox["height"]

    required_w = part_w + 20
    required_h = part_h + 20

    ax.set_title(
    f"Part size: {part_w:.1f} x {part_h:.1f} mm | "
    f"Required scrap: {required_w:.1f} x {required_h:.1f} mm"
    )

    plt.gca().set_aspect("equal", adjustable="box")

    plt.savefig(output_path, dpi=300)

    plt.close()

    print("Preview wygenerowany:")
    print(output_path)